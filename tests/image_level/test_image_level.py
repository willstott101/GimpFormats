from __future__ import annotations

from pathlib import Path

THISDIR = Path(__file__).resolve().parent

from gimpformats.GimpImageHierarchy import GimpImageHierarchy
from gimpformats.GimpImageLevel import GimpImageLevel
from gimpformats.GimpIOBase import CompressionMode
from gimpformats.gimpXcfDocument import GimpDocument

doc = GimpDocument()
doc.version = 11
doc.compression = CompressionMode.RLE
gih = GimpImageHierarchy(doc)
gih.bpp = 3
project = GimpImageLevel(gih)

# ruff: noqa: SLF001


def parse_bytes(input_file: Path):
	import ast

	with open(input_file) as f:
		byte_string = f.read().strip()

	return ast.literal_eval(byte_string)  # Convert string to real bytes


def test_case_1():
	# 4096 3 1053

	data = parse_bytes(THISDIR / "src/test.xcf.txt")
	expected = parse_bytes(THISDIR / "dest/test.xcf.decoded.txt")
	pixels = 4096
	bpp = 3

	result = project._decodeRLE(data, pixels=pixels, bpp=bpp, index=1053)
	assert result == expected
	assert len(result) == pixels * bpp


def test_case_1_encode():
	data = parse_bytes(THISDIR / "dest/test.xcf.decoded.txt")
	expected = parse_bytes(THISDIR / "src/test.xcf.txt")

	result = project._encodeRLE(data, bpp=3)
	assert result in expected


def test_decode_encode():
	data = parse_bytes(THISDIR / "src/test.xcf.txt")
	expected = parse_bytes(THISDIR / "dest/test.xcf.decoded.txt")

	result = project.decode(data, index=1029)
	assert result == 1053
	subimage = project._tiles[0]

	cmp = data[1029:]

	result = project.encode(offset=1029)
	assert len(result) == len(cmp)
	assert result == cmp

	# subimage.show()
	# assert len(result) == pixels * bpp
