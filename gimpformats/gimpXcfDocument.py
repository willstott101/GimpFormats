"""Pure python implementation of the gimp xcf file format.

Currently supports:
	Loading xcf files
	Getting image hierarchy and info
	Getting image for each layer (PIL image)
Currently not supporting:
	Saving
	Programatically alter documents (add layer, etc)
	Rendering a final, compositied image
"""

from __future__ import annotations

import copy
from enum import Enum
from io import BytesIO
from typing import NoReturn

import PIL.ImageGrab
from blendmodes.blend import BlendType, blendLayers
from PIL import Image

from gimpformats import utils
from gimpformats.binaryiotools import IO
from gimpformats.GimpChannel import GimpChannel
from gimpformats.GimpImageHierarchy import GimpImageHierarchy
from gimpformats.GimpIOBase import GimpIOBase, camel_to_pascal_with_spaces
from gimpformats.GimpLayer import GimpLayer
from gimpformats.GimpPrecision import Precision
from gimpformats.utils import repr_indent_lines


class GimpDocument(GimpIOBase):
	"""Pure python implementation of the gimp file format.

	Has a series of attributes including the following:
	self._layers = None
	self._layerPtr = []
	self._channels = []
	self._channelPtr = []
	self.version = None
	self.width = 0
	self.height = 0
	self.baseColorMode = 0
	self.precision = None # Precision object
	self._data = None

	See:
		https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/xcf.txt
	"""

	def __init__(self, fileName: BytesIO | str | None=None) -> None:
		"""Pure python implementation of the gimp file format.

		Has a series of attributes including the following:
		self._layers = None
		self._layerPtr = []
		self._channels = []
		self._channelPtr = []
		self.version = None
		self.width = 0
		self.height = 0
		self.baseColorMode = 0
		self.precision = None # Precision object
		self._data = None

		See:
			https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/xcf.txt
		"""
		GimpIOBase.__init__(self, self)
		self._layers = []
		self._layerPtr = []
		self._channels = []
		self._channelPtr = []
		self.version = 11  # This is the most recent version
		self.width = 0
		self.height = 0
		self.baseColorMode = 0
		self.precision = None  # Precision object
		self._data = None
		self.fileName = None
		if fileName is not None:
			self.load(fileName)

	def load(self, fileName: BytesIO | str) -> None:
		"""Load a gimp xcf and decode the file. See decode for more on this process.

		:param fileName: can be a file name or a file-like object
		"""
		self.fileName, data = utils.fileOpen(fileName)
		self.decode(data)

	def decode(self, data: bytes, index: int = 0) -> int:
		"""Decode a byte buffer.

		Steps:
		Create a new IO buffer
		Check that the file is a valid gimp xcf
		Grab the file version
		Grab other attributes as outlined in the spec
		Get precision data using the class and ioBuf buffer
		List of properties
		Get the layers and add the pointers to them
		Get the channels and add the pointers to them
		Return the offset

		Args:
		----
			data (bytes): data buffer to decode
			index (int, optional): index within the buffer to start at]. Defaults to 0.

		Raises:
		------
			RuntimeError: "Not a valid GIMP file"

		Returns:
		-------
			int: offset

		"""
		# Create a new IO buffer
		ioBuf = IO(data, index)
		# Check that the file is a valid gimp xcf
		if ioBuf.getBytes(9) != b"gimp xcf ":
			msg = "Not a valid GIMP file"
			raise RuntimeError(msg)
		# Grab the file version
		version = ioBuf.cString
		if version == "file":
			self.version = 0
		else:
			self.version = int(version[1:])
		# Grab other attributes as outlined in the spec
		self.width = ioBuf.u32
		self.height = ioBuf.u32
		self.baseColorMode = ioBuf.u32
		# Get precision data using the class and ioBuf buffer
		self.precision = Precision()
		self.precision.decode(self.version, ioBuf)
		# List of properties
		self._propertiesDecode(ioBuf)
		self._layerPtr = []
		self._layers = []
		# Get the layers and add the pointers to them
		while True:
			ptr = self._pointerDecode(ioBuf)
			if ptr == 0:
				break
			self._layerPtr.append(ptr)
			layer = GimpLayer(self)
			layer.decode(ioBuf.data, ptr)
			self._layers.append(layer)
		# Get the channels and add the pointers to them
		self._channelPtr = []
		self._channels = []
		while True:
			ptr = self._pointerDecode(ioBuf)
			if ptr == 0:
				break
			self._channelPtr.append(ptr)
			chnl = GimpChannel(self)
			chnl.decode(ioBuf.data, ptr)
			self._channels.append(chnl)
		# Return the offset
		return ioBuf.index

	def encode(self) -> bytearray:
		"""Encode to bytes.

		Steps:
		Create a new IO buffer
		The file is a valid gimp xcf
		Set the file version
		Set other attributes as outlined in the spec
		Set precision data using the class and ioBuf buffer
		List of properties
		Set the layers and add the pointers to them
		Set the channels and add the pointers to them
		Return the data

		"""
		# Create a new IO buffer
		ioBuf = IO()
		# The file is a valid gimp xcf
		ioBuf.addBytes("gimp xcf ")
		# Set the file version
		ioBuf.addBytes(f"v{self.version:03d}\0")
		# Set other attributes as outlined in the spec
		ioBuf.u32 = self.width
		ioBuf.u32 = self.height
		ioBuf.u32 = self.baseColorMode
		# Set precision data using the class and ioBuf buffer
		if self.precision is None:
			self.precision = Precision()
		self.precision.encode(self.version, ioBuf)
		# List of properties
		ioBuf.addBytes(self._propertiesEncode())
		dataAreaIdx = ioBuf.index + self.pointerSize * (len(self.layers) + len(self._channels))
		dataAreaIO = IO()
		# Set the layers and add the pointers to them
		for layer in self.layers:
			ioBuf.index = dataAreaIdx + dataAreaIO.index
			dataAreaIO.addBytes(layer.encode())
		# Set the channels and add the pointers to them
		for channel in self._channels:
			ioBuf.index = dataAreaIdx + dataAreaIO.index
			dataAreaIO.addBytes(channel.encode())
		ioBuf.addBytes(dataAreaIO)
		# Return the data
		return ioBuf.data

	def forceFullyLoaded(self) -> None:
		"""Make sure everything is fully loaded from the file."""
		for layer in self.layers:
			layer.forceFullyLoaded()
		for channel in self._channels:
			channel.forceFullyLoaded()
		# no longer try to get the data from file
		self._layerPtr = None
		self._channelPtr = None
		self._data = None

	@property
	def layers(self) -> list[GimpLayer]:
		"""Decode the image's layers if necessary.

		TODO: need to do the same thing with self.Channels
		"""
		if len(self._layers) == 0:
			self._layers = []
			for ptr in self._layerPtr:
				layer = GimpLayer(self)
				layer.decode(self._data, ptr)
				self._layers.append(layer)
			# add a reference back to this object so it doesn't go away while array is in use
			self._layers.parent = self
			# override some internal methods so we can do more with them
			self._layers._actualDelitem_ = self._layers.__delitem__
			self._layers.__delitem__ = self.deleteLayer
			self._layers._actualSetitem_ = self._layers.__setitem__
			self._layers.__setitem__ = self.setLayer
		return self._layers

	def getLayer(self, index: int) -> GimpLayer:
		"""Return a given layer."""
		return self.layers[index]

	def setLayer(self, index: int, layer: GimpLayer) -> None:
		"""Assign to a given layer."""
		self.forceFullyLoaded()
		self._layerPtr = None  # no longer try to use the pointers to get data
		self.layers._actualSetitem_(index, layer)

	def newLayer(self, name: str, image: Image.Image, index: int = -1) -> GimpLayer:
		"""Create a new layer based on a PIL image.

		Args:
		----
			name (str): a name for the new layer
			image (Image.Image): pil image
			index (int, optional): where to insert the new layer (default=top). Defaults to -1.

		Returns:
		-------
			GimpLayer: newly created GimpLayer object

		"""
		layer = GimpLayer(self, name, image)
		layer.imageHierarchy = GimpImageHierarchy(self, image=image)
		self.insertLayer(layer, index)
		return layer

	def newLayerFromClipboard(self, name: str = "pasted", index: int = -1) -> GimpLayer | None:
		"""Create a new image from the system clipboard.

		NOTE: requires pillow PIL implementation
		NOTE: only works on OSX and Windows

		Args:
		----
			name (str): a name for the new layer
			index (int, optional): where to insert the new layer (default=top). Defaults to -1.

		Returns:
		-------
			GimpLayer: newly created GimpLayer object

		"""
		image = PIL.ImageGrab.grabclipboard()
		if isinstance(image, Image.Image):
			return self.newLayer(name, image, index)
		return None

	def addLayer(self, layer: GimpLayer) -> None:
		"""Append a layer object to the document.

		:param layer: the new layer to append
		"""
		self.insertLayer(layer, -1)

	def appendLayer(self, layer: GimpLayer) -> None:
		"""Append a layer object to the document.

		:param layer: the new layer to append
		"""
		self.insertLayer(layer, -1)

	def insertLayer(self, layer: GimpLayer, index: int = -1) -> None:
		"""Insert a layer object at a specific position.

		:param layer: the new layer to insert
		:param index: where to insert the new layer (default=top)
		"""
		self._layers.insert(index, layer)

	def deleteLayer(self, index: int) -> None:
		"""Delete a layer."""
		self.__delitem__(index)

	# make this class act like this class is an array of layers
	def __len__(self) -> int:
		"""Make this class act like this class is an array of layers...

		Get the len.
		"""
		return len(self.layers)

	def __getitem__(self, index: int) -> GimpLayer:
		"""Make this class act like this class is an array of layers...

		Get the layer at an index.
		"""
		return self.layers[index]

	def __setitem__(self, index: int, layer: GimpLayer) -> None:
		"""Make this class act like this class is an array of layers...

		Set a layer at an index.
		"""
		self.setLayer(index, layer)

	def __delitem__(self, index: int) -> None:
		"""Make this class act like this class is an array of layers...

		Delete a layer at an index.
		"""
		self.deleteLayer(index)

	def __inc__(self, amt: GimpLayer) -> GimpDocument:
		self.appendLayer(amt)
		return self

	@property
	def image(self) -> Image.Image:
		"""Generates a final, compiled image by processing layers and groups."""

		# Create a deep copy of the layers to avoid modifying the original list
		layers = self.layers[:]

		# Initialize a dummy group container: [Group, [Layer1, Layer2, ...]]
		root_group = [None, []]

		# Process each layer or group
		for layer in layers:
			parent = root_group  # Default to the root group

			# Determine the correct parent list using itemPath hierarchy
			if layer.itemPath is not None:
				for level_index in layer.itemPath[:-1]:
					parent = parent[1][level_index]

			# Create a deep copy of the layer/group to ensure immutability
			layer_copy: GimpLayer = copy.deepcopy(layer)

			# Append layer to its parent group
			if layer.isGroup:
				parent[1].append([layer_copy, []])  # Groups are stored as [Group, [Layers...]]
			else:
				parent[1].append(layer_copy)  # Regular layers are stored as-is

		# Flatten the processed hierarchy into a final image
		return flattenAll(root_group[1], (self.width, self.height))

	def save(self, filename: str | BytesIO | None = None) -> NoReturn:
		"""Save this gimp image to a file."""

		# Save not yet implemented so for now throw
		# an except so we don't corrupt the file
		raise NotImplementedError

		# self.forceFullyLoaded()
		# utils.save(self.encode(), filename or self.fileName)

	def saveNew(self, filename=None) -> NoReturn:
		"""Save a new gimp image to a file."""

		# Save not yet implemented so for now throw
		# an except so we don't corrupt the file
		raise NotImplementedError

		# utils.save(self.encode(), filename or self.fileName)

	def __str__(self) -> str:
		"""Get a textual representation of this object."""
		return self.__repr__()

	def __repr__(self, indent: int = 0) -> str:
		"""Get a textual representation of this object."""
		attrs = [
			"fileName",
			"version",
			"width",
			"height",
			"baseColorMode",
			"precision",
		]

		ret = [
			f"{camel_to_pascal_with_spaces(attr)}: {getattr(self, attr)}"
			for attr in attrs
			if getattr(self, attr) is not None
		]
		ret.append(GimpIOBase.__repr__(self))
		if self._layerPtr:
			ret.append("Layers:")
			for layer in self.layers:
				ret.append(layer.__repr__(indent=indent + 1))
		if self._channelPtr:
			ret.append("Channels:")
			for channel in self._channels:
				ret.append(channel.__repr__(indent=indent + 1))

		return repr_indent_lines(indent, ret)


