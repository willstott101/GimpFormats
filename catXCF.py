"""Output Gimp Layers and Groups."""

from __future__ import annotations

from gimpformats.gimpXcfDocument import GimpDocument, GimpGroup

# ruff: noqa: T201


def cat_group(group: GimpGroup, i: int = 0) -> None:
	"""Output layers in group."""
	for idx, child in enumerate(group.children):
		if isinstance(child, GimpGroup):
			print("\t" * i, idx, child.layer_options)
			cat_group(child, i + 1)
		else:
			print("\t" * i, idx, child)


def catXCF(file: str) -> None:
	"""Open an .xcf file into a layered image."""
	project = GimpDocument(file)
	root_goup = project.walkTree()
	print()
	print("=" * 60)
	print("=", project.fileName)
	print("=" * 60)
	cat_group(root_goup)


catXCF("test_files/test.xcf")
catXCF("test_files/base24.xcf")
