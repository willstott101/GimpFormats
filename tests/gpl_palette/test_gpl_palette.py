"""python3 -m pytest in project root"""

from __future__ import annotations

import os
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)

from gimpformats.GimpGplPalette import GimpGplPalette

dut = GimpGplPalette()


def test_plasma() -> None:
	"""test plasma."""
	dut.load(f"{THISDIR}/plasma.gpl")
	# test round-trip compatibility
	dut.save(f"{THISDIR}/actualOutput_plasma.gpl")
	original = open(f"{THISDIR}/plasma.gpl")
	actual = open(f"{THISDIR}/actualOutput_plasma.gpl")
	assert actual.read() == original.read()
	original.close()
	actual.close()
	os.remove(f"{THISDIR}/actualOutput_plasma.gpl")


def test_web() -> None:
	"""test web."""
	dut.load(f"{THISDIR}/web.gpl")
	assert dut.name == "Web Safe Colors"
	assert dut.columns == 6
	assert len(dut.colorNames) == 216
	assert len(dut.colors) == 216


def test_pantone() -> None:
	"""test pantone."""
	dut.load(f"{THISDIR}/pantone.gpl")
	assert dut.name == "Pantone colors"
	assert dut.columns == 16
	assert len(dut.colorNames) == 940
	assert len(dut.colors) == 940