def blendModeLookup(
	blendmode: int, blendLookup: dict[int, BlendType], default: BlendType = BlendType.NORMAL
):
	"""Get the blendmode from a lookup table."""
	if blendmode not in blendLookup:
		return default
	return blendLookup[blendmode]


class BlendType(Enum):
	NORMAL = 0
	MULTIPLY = 3
	SCREEN = 4
	OVERLAY = 5
	DIFFERENCE = 6
	ADDITIVE = 7
	NEGATION = 8
	DARKEN = 9
	LIGHTEN = 10
	HUE = 11
	SATURATION = 12
	COLOUR = 13
	LUMINOSITY = 14
	DIVIDE = 15
	COLOURDODGE = 16
	COLOURBURN = 17
	HARDLIGHT = 18
	SOFTLIGHT = 19
	GRAINEXTRACT = 20
	GRAINMERGE = 21
	VIVIDLIGHT = 48
	PINLIGHT = 49
	EXCLUSION = 52


blendLookup = {
	0: BlendType.NORMAL,
	3: BlendType.MULTIPLY,
	4: BlendType.SCREEN,
	5: BlendType.OVERLAY,
	6: BlendType.DIFFERENCE,
	7: BlendType.ADDITIVE,
	8: BlendType.NEGATION,
	9: BlendType.DARKEN,
	10: BlendType.LIGHTEN,
	11: BlendType.HUE,
	12: BlendType.SATURATION,
	13: BlendType.COLOUR,
	14: BlendType.LUMINOSITY,
	15: BlendType.DIVIDE,
	16: BlendType.COLOURDODGE,
	17: BlendType.COLOURBURN,
	18: BlendType.HARDLIGHT,
	19: BlendType.SOFTLIGHT,
	20: BlendType.GRAINEXTRACT,
	21: BlendType.GRAINMERGE,
	23: BlendType.OVERLAY,
	24: BlendType.HUE,
	25: BlendType.SATURATION,
	26: BlendType.COLOUR,
	27: BlendType.LUMINOSITY,
	28: BlendType.NORMAL,
	30: BlendType.MULTIPLY,
	31: BlendType.SCREEN,
	32: BlendType.DIFFERENCE,
	33: BlendType.ADDITIVE,
	34: BlendType.NEGATION,
	35: BlendType.DARKEN,
	36: BlendType.LIGHTEN,
	37: BlendType.HUE,
	38: BlendType.SATURATION,
	39: BlendType.COLOUR,
	40: BlendType.LUMINOSITY,
	41: BlendType.DIVIDE,
	42: BlendType.COLOURDODGE,
	43: BlendType.COLOURBURN,
	44: BlendType.HARDLIGHT,
	45: BlendType.SOFTLIGHT,
	46: BlendType.GRAINEXTRACT,
	47: BlendType.GRAINMERGE,
	48: BlendType.VIVIDLIGHT,
	49: BlendType.PINLIGHT,
	52: BlendType.EXCLUSION,
}


