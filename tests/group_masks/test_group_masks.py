"""python3 -m pytest in project root"""

from __future__ import annotations

from pathlib import Path

import pytest

THISDIR = str(Path(__file__).resolve().parent)

from imgcompare import imgcompare

from gimpformats.gimpXcfDocument import GimpDocument

project = GimpDocument()


@pytest.mark.parametrize(
	("image_name"),
	[
		"multiple-offset-masked-groups",
		"multiple-masked-groups",
		"single-masked-group",
		"xcf_mask_test",
	],
)
def test_multipleOffsetMaskedGroups(image_name: str) -> None:
	"""Test multiple offset layer groups with masks."""
	project.load(f"{THISDIR}/{image_name}.xcf")
	result = project.image
	des_im = f"{THISDIR}/{image_name}.png"
	# result.save(des_im)
	assert imgcompare.is_equal(
		result,
		des_im,
		tolerance=0.2,
	)
