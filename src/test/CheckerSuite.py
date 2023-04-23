import unittest
from TestUtils import TestChecker
from AST import *
from Visitor import Visitor
from StaticError import *
from abc import ABC

class CheckerSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """
            
x: function void() {}
    main: function void() inherit x {
        super(); //?
    }
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 300))