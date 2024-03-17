"""python3 -m pytest in project root"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
from imgcompare import imgcompare

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

from gimpformats.GimpVbrBrush import GimpVbrBrush

dut = GimpVbrBrush()


@pytest.mark.skip("NotImplementedError")
def test_DiagonalStar() -> None:
	"""Test diagonal star."""
	dut.load(f"{THISDIR}/Diagonal-Star-17.vbr")
	assert imgcompare.is_equal(
		dut.image, f"{THISDIR}/desiredOutput_Diagonal-Star-17.png", tolerance=0.2
	)
	# test round-trip compatibility
	dut.save(f"{THISDIR}/actualOutput_Diagonal-Star-17.vbr")
	original = GimpVbrBrush(f"{THISDIR}/Diagonal-Star-17.vbr")
	assert dut == original
