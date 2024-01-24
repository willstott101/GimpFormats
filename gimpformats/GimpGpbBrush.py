"""Pure python implementation of the OLD gimp gpb brush format.
"""
from __future__ import annotations

from io import BytesIO

from . import utils
from .binaryiotools import IO
from .GimpGbrBrush import GimpGbrBrush
from .GimpPatPattern import GimpPatPattern


class GimpGpbBrush:
	"""Pure python implementation of the OLD gimp gpb brush format.

	See:
		https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/vbr.txt
	"""

	def __init__(self, fileName: BytesIO | str) -> None:
		"""Pure python implementation of the OLD gimp gpb brush format.

		Args:
		----
			fileName (BytesIO): filename/ filepointer
		"""
		self.brush = GimpGbrBrush()
		self.pattern = GimpPatPattern()
		if isinstance(fileName, str):
			self.fileName = fileName
		else:
			self.fileName = fileName.name

	def load(self, fileName: BytesIO | str) -> None:
		"""Load a gimp file.

		:param fileName: can be a file name or a file-like object
		"""
		self.fileName, data = utils.fileOpen(fileName)
		self.decode(data)

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
		return self.brush.decode(data, index)
		# index = self.pattern.decode(data, index)

	def encode(self) -> bytes:
		"""Encode this object to bytes."""
		ioBuf = IO()
		ioBuf.addBytes(self.brush.encode())
		ioBuf.addBytes(self.pattern.encode())
		return ioBuf.data

	def save(self, tofileName: str|BytesIO|None=None) -> None:
		"""Save this gimp image to a file."""
		utils.save(self.encode(), tofileName)

	def __repr__(self, indent: str = "") -> str:
		"""Get a textual representation of this object."""
		ret = []
		if self.fileName is not None:
			ret.append(f"fileName: {self.fileName}")
		ret.append(self.brush.__repr__(indent + "\t"))
		ret.append(self.pattern.__repr__())
		return (f"\n{indent}").join(ret)
