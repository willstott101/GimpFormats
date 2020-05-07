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
from imgcompare import imgcompare
from gimpformats.GimpPatPattern import GimpPatPattern

__HERE__ = os.path.abspath(__file__).rsplit(os.sep, 1)[0] + os.sep


class Test(unittest.TestCase):
	"""
	Run unit test
	"""
	def setUp(self):
		self.dut = GimpPatPattern()

	def tearDown(self):
		pass

	def test3dgreen(self):
		self.dut.load(__HERE__ + '3dgreen.pat')
		# test image saving (implicit)
		self.dut.save(__HERE__ + 'actualOutput_3dgreen.png')
		# test for image match
		assert imgcompare.is_equal(self.dut.image, __HERE__ + 'desiredOutput_3dgreen.png', tolerance=1)
		os.remove(__HERE__ + 'actualOutput_3dgreen.png')
		# test round-trip compatibility
		self.dut.save(__HERE__ + 'actualOutput_3dgreen.pat')
		original = open(__HERE__ + '3dgreen.pat', 'rb')
		actual = open(__HERE__ + 'actualOutput_3dgreen.pat', 'rb')
		assert actual.read() == original.read()
		original.close()
		actual.close()
		os.remove(__HERE__ + 'actualOutput_3dgreen.pat')

	def testLeopard(self):
		self.dut.load(__HERE__ + 'leopard.pat')
		# test image saving (explicit)
		self.dut.image.save(__HERE__ + 'actualOutput_leopard.png')
		# test for image match
		assert imgcompare.is_equal(self.dut.image, __HERE__ + 'desiredOutput_leopard.png', tolerance=1)
		os.remove(__HERE__ + 'actualOutput_leopard.png')
		# test round-trip compatibility
		self.dut.save(__HERE__ + 'actualOutput_leopard.pat')
		original = open(__HERE__ + 'leopard.pat', 'rb')
		actual = open(__HERE__ + 'actualOutput_leopard.pat', 'rb')
		assert actual.read() == original.read()
		original.close()
		actual.close()
		os.remove(__HERE__ + 'actualOutput_leopard.pat')


def testSuite():
	"""
	Combine unit tests into an entire suite
	"""
	varTestSuite = unittest.TestSuite()
	varTestSuite.addTest(Test("test3dgreen"))
	varTestSuite.addTest(Test("testLeopard"))
	return varTestSuite


if __name__ == '__main__':
	"""
	Run all the test suites in the standard way.
	"""
	unittest.main()
