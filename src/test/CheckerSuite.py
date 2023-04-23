import unittest
from TestUtils import TestChecker
from AST import *
from Visitor import Visitor
from StaticError import *
from abc import ABC

class CheckerSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """
            

main : function void() inherit foo{
                super(1.0, 2.0, 3.0);
                z: integer = foo(1,2,3) + 1;
                x = "abc";
                y = true;
            }
            foo : function auto(inherit x : auto, inherit y : auto, z : auto){
                x = true;
                return "1";
            }
        
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 300))