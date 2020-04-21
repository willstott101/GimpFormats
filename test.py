from gimpformats_unofficial.gimpXcfDocument import GimpDocument

project = GimpDocument("base24.xcf")

layers = project.layers
index = 0
while index < len(layers):
	layerOrGroup = layers[index]
	if layerOrGroup.isGroup:
		index += 1
		while layers[index].itemPath is not None:
			print("Group " + layerOrGroup.name + " contains Layer " + layers[index].name)
			layers.pop(index)
	else:
		index += 1

for layerOrGroup in layers:
	print(layerOrGroup.name + " is a " + ("Group" if layerOrGroup.isGroup else "Layer"))
