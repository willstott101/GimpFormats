"""Gets packed pixels from a gimp image.

NOTE: This was originally designed to be a hierarchy, like
	an image pyramid, through in practice they only use the
	top level of the pyramid (64x64) and ignore the rest.
"""

from __future__ import annotations

from PIL import Image

from gimpformats.GimpImageLevel import GimpImageLevel
from gimpformats.GimpIOBase import IO, GimpIOBase


class GimpImageHierarchy(GimpIOBase):
	"""
	Represents packed pixels from a GIMP image hierarchy.

	Note that the XCF docs say this was originally designed as a hierarchy,
	but currently only the top level (lptr) is used

	uint32      width   Width of the pixel array
	uint32      height  Height of the pixel array
	uint32      bpp     Number of bytes per pixel; this depends on the
					color mode and image precision (fields 'base_type'
					and 'precision' of the image header). For
					instance, some combination values:
					3: RGB color without alpha in 8-bit precision
					4: RGB color with alpha in 8-bit precision
					6: RGB color without alpha in 16-bit precision
					16: RGB color with alpha in 32-bit precision
					1: Grayscale without alpha in 8-bit precision
					4: Grayscale with alpha in 16-bit precision
					1: Indexed without alpha (always 8-bit)
					2: Indexed with alpha (always 8-bit)
					And so on.

	pointer     lptr    Pointer to the "level" structure
	,--------   ------  Repeat zero or more times
	| pointer   dlevel  Pointer to an unused level structure (dummy level)
	`--
	pointer     0       Zero marks the end of the list of level pointers.
	.
	"""

	def __init__(self, parent, image: Image.Image | None = None) -> None:
		super().__init__(parent)
		self.width: int = 0
		self.height: int = 0
		self.bpp: int = 0  # Number of bytearray per pixel
		self._levelPtrs = []
		self._levels = None
		self._data = None
		if image is not None:
			self.image = image

	def decode(self, data: bytearray, index: int = 0) -> int:
		"""
		Decode packed pixels from a byte buffer.
		"""

		if not data:
			msg = "No data provided for decoding."
			raise RuntimeError(msg)

		ioBuf = IO(data, index)
		self.width = ioBuf.u32
		self.height = ioBuf.u32
		self.bpp = ioBuf.u32

		if not (1 <= self.bpp <= 4):
			msg = f"Unexpected bytearray-per-pixel value: {self.bpp}. Possible file corruption."
			raise RuntimeError(msg)

		while True:
			ptr = self._pointerDecode(ioBuf)
			if ptr == 0:
				break
			self._levelPtrs.append(ptr)

		# Here we enforce that only the first pointer is actually used
		if self._levelPtrs:
			self._levelPtrs = [self._levelPtrs[0]]
		self._data = data
		return ioBuf.index

	def encode(self, offset: int = 0) -> bytearray:
		"""
		Encode packed pixels data into a byte buffer.
		"""
		ioBuf = IO()
		ioBuf.u32 = self.width
		ioBuf.u32 = self.height
		ioBuf.u32 = self.bpp
		pointerSizeb = self.pointerSize // 8

		dataIndex = offset + ioBuf.index + pointerSizeb + pointerSizeb

		topLevel = self.levels[0]
		data = topLevel.encode(offset=dataIndex)
		ioBuf.addbytearray(self._pointerEncode(dataIndex))
		ioBuf.addbytearray(self._pointerEncode(0))
		ioBuf.addbytearray(data)

		return ioBuf.data

	@property
	def levels(self) -> list[GimpImageLevel]:
		"""Get the levels within this hierarchy.

		Presently hierarchy is not really used by gimp,
		so this returns an array of one item
		"""
		if self._levels is None:
			for ptr in self._levelPtrs or []:
				level = GimpImageLevel(self)
				level.decode(self._data, ptr)
				self._levels = [level]
		return self._levels or []

	@property
	def image(self) -> Image.Image | None:
		"""Get a final, compiled image."""
		return self.levels[0].image if self.levels else None

	@image.setter
	def image(self, image: Image.Image) -> None:
		"""Set the image."""
		self.width, self.height = image.size
		if image.mode not in ["L", "LA", "RGB", "RGBA"]:
			msg = "Unsupported PIL image type."
			raise NotImplementedError(msg)
		self.bpp = len(image.mode)
		self._levelPtrs = []

	def __str__(self) -> str:
		"""Get a textual representation of this object."""
		return self.__repr__()

	def __repr__(self) -> str:
		"""Get a textual representation of this object."""
		return f"<GimpImageHierarchy size={self.width}x{self.height}, bpp={self.bpp}>"
