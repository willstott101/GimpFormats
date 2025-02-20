"""python3 -m pytest in project root"""

from __future__ import annotations

import os
from pathlib import Path

import pytest
from imgcompare import imgcompare

from gimpformats.GimpGbrBrush import GimpGbrBrush

THISDIR = str(Path(__file__).resolve().parent)


project = GimpGbrBrush()


@pytest.mark.parametrize(("file_name"), ["pepper", "dunes"])
def test_gbrbrush(file_name: str) -> None:
	"""test {file_name}"""
	project.load(f"{THISDIR}/{file_name}.gbr")
	project.save(f"{THISDIR}/actualOutput_{file_name}.png")

	assert imgcompare.is_equal(
		project.image, f"{THISDIR}/desiredOutput_{file_name}.png", tolerance=0.2
	)
	os.remove(f"{THISDIR}/actualOutput_{file_name}.png")


@pytest.mark.parametrize(("file_name"), ["pepper", "dunes"])
def test_gbrbrush_roundtrip(file_name: str) -> None:
	src = f"{THISDIR}/{file_name}.gbr"
	dest = f"{THISDIR}/actualOutput_{file_name}.gbr"
	project.load(src)
	project.save(dest)
	original = open(src, "rb")
	actual = open(dest, "rb")
	assert actual.read() == original.read().replace(b"\r\n", b"\n")
	original.close()
	actual.close()
	os.remove(dest)
