"""Feature: https://github.com/FHPythonUtils/GimpFormats/issues/6."""

from __future__ import annotations

import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, THISDIR)

from gimpformats.gimpXcfDocument import GimpDocument

project = GimpDocument("test_files/xcf_mask_test.xcf")
project.image.show()
