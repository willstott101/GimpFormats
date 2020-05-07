"""List data on groups followed by the direct children of a gimp xcf document
"""

from PIL import Image
from gimpformats.gimpXcfDocument import GimpDocument

project = GimpDocument("base24.xcf")

layers = project.layers
print("## Visible layers.")
for layer in layers:
	print(layer.name, layer.visible)
index = 0
print("## Group info...")
while index < len(layers):
	layerOrGroup = layers[index]
	if layerOrGroup.isGroup:
		index += 1
		while layers[index].itemPath is not None:
			print("Group \"" + layerOrGroup.name + "\" contains Layer \"" + layers[index].name + "\"")
			layers.pop(index)
	else:
		index += 1

print("## Document direct children...")
for layerOrGroup in layers:
	print("\"" + layerOrGroup.name + "\" is a " + ("Group" if layerOrGroup.isGroup else "Layer"))

print("## Saving base24.xcf as base24copy.xcf")
project.save("base24copy.xcf")

print("## Creating new test.xcf using gimp-wilber.png")
wilber = Image.open("gimp-wilber.png")
newProj = GimpDocument()
newProj.newLayer("wilber", wilber)
for layer in newProj.layers:
	print(layer.name)
newProj.saveNew("wilber.xcf")
