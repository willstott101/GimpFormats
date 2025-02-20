"""
TODO: THIS IS BROKEN

python3 -m pytest in project root
"""

from __future__ import annotations

import os
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)

from gimpformats.GimpGtpToolPreset import GimpGtpToolPreset

dut = GimpGtpToolPreset()


def test_smudgeRough() -> None:
	"""test smudge rough."""
	dut.load(f"{THISDIR}/Smudge-Rough.gtp")
	# test round-trip compatibility
	dut.save(f"{THISDIR}/actualOutput_Smudge-Rough.gtp")
	original = open(f"{THISDIR}/Smudge-Rough.gtp", "rb")
	actual = open(f"{THISDIR}/actualOutput_Smudge-Rough.gtp", "rb")
	assert actual.read() == original.read().replace(b"\r\n", b"\n")
	original.close()
	actual.close()
	os.remove(f"{THISDIR}/actualOutput_Smudge-Rough.gtp")
