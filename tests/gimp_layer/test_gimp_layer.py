from __future__ import annotations

from pathlib import Path


from gimpformats.gimpXcfDocument import GimpDocument
from gimpformats.GimpLayer import GimpLayer

THISDIR = Path(__file__).resolve().parent


doc = GimpDocument()
doc.version = 11
project = GimpLayer(doc)

# ruff: noqa: SLF001


def parse_bytes(input_file: Path):
	import ast

	with open(input_file) as f:
		byte_string = f.read().strip()

	return ast.literal_eval(byte_string)  # Convert string to real bytes


def test_case_1():
	data = parse_bytes(THISDIR / "case1.txt")
	idx = project.decode(data, index=426)
	assert project.width == 410
	assert project.height == 410
	assert project.colorMode == 1
	assert project.name == "bg #1"
	assert idx == 680


# def test_case_1_encode():
# 	expected = parse_bytes(THISDIR / "case1.txt")

# 	result = project.encode()
# 	assert result in expected
