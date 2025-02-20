"""python3 -m pytest in project root"""

from __future__ import annotations

import os
from io import BufferedReader
from pathlib import Path

import pytest

THISDIR = str(Path(__file__).resolve().parent)

from gimpformats.GimpGgrGradient import GimpGgrGradient

project = GimpGgrGradient()


def colorArray(numPoints: int) -> list:
	"""colour array."""
	colors = []
	i = 0.0
	inc = 1.0 / numPoints
	while i < 1.0:
		colors.append(project.getColor(i))
	i += inc
	return colors


def saveColors(f: BufferedReader, colorArray: list) -> None:
	"""save colours."""
	f.write(b"r, g, b, a\n")
	for c in colorArray:
		_line: list[str] = []
		for _chan in c:
			_line.append(str(c))
			line = ", ".join(_line) + "\n"
			f.write(line.encode("utf-8"))


@pytest.mark.parametrize(("file_name"), ["Cold_Steel_2", "Mexican_flag"])
def test_grgradient_roundtrip(file_name: str) -> None:
	src = f"{THISDIR}/{file_name}.ggr"
	dest = f"{THISDIR}/actualOutput_{file_name}.ggr"
	project.load(src)
	project.save(dest)
	original = open(src, "rb")
	actual = open(dest, "rb")
	assert actual.read() == original.read().replace(b"\r\n", b"\n")
	original.close()
	actual.close()
	os.remove(dest)
