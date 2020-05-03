#!/usr/bin/env python3
"""
TODO: THIS IS BROKEN

Run unit tests

See:
	http://pyunit.sourceforge.net/pyunit.html
"""
import unittest
import os
import sys
from pathlib import Path
PROJECTDIR = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, os.path.dirname(PROJECTDIR))
from imgcompare import imgcompare
from gimpformats import GimpGihBrushSet

__HERE__ = os.path.abspath(__file__).rsplit(os.sep, 1)[0] + os.sep


class Test(unittest.TestCase):
	"""
	Run unit test
	"""
	def setUp(self):
		self.dut = GimpGihBrushSet()

	def tearDown(self):
		pass

	def testWilber(self):
		""" test wilber """
		self.dut.load(__HERE__ + 'Wilber.gih')
		# test image saving (implicit)
		self.dut.save(__HERE__ + 'actualOutput_Wilber.png')
		# test for image match
		assert imgcompare.is_equal(self.dut.image, __HERE__ + 'desiredOutput_Wilber.png', tolerance=1)
		os.remove(__HERE__ + 'actualOutput_Wilber.png')
		# test round-trip compatibility
		self.dut.save(__HERE__ + 'actualOutput_Wilber.gih')
		original = open(__HERE__ + 'Wilber.gih', 'rb').read()
		actual = open(__HERE__ + 'actualOutput_Wilber.gih', 'rb').read()
		assert actual == original
		os.remove(__HERE__ + 'actualOutput_Wilber.gih')

	def testFeltpen(self):
		""" test felt pen """
		self.dut.load(__HERE__ + 'feltpen.gih')
		# test image saving (explicit)
		self.dut.image.save(__HERE__ + 'actualOutput_feltpen.png')
		# test for image match
		assert imgcompare.is_equal(self.dut.image, __HERE__ + 'desiredOutput_feltpen.png', tolerance=1)
		os.remove(__HERE__ + 'actualOutput_feltpen.png')
		# test round-trip compatibility
		self.dut.save(__HERE__ + 'actualOutput_feltpen.gih')
		original = open(__HERE__ + 'feltpen.gih', 'rb').read()
		actual = open(__HERE__ + 'actualOutput_feltpen.gih', 'rb').read()
		assert actual == original
		os.remove(__HERE__ + 'actualOutput_feltpen.gih')


def testSuite():
	"""
	Combine unit tests into an entire suite
	"""
	varTestSuite = unittest.TestSuite()
	varTestSuite.addTest(Test("testWilber"))
	varTestSuite.addTest(Test("testFeltpen"))
	return varTestSuite


if __name__ == '__main__':
	"""
	Run all the test suites in the standard way.
	"""
	unittest.main()