def flattenLayerOrGroup(
	layerOrGroup: GimpLayer | list[GimpLayer],
	imageDimensions: tuple[int, int],
	flattenedSoFar: Image.Image | None = None,
	ignoreHidden: bool = True,
) -> Image.Image:
	"""Optimized function to flatten a layer or group with reduced redundant operations."""

	if isinstance(layerOrGroup, list):
		first_layer = layerOrGroup[0]
		if ignoreHidden and not first_layer.visible:
			foregroundComposite = Image.new("RGBA", imageDimensions)
		else:
			foregroundComposite = renderLayerOrGroup(
				flattenAll(layerOrGroup, imageDimensions, ignoreHidden), imageDimensions
			)
			if first_layer.mask is not None:
				foregroundComposite = applyMask(
					foregroundComposite,
					first_layer.mask.image,
					first_layer.xOffset,
					first_layer.yOffset,
					imageDimensions,
				)

		return blendWithFlattened(flattenedSoFar, foregroundComposite, first_layer)

	# Single layer case
	if ignoreHidden and not layerOrGroup.visible:
		return flattenedSoFar if flattenedSoFar else Image.new("RGBA", imageDimensions)

	foregroundComposite = renderLayerOrGroup(
		layerOrGroup.image, imageDimensions, (layerOrGroup.xOffset, layerOrGroup.yOffset)
	)

	if layerOrGroup.mask is not None:
		foregroundComposite = applyMask(
			foregroundComposite,
			layerOrGroup.mask.image,
			layerOrGroup.xOffset,
			layerOrGroup.yOffset,
			imageDimensions,
		)

	return blendWithFlattened(flattenedSoFar, foregroundComposite, layerOrGroup)


