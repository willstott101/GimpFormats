"""
TODO: THIS IS BROKEN

python3 -m pytest in project root
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
from imgcompare import imgcompare

from gimpformats.GimpGihBrushSet import GimpGihBrushSet

dut = GimpGihBrushSet()


@pytest.mark.skip("RuntimeError")
def test_wilber() -> None:
	"""test wilber."""
	dut.load(f"{THISDIR}/Wilber.gih")
	# test image saving (implicit)
	dut.save(f"{THISDIR}/actualOutput_Wilber.png")
	# test for image match
	assert imgcompare.is_equal(dut.image, f"{THISDIR}/desiredOutput_Wilber.png", tolerance=0.2)
	os.remove(f"{THISDIR}/actualOutput_Wilber.png")
	# test round-trip compatibility
	dut.save(f"{THISDIR}/actualOutput_Wilber.gih")
	original = open(f"{THISDIR}/Wilber.gih", "rb").read()
	actual = open(f"{THISDIR}/actualOutput_Wilber.gih", "rb").read()
	assert actual == original
	os.remove(f"{THISDIR}/actualOutput_Wilber.gih")


@pytest.mark.skip("RuntimeError")
def test_feltpen() -> None:
	"""test felt pen."""
	dut.load(f"{THISDIR}/feltpen.gih")
	# test image saving (explicit)
	dut.image.save(f"{THISDIR}/actualOutput_feltpen.png")
	# test for image match
	assert imgcompare.is_equal(dut.image, f"{THISDIR}/desiredOutput_feltpen.png", tolerance=0.2)
	os.remove(f"{THISDIR}/actualOutput_feltpen.png")
	# test round-trip compatibility
	dut.save(f"{THISDIR}/actualOutput_feltpen.gih")
	original = open(f"{THISDIR}/feltpen.gih", "rb").read()
	actual = open(f"{THISDIR}/actualOutput_feltpen.gih", "rb").read()
	assert actual == original
	os.remove(f"{THISDIR}/actualOutput_feltpen.gih")
