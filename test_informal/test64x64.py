from __future__ import annotations

import os
import sys
from pathlib import Path

THISDIR = Path(__file__).resolve().parent
sys.path.insert(0, os.path.dirname(THISDIR))

from gimpformats.GimpLayer import GimpLayer
from gimpformats.gimpXcfDocument import GimpDocument

FILES = THISDIR.parent / "test_files"


project = GimpDocument((FILES / "64x64.xcf").as_posix())
# project.cat()
# This doc contains a single img rep
# project.layers[0].image.show()

newProject = GimpDocument()
newProject.addLayer(GimpLayer(newProject, "BG", project.layers[0].image))
newProject.saveNew((FILES / "64x64_copy.xcf").as_posix())