def flattenAll(
	layers: list[GimpLayer], imageDimensions: tuple[int, int], ignoreHidden: bool = True
) -> Image.Image:
	"""Optimized flattenAll to avoid excessive recursion."""
	flattened = None
	for layer in reversed(layers):
		flattened = flattenLayerOrGroup(layer, imageDimensions, flattened, ignoreHidden)
	return flattened


def renderLayerOrGroup(
	image: Image.Image, size: tuple[int, int], offsets: tuple[int, int] = (0, 0)
) -> Image.Image:
	"""Optimized function to render a layer or group with reduced conversions."""
	image = image.convert("RGBA")
	imageOffset = Image.new("RGBA", size)
	imageOffset.paste(image, offsets, image)
	return imageOffset


def applyMask(
	image: Image.Image, mask: Image.Image, xOffset: int, yOffset: int, size: tuple[int, int]
) -> Image.Image:
	"""Applies a mask efficiently."""
	masked_image = Image.new("RGBA", size)
	masked_image.paste(image, (xOffset, yOffset), mask)
	return masked_image


def blendWithFlattened(
	flattened: Image.Image | None, foreground: Image.Image, layer: GimpLayer
) -> Image.Image:
	"""Optimized function to blend layers with existing flattened image."""
	if flattened is None:
		return foreground
	return blendLayers(
		flattened, foreground, blendModeLookup(layer.blendMode, blendLookup), layer.opacity
	)


def blendModeLookup(blend_mode, blendLookup):
	"""Looks up the blend mode from the lookup table."""
	return blendLookup.get(blend_mode, BlendType.NORMAL)
