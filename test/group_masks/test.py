#!/usr/bin/env python3
"""Run unit tests.

You might be looking to run test.py from the 'test' directory. In windows::
/GimpFormats/test> py ./test.py

Alternatively, you can do py test.py or if you have pytest, pytest test.py
"""
from __future__ import annotations

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

	def testSingleMaskedGroup(self):
		"""Test a single group with layer mask."""
		self.dut.load(__HERE__ + "single-masked-group.xcf")
		result = self.dut.image
		assert imgcompare.is_equal(
			result,
			__HERE__ + "single-masked-group.tga",
			tolerance=1,
		)

	def testMultipleMaskedGroups(self):
		"""Test multiple layer groups with masks."""
		self.dut.load(__HERE__ + "multiple-masked-groups.xcf")
		result = self.dut.image
		assert imgcompare.is_equal(
			result,
			__HERE__ + "multiple-masked-groups.tga",
			tolerance=1,
		)

	def testMultipleOffsetMaskedGroups(self):
		"""Test multiple offset layer groups with masks."""
		self.dut.load(__HERE__ + "multiple-offset-masked-groups.xcf")
		result = self.dut.image
		assert imgcompare.is_equal(
			result,
			__HERE__ + "multiple-offset-masked-groups.tga",
			tolerance=1,
		)


def testSuite():
	"""
	Combine unit tests into an entire suite
	"""
	varTestSuite = unittest.TestSuite()
	varTestSuite.addTest(Test("testSingleMaskedGroup"))
	varTestSuite.addTest(Test("testMultipleMaskedGroups"))
	varTestSuite.addTest(Test("testMultipleOffsetMaskedGroups"))
	return varTestSuite


if __name__ == "__main__":
	"""
	Run all the test suites in the standard way.
	"""
	unittest.main()
