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
from gimpformats.GimpGbrBrush import GimpGbrBrush
from imgcompare import imgcompare

__HERE__ = os.path.abspath(__file__).rsplit(os.sep, 1)[0] + os.sep


class Test(unittest.TestCase):
	"""
	Run unit test
	"""

	def setUp(self):
		self.dut = GimpGbrBrush()

	def tearDown(self):
		pass

	def testPepper(self):
		"""test pepper"""
		self.dut.load(__HERE__ + "pepper.gbr")
		# test image saving (implicit)
		self.dut.save(__HERE__ + "actualOutput_pepper.png")
		# test for image match
		assert imgcompare.is_equal(
			self.dut.image, __HERE__ + "desiredOutput_pepper.png", tolerance=1
		)
		os.remove(__HERE__ + "actualOutput_pepper.png")
		# test round-trip compatibility
		self.dut.save(__HERE__ + "actualOutput_pepper.gbr")
		original = open(__HERE__ + "pepper.gbr", "rb")
		actual = open(__HERE__ + "actualOutput_pepper.gbr", "rb")
		assert actual.read() == original.read().replace(b"\r\n", b"\n")
		original.close()
		actual.close()
		os.remove(__HERE__ + "actualOutput_pepper.gbr")

	def testDunes(self):
		"""test dunes"""
		self.dut.load(__HERE__ + "dunes.gbr")
		# test image saving (explicit)
		self.dut.image.save(__HERE__ + "actualOutput_dunes.png")
		# test for image match
		assert imgcompare.is_equal(
			self.dut.image, __HERE__ + "desiredOutput_dunes.png", tolerance=1
		)
		os.remove(__HERE__ + "actualOutput_dunes.png")
		# test round-trip compatibility
		self.dut.save(__HERE__ + "actualOutput_dunes.gbr")
		original = open(__HERE__ + "dunes.gbr", "rb")
		actual = open(__HERE__ + "actualOutput_dunes.gbr", "rb")
		assert actual.read() == original.read().replace(b"\r\n", b"\n")
		original.close()
		actual.close()
		os.remove(__HERE__ + "actualOutput_dunes.gbr")


def testSuite():
	"""
	Combine unit tests into an entire suite
	"""
	varTestSuite = unittest.TestSuite()
	varTestSuite.addTest(Test("testDunes"))
	varTestSuite.addTest(Test("testPepper"))
	return varTestSuite


if __name__ == "__main__":
	"""
	Run all the test suites in the standard way.
	"""
	unittest.main()
