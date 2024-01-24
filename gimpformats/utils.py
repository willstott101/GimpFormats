from __future__ import annotations

from io import BytesIO


def fileOpen(fileName: BytesIO | str) -> tuple[str, bytes]:
	if isinstance(fileName, str):
		file = open(fileName, "rb")
	else:
		fileName = fileName.name
		file = fileName
	data = file.read()
	file.close()
	return fileName, data


def save(data: bytes, tofileName: BytesIO | str) -> None:
	"""Save this gimp image to a file."""
	file = open(tofileName, "wb") if isinstance(tofileName, str) else tofileName
	file.write(data)
	file.close()
