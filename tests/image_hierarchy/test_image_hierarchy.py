from __future__ import annotations

from pathlib import Path


from gimpformats.gimpXcfDocument import GimpDocument
from gimpformats.GimpImageHierarchy import GimpImageHierarchy
from gimpformats.GimpIOBase import  CompressionMode


THISDIR = Path(__file__).resolve().parent

doc = GimpDocument()
doc.version = 11
doc.compression =  CompressionMode.RLE

project = GimpImageHierarchy(doc)

# ruff: noqa: SLF001


def parse_bytes(input_file: Path) -> bytes:
	import ast

	with open(input_file) as f:
		byte_string = f.read().strip()

	return ast.literal_eval(byte_string)  # Convert string to real bytes


def test_case_1():
	data = parse_bytes(THISDIR / "test.xcf.txt")
	idx = project.decode(data, index=1001)
	assert project.width == 64
	assert project.height == 64
	assert project.bpp == 3
	assert idx == 1029


def test_case_1_encode():

	data = parse_bytes(THISDIR / "test.xcf.txt")

	idx = project.decode(data, index=1001)

	print("done")
	expected = parse_bytes(THISDIR / "test.xcf.txt")[1001:]

	# print(expected)

	result = project.encode(offset=1001)

	# print(result)
	assert len(result) == len(expected)
	assert result == expected
