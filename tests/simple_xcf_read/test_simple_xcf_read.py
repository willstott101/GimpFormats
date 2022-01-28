#!/usr/bin/env python3
"""python3 -m pytest in project root
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from imgcompare import imgcompare

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

from gimpformats.gimpXcfDocument import GimpDocument

dut = GimpDocument()


def test_oneLayerWithTransparency():
	"""test an image."""
	dut.load(f"{THISDIR}/testOneLayerWithTransparency.xcf")
	dut.image.save(f"{THISDIR}/testOneLayerWithTransparency.png")
	assert imgcompare.is_equal(
		dut.image, f"{THISDIR}/testOneLayerWithTransparency_expected.png", tolerance=0.2
	)


def test_complexImage():
	"""test an image."""
	dut.load(f"{THISDIR}/testComplexImage.xcf")
	dut.image.save(f"{THISDIR}/testComplexImage.png")
	assert imgcompare.is_equal(dut.image, f"{THISDIR}/testComplexImage_expected.png", tolerance=0.2)
