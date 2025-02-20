from pathlib import Path

import pytest
from imgcompare import imgcompare

from gimpformats.gimpXcfDocument import GimpDocument

THISDIR = Path(__file__).resolve().parent


@pytest.fixture
def gimp_doc() -> GimpDocument:
	"""Fixture to return a fresh instance of GimpDocument for each test."""
	return GimpDocument()


@pytest.mark.parametrize("xcf_path", list((THISDIR / "rods-custom-font-xcf-files").glob("*.xcf")))
def test_font_comparison(gimp_doc: GimpDocument, xcf_path: Path) -> None:
	"""Test if the generated image matches the expected output."""
	output_png = THISDIR / f"rods-custom-font-xcf-files/{xcf_path.name}_actual.png"
	expected_png = THISDIR / f"rods-custom-font-xcf-files/{xcf_path.name}.png"

	gimp_doc.load(str(xcf_path))
	gimp_doc.image.save(str(output_png))
	# gimp_doc.image.save(str(expected_png))

	assert imgcompare.is_equal(gimp_doc.image, str(expected_png), tolerance=0.01)
