"""
TODO: THIS IS BROKEN

python3 -m pytest in project root
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from gimpformats.GimpGtpToolPreset import GimpGtpToolPreset

THISDIR = str(Path(__file__).resolve().parent)

project = GimpGtpToolPreset()


@pytest.mark.parametrize("base_name", ["Smudge-Rough", "4_3-Landscape"])
def test_roundtrip(base_name: str) -> None:
	"""test smudge rough."""
	project.load(f"{THISDIR}/{base_name}.gtp")
	# test round-trip compatibility
	project.save(f"{THISDIR}/actualOutput_{base_name}.gtp")
	original = open(f"{THISDIR}/{base_name}.gtp", "rb")
	actual = open(f"{THISDIR}/actualOutput_{base_name}.gtp", "rb")
	assert actual.read() == original.read().replace(b"\r\n", b"\n")
	original.close()
	actual.close()
	os.remove(f"{THISDIR}/actualOutput_{base_name}.gtp")
