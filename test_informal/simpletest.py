"""List data on groups followed by the direct children of a gimp xcf document.
"""

from __future__ import annotations


from PIL import Image
from pathlib import Path
import sys
THISDIR = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, THISDIR)

from gimpformats.gimpXcfDocument import GimpDocument

print("!! use catXCF.py to output the logical structure of an xcf !!")

print("## Test round trip! - Saving base24.xcf as base24copy.xcf")

project = GimpDocument("test_files/base24.xcf")
# project.save("test_files/base24copy.xcf")

print("## Creating new test.xcf using gimp-wilber.png")
wilber = Image.open("test_files/gimp-wilber.png")
newProj = GimpDocument()
print("### test.xcf representation")
print(newProj)
print("\n")
newProj.newLayer("wilber", wilber)
for layer in newProj.layers:
	print(layer.name)
# newProj.saveNew("test_files/wilber.xcf")
