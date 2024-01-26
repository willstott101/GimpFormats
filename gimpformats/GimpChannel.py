"""Represents a single channel or mask in a gimp image.
"""
from __future__ import annotations

from PIL import Image

from .binaryiotools import IO
from .GimpImageHierarchy import GimpImageHierarchy
from .GimpIOBase import GimpIOBase
from .utils import repr_indent_lines


class GimpChannel(GimpIOBase):
	"""Represents a single channel or mask in a gimp image."""

	def __init__(
		self, parent: GimpIOBase, name: str = "", image: Image.Image | None = None
	) -> None:
		"""GimpChannel.

		Args:
		----
			parent ([type]): some parent node/ object
			name (str, optional): name of the channel. Defaults to "".
			image (Image.Image, optional): image to set. Defaults to None.
		"""
		GimpIOBase.__init__(self, parent)
		self.width = 0
		self.height = 0
		self.name = name
		self._imageHierarchy = None
		self._imageHierarchyPtr = None
		if image is not None:  # this is last because image can reset values
			self.image = image
		self._data = None

	def decode(self, data: bytes, index: int = 0) -> int:
		"""Decode a byte buffer.

		Args:
		----
			data (bytes): data to decode
			index (int, optional): index to start from. Defaults to 0.

		Returns:
		-------
			int: pointer
		"""
		ioBuf = IO(data, index)
		# print 'Decoding channel at',index
		self.width = ioBuf.u32
		self.height = ioBuf.u32
		self.name = ioBuf.sz754
		self._propertiesDecode(ioBuf)
		self._imageHierarchyPtr = self._pointerDecode(ioBuf)
		self._data = ioBuf.data
		return ioBuf.index

	def encode(self) -> bytearray:
		"""Encode this object to a byte buffer."""
		ioBuf = IO()
		ioBuf.u32 = self.width
		ioBuf.u32 = self.height
		ioBuf.sz754 = self.name
		ioBuf.addBytes(self._propertiesEncode())
		imgH = self._imageHierarchyPtr
		if imgH is None:
			imgH = 0
		ioBuf.addBytes(self._pointerEncode(imgH))
		return ioBuf.data

	@property
	def image(self) -> Image.Image | None:
		"""Get a final, compiled image."""
		return self.imageHierarchy.image

	@image.setter
	def image(self, image: Image.Image) -> None:
		"""Get a final, compiled image."""
		self.width = image.width
		self.height = image.height
		if not self.name and isinstance(image, str):
			# try to use a fileName as the name
			self.name = image.rsplit("\\", 1)[-1].rsplit("/", 1)[-1]
		self._imageHierarchy = GimpImageHierarchy(self, image)

	def forceFullyLoaded(self) -> None:
		"""Make sure everything is fully loaded from the file."""
		_ = self.image  # make sure the image is loaded so we can delete the hierarchy nonsense
		self._imageHierarchyPtr = None
		self._data = None

	@property
	def imageHierarchy(self) -> GimpImageHierarchy:
		"""Get the image hierarchy.

		This is mainly used for decoding the image, so
		not much use to you.
		"""
		if self._data and self._imageHierarchyPtr:
			if self._imageHierarchy is None:
				self._imageHierarchy = GimpImageHierarchy(self)
				self._imageHierarchy.decode(self._data, self._imageHierarchyPtr)
			return self._imageHierarchy
		msg = "self._data or self._imageHierarchyPtr is None"
		raise RuntimeError(msg)

	def __str__(self) -> str:
		"""Get a textual representation of this object."""
		return self.__repr__()

	def __repr__(self, indent: int = 0) -> str:
		"""Get a textual representation of this object."""
		ret = []
		ret.append(f"Name: {self.name}")
		ret.append(f"Size: {self.width} x {self.height}")
		ret.append(GimpIOBase.__repr__(self, indent))
		return repr_indent_lines(indent, ret)
