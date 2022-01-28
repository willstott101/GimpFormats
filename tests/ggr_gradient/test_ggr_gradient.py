#!/usr/bin/env python3
"""python3 -m pytest in project root
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
from gimpformats.GimpGgrGradient import GimpGgrGradient

dut = GimpGgrGradient()


def colorArray(numPoints):
	"""colour array."""
	colors = []
	i = 0.0
	inc = 1.0 / numPoints
	while i < 1.0:
		colors.append(dut.getColor(i))
	i += inc
	return colors


def saveColors(f, colorArray):
	"""save colours."""
	f.write(b"r, g, b, a\n")
	for c in colorArray:
		line = []
		for _chan in c:
			line.append(str(c))
			line = ", ".join(line) + "\n"
			f.write(line.encode("utf-8"))


def test_coldSteel():
	"""test cold steel."""
	dut.load(f"{THISDIR}/Cold_Steel_2.ggr")
	# test round-trip compatibility
	dut.save(f"{THISDIR}/actualOutput_Cold_Steel_2.ggr")
	original = open(f"{THISDIR}/Cold_Steel_2.ggr", "rb")
	actual = open(f"{THISDIR}/actualOutput_Cold_Steel_2.ggr", "rb")
	assert actual.read() == original.read().replace(b"\r\n", b"\n")
	original.close()
	actual.close()
	os.remove(f"{THISDIR}/actualOutput_Cold_Steel_2.ggr")
	# TODO: test calculated colors
	# colors=colorArray(512)
	# actual=open(__HERE__+'actualOutput_Cold_Steel_2.csv','wb')
	# saveColors(actual,colors)
