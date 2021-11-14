"""Feature: https://github.com/FHPythonUtils/GimpFormats/issues/6
"""

from __future__ import annotations

from gimpformats.gimpXcfDocument import GimpDocument

project = GimpDocument("test_files/xcf_mask_test.xcf")
project.image.show()
