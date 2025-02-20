"""
TODO: THIS IS BROKEN

python3 -m pytest in project root
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

THISDIR = str(Path(__file__).resolve().parent)

from imgcompare import imgcompare

from gimpformats.GimpGihBrushSet import GimpGihBrushSet

project = GimpGihBrushSet()


@pytest.mark.skip("RuntimeError")
@pytest.mark.parametrize(("file_name"), ["Wilber", "feltpen"])
def test_gihbrush(file_name: str) -> None:
	"""test felt pen."""
	project.load(f"{THISDIR}/{file_name}.gih")
	project.image.save(f"{THISDIR}/actualOutput_{file_name}.png")
	assert imgcompare.is_equal(
		project.image, f"{THISDIR}/desiredOutput_{file_name}.png", tolerance=0.2
	)
	os.remove(f"{THISDIR}/actualOutput_{file_name}.png")


@pytest.mark.skip("RuntimeError: Unknown brush version")
@pytest.mark.parametrize(("file_name"), ["Wilber", "feltpen"])
def test_gihbrush_roundtrip(file_name: str) -> None:
	project.load(f"{THISDIR}/{file_name}.gih")
	project.save(f"{THISDIR}/actualOutput_{file_name}.gih")
	original = open(f"{THISDIR}/{file_name}.gih", "rb").read()
	actual = open(f"{THISDIR}/actualOutput_{file_name}.gih", "rb").read()
	assert actual == original
	os.remove(f"{THISDIR}/actualOutput_{file_name}.gih")
