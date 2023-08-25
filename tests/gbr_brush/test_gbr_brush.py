"""python3 -m pytest in project root
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
from imgcompare import imgcompare

from gimpformats.GimpGbrBrush import GimpGbrBrush

dut = GimpGbrBrush()


def test_pepper():
	"""test pepper"""
	dut.load(f"{THISDIR}/pepper.gbr")
	# test image saving (implicit)
	dut.save(f"{THISDIR}/actualOutput_pepper.png")
	# test for image match
	assert imgcompare.is_equal(dut.image, f"{THISDIR}/desiredOutput_pepper.png", tolerance=0.2)
	os.remove(f"{THISDIR}/actualOutput_pepper.png")
	# test round-trip compatibility
	dut.save(f"{THISDIR}/actualOutput_pepper.gbr")
	original = open(f"{THISDIR}/pepper.gbr", "rb")
	actual = open(f"{THISDIR}/actualOutput_pepper.gbr", "rb")
	assert actual.read() == original.read().replace(b"\r\n", b"\n")
	original.close()
	actual.close()
	os.remove(f"{THISDIR}/actualOutput_pepper.gbr")


def test_dunes():
	"""test dunes"""
	dut.load(f"{THISDIR}/dunes.gbr")
	# test image saving (explicit)
	dut.image.save(f"{THISDIR}/actualOutput_dunes.png")
	# test for image match
	assert imgcompare.is_equal(dut.image, f"{THISDIR}/desiredOutput_dunes.png", tolerance=0.2)
	os.remove(f"{THISDIR}/actualOutput_dunes.png")
	# test round-trip compatibility
	dut.save(f"{THISDIR}/actualOutput_dunes.gbr")
	original = open(f"{THISDIR}/dunes.gbr", "rb")
	actual = open(f"{THISDIR}/actualOutput_dunes.gbr", "rb")
	assert actual.read() == original.read().replace(b"\r\n", b"\n")
	original.close()
	actual.close()
	os.remove(f"{THISDIR}/actualOutput_dunes.gbr")
