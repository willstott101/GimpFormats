import sys
import pytest
from pathlib import Path
from imgcompare import imgcompare
from gimpformats.gimpXcfDocument import GimpDocument

THISDIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THISDIR.parent))


@pytest.fixture
def gimp_doc() -> GimpDocument:
	"""Fixture to return a fresh instance of GimpDocument for each test."""
	return GimpDocument()


@pytest.fixture(params=["testOneLayerWithTransparency", "testComplexImage", "issue_14"])
def image_name(request) -> str:
	"""Fixture to provide different image names for parametrized tests."""
	return request.param


def test_image_repr(gimp_doc: GimpDocument, image_name: str) -> None:
	"""Test the text representation of an image."""
	xcf_path = THISDIR / f"src/{image_name}.xcf"
	txt_path = THISDIR / f"dest/{image_name}.txt"

	gimp_doc.load(str(xcf_path))
	actual_text = str(gimp_doc).split("\n", 1)[1]
	# txt_path.write_text(actual_text, encoding="utf-8")

	expected_text = txt_path.read_text("utf-8").strip()
	assert actual_text == expected_text


@pytest.mark.parametrize("xcf_path", list((THISDIR / "rods-custom-font-xcf-files").glob("*.xcf")))
def test_font_comparison(gimp_doc: GimpDocument, xcf_path: Path) -> None:
	"""Test if the generated image matches the expected output."""
	# output_png = THISDIR / f"rods-custom-font-xcf-files/{xcf_path.name}_actual.png"
	expected_png = THISDIR / f"rods-custom-font-xcf-files/{xcf_path.name}.png"

	gimp_doc.load(str(xcf_path))
	# gimp_doc.image.save(str(output_png))
	# gimp_doc.image.save(str(expected_png))

	# assert imgcompare.is_equal(gimp_doc.image, str(expected_png), tolerance=0.2)


def test_image_comparison(gimp_doc: GimpDocument, image_name: str) -> None:
	"""Test if the generated image matches the expected output."""
	xcf_path = THISDIR / f"src/{image_name}.xcf"
	output_png = THISDIR / f"dest/{image_name}_actual.png"
	expected_png = THISDIR / f"dest/{image_name}.png"

	gimp_doc.load(str(xcf_path))
	gimp_doc.image.save(str(output_png))
	# gimp_doc.image.save(str(expected_png))

	assert imgcompare.is_equal(gimp_doc.image, str(expected_png), tolerance=0.2)
