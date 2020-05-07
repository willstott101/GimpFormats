#!/usr/bin/env python3
"""
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
from gimpformats.GimpGplPalette import GimpGplPalette

__HERE__ = os.path.abspath(__file__).rsplit(os.sep, 1)[0] + os.sep


class Test(unittest.TestCase):
	"""
	Run unit test
	"""
	def setUp(self):
		self.dut = GimpGplPalette()

	def tearDown(self):
		pass

	def testPlasma(self):
		""" test plasma """
		self.dut.load(__HERE__ + 'Plasma.gpl')
		# test round-trip compatibility
		self.dut.save(__HERE__ + 'actualOutput_Plasma.gpl')
		original = open(__HERE__ + 'Plasma.gpl', 'rb')
		actual = open(__HERE__ + 'actualOutput_Plasma.gpl', 'rb')
		assert actual.read() == original.read()
		original.close()
		actual.close()
		os.remove(__HERE__ + 'actualOutput_Plasma.gpl')


def testSuite():
	"""
	Combine unit tests into an entire suite
	"""
	varTestSuite = unittest.TestSuite()
	varTestSuite.addTest(Test("testPlasma"))
	return varTestSuite


if __name__ == '__main__':
	"""
	Run all the test suites in the standard way.
	"""
	unittest.main()
