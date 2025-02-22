"""Drive gimp directly if it exists to do a conversion. Note this is highly
experimental at present, though will likely export more accurately than gimpformats will."""

from __future__ import annotations

import os
import shlex
import subprocess
import sys
from pathlib import Path

from loguru import logger

logger.remove()
logger.add(sys.stdout, format="<level>{level: <8}</level> | {message}", level="INFO")

image_extensions = [
	".jpg",
	".jpeg",
	".png",
	".bmp",
	".tiff",
	".webp",
	".ico",
	".raw",
	".heif",
	".heic",
	".pdf",
	".avif",
	".exr",
]


def _convert_xcf_to_flat_image(xcf_path: str, output_path: str) -> list[str] | None:
	common_gimp_paths = [
		r"C:\Program Files\GIMP 2\bin\gimp-console-2.10.exe",
		r"C:\Program Files (x86)\GIMP 2\bin\gimp-console-2.10.exe",
		"/bin/gimp-console",
		"/usr/bin/gimp-console",
		"/usr/local/bin/gimp-console",
	]

	gimp_path = None
	for path in common_gimp_paths:
		if os.path.exists(path):
			gimp_path = path

	if gimp_path is None:
		logger.error(f"GIMP is not installed or not found at common locations. {common_gimp_paths}")
		return None

	# Prepare the command to run GIMP in batch mode
	return [
		gimp_path,
		"-n",
		"-i",
		"-b",
		f'(begin (define xcf-path "{xcf_path}") '
		f"(define image (car (gimp-file-load RUN-NONINTERACTIVE xcf-path xcf-path))) "
		f"(define layer (car (gimp-image-merge-visible-layers image CLIP-TO-IMAGE))) "
		f'(gimp-file-save RUN-NONINTERACTIVE image layer "{output_path}" "{output_path}") '
		f"(gimp-image-delete image) (gimp-quit 0))",
	]


def convert_xcf_to_flat_image(xcf_path: str, output_path: str, *, run_anyway=False) -> None:
	"""Convert an xcf file given by `xcf_path` to some flat image (such
	as a jpg, png etc) given by `output_path`.

	:param str xcf_path: path to a source xcf file
	:param str output_path: path to an output file (eg a png)
	:param bool run_anyway: force running this, unsafe!
	"""
	# Ensure the input .xcf path exists
	if not Path(xcf_path).is_file():
		logger.error(f"Input file does not exist: {xcf_path}")
		return

	output_path = shlex.quote(output_path)
	_suf = Path(output_path).suffix
	if _suf not in image_extensions:
		logger.error(f"Output file extension `{_suf}` not supported: {image_extensions}")
		return

	# Check if the OS is Windows
	platform_supported = sys.platform in ("win32", "linux")
	command = None
	if platform_supported or (not platform_supported and run_anyway):
		if sys.platform in ("linux",) and _suf in (".avif", "fuck_knows"):
			logger.error(f"{_suf} is not supported in this system")
			return
		command = _convert_xcf_to_flat_image(xcf_path, output_path)

	if not platform_supported and run_anyway:
		logger.warning(
			f"this script may not be supported on `{sys.platform}`, "
			"pass run_anyway=True to override this"
		)
	if command is None:
		return

	try:
		# Run the command and convert the file
		subprocess.run(command, check=True)  # noqa: S603 # Choosing to ignore this for now. Need to investigate how to escape user input here!
		logger.info(f"Conversion successful: {output_path}")
	except subprocess.CalledProcessError as e:
		logger.error(f"Error running GIMP: {e}")
	except Exception as e:  # noqa: BLE001
		logger.error(f"Unexpected error: {e}")
