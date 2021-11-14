#!/usr/bin/env python3
"""
TODO: THIS IS BROKEN

Run unit tests.

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
from gimpformats.GimpGtpToolPreset import GimpGtpToolPreset

__HERE__ = os.path.abspath(__file__).rsplit(os.sep, 1)[0] + os.sep


class Test(unittest.TestCase):
	"""
	Run unit test
	"""

	def setUp(self):
		self.dut = GimpGtpToolPreset()

	def tearDown(self):
		pass

	def testSmudgeRough(self):
		"""test smudge rough."""
		self.dut.load(__HERE__ + "Smudge-Rough.gtp")
		# test round-trip compatibility
		self.dut.save(__HERE__ + "actualOutput_Smudge-Rough.gtp")
		original = open(__HERE__ + "Smudge-Rough.gtp", "rb")
		actual = open(__HERE__ + "actualOutput_Smudge-Rough.gtp", "rb")
		assert actual.read() == original.read().replace(b"\r\n", b"\n")
		original.close()
		actual.close()
		os.remove(__HERE__ + "actualOutput_Smudge-Rough.gtp")


def testSuite():
	"""
	Combine unit tests into an entire suite
	"""
	varTestSuite = unittest.TestSuite()
	varTestSuite.addTest(Test("testSmudgeRough"))
	return varTestSuite


if __name__ == "__main__":
	"""
	Run all the test suites in the standard way.
	"""
	unittest.main()
