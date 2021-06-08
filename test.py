"""List data on groups followed by the direct children of a gimp xcf document.
"""

from PIL import Image

from gimpformats.gimpXcfDocument import GimpDocument

print("!! use catXCF.py to output the logical structure of an xcf !!")

print("## Test round trip! - Saving base24.xcf as base24copy.xcf")

project = GimpDocument("test_files/base24.xcf")
project.save("test_files/base24copy.xcf")

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
