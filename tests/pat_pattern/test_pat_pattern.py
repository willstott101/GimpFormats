"""python3 -m pytest in project root
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from imgcompare import imgcompare

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

from gimpformats.GimpPatPattern import GimpPatPattern

dut = GimpPatPattern()


def test_3dgreen() -> None:
	dut.load(f"{THISDIR}/3dgreen.pat")
	# test image saving (implicit)
	dut.save(f"{THISDIR}/actualOutput_3dgreen.png")
	# test for image match
	assert imgcompare.is_equal(dut.image, f"{THISDIR}/desiredOutput_3dgreen.png", tolerance=0.2)
	os.remove(f"{THISDIR}/actualOutput_3dgreen.png")
	# test round-trip compatibility
	dut.save(f"{THISDIR}/actualOutput_3dgreen.pat")
	original = open(f"{THISDIR}/3dgreen.pat", "rb")
	actual = open(f"{THISDIR}/actualOutput_3dgreen.pat", "rb")
	assert actual.read() == original.read().replace(b"\r\n", b"\n")
	original.close()
	actual.close()
	os.remove(f"{THISDIR}/actualOutput_3dgreen.pat")


def test_leopard() -> None:
	dut.load(f"{THISDIR}/leopard.pat")
	# test image saving (explicit)
	dut.image.save(f"{THISDIR}/actualOutput_leopard.png")
	# test for image match
	assert imgcompare.is_equal(dut.image, f"{THISDIR}/desiredOutput_leopard.png", tolerance=0.2)
	os.remove(f"{THISDIR}/actualOutput_leopard.png")
	# test round-trip compatibility
	dut.save(f"{THISDIR}/actualOutput_leopard.pat")
	original = open(f"{THISDIR}/leopard.pat", "rb")
	actual = open(f"{THISDIR}/actualOutput_leopard.pat", "rb")
	assert actual.read() == original.read()
	original.close()
	actual.close()
	os.remove(f"{THISDIR}/actualOutput_leopard.pat")
