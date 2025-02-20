from __future__ import annotations

import os
import sys
from pathlib import Path

THISDIR = Path(__file__).resolve().parent
sys.path.insert(0, os.path.dirname(THISDIR))

from gimpformats.native_convert import convert_xcf_to_flat_image

FILES = THISDIR.parent / "test_files"

image_extensions = [
	".jpg",
	".jpeg",
	".png",
	".gif",
	".bmp",
	".tiff",
	".webp",
	".svg",
	".ico",
	".raw",
	".heif",
	".heic",
	".eps",
	".ai",
	".pdf",
	".avif",
	".exr",
	".dng",
	".pbm",
	".ppm",
	".pgm",
	".wbmp",
	".xpm",
	".flif",
	".ico",
]

convert_xcf_to_flat_image(
	xcf_path=(FILES / "64x64.xcf").as_posix(), output_path="exclude_64x64.png"
)
convert_xcf_to_flat_image(
	xcf_path=(FILES / "base24.xcf").as_posix(), output_path="exclude_base24.png"
)
convert_xcf_to_flat_image(
	xcf_path=(FILES / "base24.xcf").as_posix(), output_path="exclude_file; rm -rf /"
)

for ext in image_extensions:
	convert_xcf_to_flat_image(
		xcf_path=(FILES / "64x64.xcf").as_posix(), output_path=f"exclude_64x64{ext}"
	)
