"""python3 -m pytest in project root"""

from __future__ import annotations

import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
from imgcompare import imgcompare

from gimpformats.gimpXcfDocument import GimpDocument

dut = GimpDocument()


def test_singleMaskedGroup() -> None:
	"""Test a single group with layer mask."""
	dut.load(f"{THISDIR}/single-masked-group.xcf")
	result = dut.image
	assert imgcompare.is_equal(
		result,
		f"{THISDIR}/single-masked-group.tga",
		tolerance=0.2,
	)


def test_multipleMaskedGroups() -> None:
	"""Test multiple layer groups with masks."""
	dut.load(f"{THISDIR}/multiple-masked-groups.xcf")
	result = dut.image
	assert imgcompare.is_equal(
		result,
		f"{THISDIR}/multiple-masked-groups.tga",
		tolerance=0.2,
	)


def test_multipleOffsetMaskedGroups() -> None:
	"""Test multiple offset layer groups with masks."""
	dut.load(f"{THISDIR}/multiple-offset-masked-groups.xcf")
	result = dut.image
	result.save("test.png")
	assert imgcompare.is_equal(
		result,
		f"{THISDIR}/multiple-offset-masked-groups.tga",
		tolerance=0.2,
	)
