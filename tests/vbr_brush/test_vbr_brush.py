"""python3 -m pytest in project root"""

from __future__ import annotations

from pathlib import Path

import pytest
from imgcompare import imgcompare

THISDIR = str(Path(__file__).resolve().parent)


from gimpformats.GimpVbrBrush import GimpVbrBrush

project = GimpVbrBrush()


def test_DiagonalStar() -> None:
	"""Test diagonal star."""
	project.load(f"{THISDIR}/Diagonal-Star-17.vbr")
	# test round-trip compatibility
	project.save(f"{THISDIR}/actualOutput_Diagonal-Star-17.vbr")
	original = GimpVbrBrush(f"{THISDIR}/Diagonal-Star-17.vbr")
	cmp = GimpVbrBrush(f"{THISDIR}/actualOutput_Diagonal-Star-17.vbr")
	assert cmp == original


@pytest.mark.skip("NotImplementedError")
def test_DiagonalStar_image() -> None:
	"""Test diagonal star."""
	project.load(f"{THISDIR}/Diagonal-Star-17.vbr")
	assert imgcompare.is_equal(
		project.image, f"{THISDIR}/desiredOutput_Diagonal-Star-17.png", tolerance=0.2
	)
