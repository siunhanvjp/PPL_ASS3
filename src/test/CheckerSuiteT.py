import unittest
from TestUtils import TestChecker
from AST import *
from Visitor import Visitor
from StaticError import *
from abc import ABC

class CheckerSuite(unittest.TestCase):


    # def test_401_test_vardecl_1(self):
    #         input = """
    #             foo: integer = 5;
    #             main: function void(){
    #                 a: integer = foo();
    #             }
    #         """
    #         expect = "Undeclared Function: foo"
    #         self.assertTrue(TestChecker.test(input, expect, 401))

    def test_oke(self):
        input = """main: function void(){}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test_402_test_vardecl_1(self):
        input = """x: auto = !true&&!false||!(!true)&&"true";"""
        expect = "Type mismatch in expression: FuncCall(foo, [])"
        self.assertTrue(TestChecker.test(input, expect, 522))

    def test_403_test_vardecl_1(self):
        input = """
            foo: integer = 5;
            main: function void(){
                a: integer = foo();
                a = foo;
            }
            foo: function auto() {}
        """
        expect = "Type mismatch in expression: FuncCall(foo, [])"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_404_test_vardecl_1(self):
        input = """
            foo: function auto() {}
            main: function void(){
                a: integer = foo();
                a = foo;
            }
            foo: integer = 5;
        """
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_405_test_vardecl_1(self):
        input = """
            foo: function auto() {}
            main: function void(){
                a: integer = foo;
            }
        """
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_jump2(self):
        input = """
            main: function void() {
                a: auto = f1(1,2,3) + 2;
                
            }
            f1: function auto(x: float, y: float, z: float) {
                return x + y + z;
            }
        """
        expect = """Type mismatch in statement: ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))"""
        self.assertTrue(TestChecker.test(input, expect, 102))


    def test_dumb3(self):
        input = """
            main: function auto(x: float, y: float, z: float) {
                return 1;
                return "abc";
                return true;
                a: string = true;
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, StringType, BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 108))

    def test_dumb4(self):
        input = """
            main: function void(b: auto, c: auto) {
                x: auto = x + 10;
                y: string;
                y = b * c;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(y), BinExpr(*, Id(b), Id(c)))"""
        self.assertTrue(TestChecker.test(input, expect, 109))

    def test_dumb5(self):
        input = """
            f1: function auto() {
                if (true) {
                    return 1;
                    return "abc";
                }
                else return 2;
                
                return true;
                return "abc";
            }
        """
        expect = """Type mismatch in statement: ReturnStmt(BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 110))

    def test_superDumb(self):
        input = """
            f1: function auto(b: float, c: auto) {
                do {
                    x: integer = 1;
                } while (x + 1);
            }
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 111))

    def test_superDumb2(self):
        input = """
            f1: function auto(b: float, c: auto) {
                do {
                    x: integer = "abc";
                } while (x + 1 == 2);
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(x, IntegerType, StringLit(abc))"""
        self.assertTrue(TestChecker.test(input, expect, 112))

    def test_superDumb3(self):
        input = """
            f1: function auto(b: float, c: auto) {
                do {
                    x: integer = "abc";
                } while (x + 1);
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(x, IntegerType, StringLit(abc))"""
        self.assertTrue(TestChecker.test(input, expect, 113))

