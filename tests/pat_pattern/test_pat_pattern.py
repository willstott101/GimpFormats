import sys
from pathlib import Path

import pytest
from imgcompare import imgcompare

from gimpformats.GimpPatPattern import GimpPatPattern

# Setting up paths
THISDIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THISDIR.parent))

# Prepare the object to test
project = GimpPatPattern()


@pytest.mark.parametrize(
	("pattern_name", "desired_image"),
	[
		("3dgreen", "desiredOutput_3dgreen.png"),
		("leopard", "desiredOutput_leopard.png"),
	],
)
def test_pattern(pattern_name: str, desired_image: str) -> None:
	"""Test pattern functionality."""
	project.load(THISDIR / f"{pattern_name}.pat")

	# Test image saving
	output_png = f"actualOutput_{pattern_name}.png"
	project.save(THISDIR / output_png)

	# Test image match
	assert imgcompare.is_equal(project.image, (THISDIR / desired_image).as_posix(), tolerance=0.2)

	# Test round-trip compatibility
	output_pat = f"actualOutput_{pattern_name}.pat"
	project.save(THISDIR / output_pat)
	with open(THISDIR / f"{pattern_name}.pat", "rb") as original, open(
		THISDIR / f"actualOutput_{pattern_name}.pat", "rb"
	) as actual:
		assert actual.read() == original.read()

	for file in [output_png, output_pat]:
		file_path = THISDIR / file
		if file_path.exists():
			file_path.unlink()
