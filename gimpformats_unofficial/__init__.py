""" gimpformats_unofficial

Forked from https://github.com/TheHeadlessSourceMan/gimpFormats

A pure python implementation of the GIMP xcf image format.

This was created primarily to serve as a file conversion tool for my smartimage
library (coming soon).  The idea is you can "upgrade" from a GIMP document to a
smartimage.

That being said, it should be generally useful to those who want to fiddle with
GIMP files using Python.
"""
from .gimpFormat import *
from .gimpGbrBrush import *
from .gimpGgrGradient import *
from .gimpGihBrushSet import *
from .gimpGpbBrush import *
from .gimpGtpToolPreset import *
from .gimpImageInternals import *
from .gimpIOBase import *
from .gimpParasites import *
from .gimpPatPattern import *
from .gimpVbrBrush import *
from .gimpVectors import *
from .gimpXcfDocument import *
from .gimpGplPalette import *