# ====== Tests from BkeL forum ======

    def test_501(self):
        input = '''goo: function void(a: auto, a: auto) inherit foo{}'''
        expect = 'Undeclared Function: foo'
        self.assertTrue(TestChecker.test(input, expect, 501))

    def test_502(self):
        input = '''foo: function integer(){}
            a: auto = foo;'''
        expect = 'Undeclared Identifier: foo'
        self.assertTrue(TestChecker.test(input, expect, 502))

    def test_503(self):
        input = '''foo: function integer() {}
            a: auto = {foo, 1, 3};'''
        expect = 'Undeclared Identifier: foo'
        self.assertTrue(TestChecker.test(input, expect, 503))

    def test_504(self):
        input = '''foo: function integer(){}
            main: function void(){
                foo = 3;
            }'''
        expect = 'Undeclared Identifier: foo'
        self.assertTrue(TestChecker.test(input, expect, 504))

    def test_505(self):
        input = '''foo: function integer(){}
            main: function void(){
                m: integer;
                m = foo + 1;
            }'''
        expect = 'Undeclared Identifier: foo'
        self.assertTrue(TestChecker.test(input, expect, 505))

    def test_506(self):
        input = '''foo: function integer(){}
            main: function void(){
                foo: integer = 3;
                a: integer;
                a = foo(); // line 5
            }'''
        expect = 'Type mismatch in expression: FuncCall(foo, [])'
        self.assertTrue(TestChecker.test(input, expect, 506))

    # def test_507(self):
    #     input = '''inc : function void (out n : integer, a: float) inherit foo{super();}
    #                 foo : function auto (inherit n: float, n: integer){}'''
    #     expect = 'Invalid Parameter: n'
    #     self.assertTrue(TestChecker.test(input, expect, 507))

    def test_508(self):
        input = '''x: function void (a: auto) {}
            main: function void() {
                x();
            }'''
        expect = 'Type mismatch in statement: CallStmt(x, )'
        self.assertTrue(TestChecker.test(input, expect, 508))

    # def test_509(self):
    #     input = '''x: function void (a: auto) {}
    #         main: function void() {
    #             x(1,2);
    #         }'''
    #     expect = 'Type mismatch in expression: IntegerLit(2)'
    #     self.assertTrue(TestChecker.test(input, expect, 509))

    def test_510(self):
        input = '''x : auto={4,5,6};
            y:  auto=x[1,2];'''
        expect = 'Type mismatch in expression: ArrayCell(x, [IntegerLit(1), IntegerLit(2)])'
        self.assertTrue(TestChecker.test(input, expect, 510))
        
    def test_511(self):
        input = '''a: array[2,2] of integer;
            b: array[2] of integer = a[0];'''
        expect = 'No entry point'
        self.assertTrue(TestChecker.test(input, expect, 511))
        
    def test_512(self):
        input = '''func: function integer() {
                a: integer = 12;
                return 3;
                a: float = 14;
            }'''
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input, expect, 512))
        
    def test_513(self):
        input = '''func: function integer(a: integer) {
                if (a < 13) return 16;
                else a = a + 1;
                a: float = 12;
                return 10;
            }'''
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input, expect, 513))
        
    def test_514(self):
        input = '''func: function integer() {
                a: integer = 1;
                while(a < 10) {
                    a = a + 1;
                    continue;
                    a: float = b;
                }
            }'''
        expect = 'Undeclared Identifier: b'
        self.assertTrue(TestChecker.test(input, expect, 514))
        
    def test_515(self):
        input = '''foo: function integer(inherit x: integer) inherit bar { super(2); }
            bar: function integer(inherit y: integer) inherit foo2 { super("Hi"); }
            foo2: function integer(inherit z: float) {}'''
        expect = 'Type mismatch in expression: StringLit(Hi)'
        self.assertTrue(TestChecker.test(input, expect, 515))

    # def test_516(self):
    #     input = '''a: float = foo(1, 2) + 1.5;
    #         foo: function auto(a: integer, b: integer) {
    #             return a + b; 
    #         }'''
    #     expect = 'No entry point'
    #     self.assertTrue(TestChecker.test(input, expect, 516))

    def test_517(self):
        input = '''a: float = 2.3; //1
            b: auto; //2
            foo: function void(a: integer, b: float) {} //3
            bar: function void() inherit foo {} //4
            a: function void() {} //5'''
        expect = 'Invalid Variable: b'
        self.assertTrue(TestChecker.test(input, expect, 517))

    def test_518(self):
        input = '''x, y: integer = 1, foo(1, 2, 3);  // 1
            x, y: string; // 2
            foo: function integer (x: integer, y: integer, x: integer) {} // 3'''
        expect = 'Redeclared Variable: x'
        self.assertTrue(TestChecker.test(input, expect, 518))

    def test_519(self):
        input = '''x: integer = foo();
            foo: function integer (){}'''
        expect = 'No entry point'
        self.assertTrue(TestChecker.test(input, expect, 519))

    def test_520(self):
        input = '''foo: function void (){
                x = 5;
                x: integer;
            }'''
        expect = 'Undeclared Identifier: x'
        self.assertTrue(TestChecker.test(input, expect, 520))

    def test_521(self):
        input = '''foo: function void(){
                while(true) { x = 5; }
                x: integer;
            }'''
        expect = 'Undeclared Identifier: x'
        self.assertTrue(TestChecker.test(input, expect, 521))