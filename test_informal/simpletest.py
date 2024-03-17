"""List data on groups followed by the direct children of a gimp xcf document."""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

THISDIR = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, THISDIR)

from gimpformats.gimpXcfDocument import GimpDocument

project = GimpDocument("test_files/base24.xcf")
# project.save("test_files/base24copy.xcf")

wilber = Image.open("test_files/gimp-wilber.png")
newProj = GimpDocument()
newProj.newLayer("wilber", wilber)
for _layer in newProj.layers:
	pass
# newProj.saveNew("test_files/wilber.xcf")
