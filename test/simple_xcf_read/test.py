#!/usr/bin/env python3
"""Run unit tests.

You might be looking to run test.py from the 'test' directory. In windows::
/GimpFormats/test> py ./test.py

Alternatively, you can do py test.py or if you have pytest, pytest test.py
"""
import os
import sys
import unittest
from pathlib import Path

PROJECTDIR = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, os.path.dirname(PROJECTDIR))
from imgcompare import imgcompare

from gimpformats.gimpXcfDocument import GimpDocument

__HERE__ = os.path.abspath(__file__).rsplit(os.sep, 1)[0] + os.sep


class Test(unittest.TestCase):
	"""
	Run unit test
	"""

	def setUp(self):
		self.dut = GimpDocument()

	def tearDown(self):
		pass

	def testImage(self):
		"""test an image."""
		self.dut.load(__HERE__ + "one_layer_with_transparency.xcf")
		# self.dut.save(__HERE__ + 'actualOutput.png')
		self.dut.image.save(__HERE__ + "actualOutput.png")
		assert imgcompare.is_equal(self.dut.image, __HERE__ + "desiredOutput.png", tolerance=1)

	def testComplexImage(self):
		"""test an image."""
		self.dut.load(__HERE__ + "base24.xcf")
		self.dut.image.save(__HERE__ + "base24.png")
		assert imgcompare.is_equal(self.dut.image, __HERE__ + "expected.png", tolerance=1)


def testSuite():
	"""
	Combine unit tests into an entire suite
	"""
	varTestSuite = unittest.TestSuite()
	varTestSuite.addTest(Test("testImage"))
	varTestSuite.addTest(Test("testComplexImage"))
	return varTestSuite


if __name__ == "__main__":
	"""
	Run all the test suites in the standard way.
	"""
	unittest.main()
