from __future__ import annotations

from pathlib import Path

THISDIR = Path(__file__).resolve().parent

from gimpformats.GimpImageLevel import GimpImageLevel

project = GimpImageLevel(None)

# ruff: noqa: SLF001


def parse_bytes(input_file: Path):
	import ast

	with open(input_file) as f:
		byte_string = f.read().strip()

	return ast.literal_eval(byte_string)  # Convert string to real bytes


def test_case_1():
	# 4096 3 1053

	data = parse_bytes(THISDIR / "src/case1.txt")
	expected = parse_bytes(THISDIR / "dest/case1.txt")
	pixels = 4096
	bpp = 3

	result = project._decodeRLE(data, pixels=pixels, bpp=bpp, index=1053)
	assert result == expected
	assert len(result) == pixels * bpp


def test_case_1_encode():
	data = parse_bytes(THISDIR / "dest/case1.txt")
	expected = parse_bytes(THISDIR / "src/case1.txt")

	result = project._encodeRLE(data, bpp=3)
	assert result in expected
