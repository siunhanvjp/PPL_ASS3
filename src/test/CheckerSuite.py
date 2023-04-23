import unittest
from TestUtils import TestChecker
from AST import *

"""

"""
class CheckerSuite(unittest.TestCase):

#     def test_redeclared_variable1(self):
#         """test_redeclared_variable1"""
#         input = """
# main: function void(){
#     a: integer  = 3;
#     a: integer;
# }"""
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input,expect,400))

#     def test_redeclared_variable2(self):
#         """test_redeclared_variable2"""
#         input = """
#         main: function void(){
#             a,b : integer = 1,2;
#             a: float = 3.5;
#         }"""
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input,expect,401))

#     def test_redeclared_variable3(self):
#         """test_redeclared_variable3"""
#         input = """
# main: function void(){
#     // do something
#     a, b: integer = 3,2;
# }
# main: auto = 3;
# """
#         expect = "Redeclared Variable: main"
#         self.assertTrue(TestChecker.test(input,expect,402))

#     def test_redeclared_variable4(self):
#         """test_redeclared_variable4"""
#         input = """
# main: function integer(){
#     a: integer = 3;
#     b: integer = a + 3;
#     return a+b;
# }
# foo: string = "hello world";
# main: float = 3.5;"""

#         expect = "Redeclared Variable: main"
#         self.assertTrue(TestChecker.test(input,expect,403))

#     def test_redeclared_variable5(self):
#         """test_redeclared_variable5"""
#         input = """
# foo: function integer(a:float){}
# A: integer;  
# goo : function float(a: float){}

# A: function string(b: string, c: string){
#     // error
#     x : float = 0.5;
#     y : integer = foo(x);
# }
# """
#         expect = "Redeclared Function: A"
#         self.assertTrue(TestChecker.test(input,expect,404))

#     def test_redeclared_variable6(self):
#         """test_redeclared_variable6"""
#         input = """
# main: function void()
# {

#         a,b:integer;
#         b = 1;
#         a:string;  // error
#         b = 0;
# }
# """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input,expect,405))

#     def test_redeclared_variable7(self):
#         """test_redeclared_variable7"""
#         input = """
#             main : function void() {
#                 doNothing();
#             }
#             a: integer = 3;

#             main: function integer()    // error
#             {
#                 a, Main:integer;
#                 b, MAIN:float;
#                 Main: integer;  
#                 return 1;
#             }
#             """
#         expect = "Undeclared Function: doNothing"
#         self.assertTrue(TestChecker.test(input,expect,406))

#     def test_redeclared_variable8(self):
#         """test_redeclared_variable8"""
#         input = """
#         main: function void(){
#             for (i = 0, i < 10, i + 1){
#                 doNothing();
#                 count = 1;
#                 count = count + 1;
#             }
#         }
#         arrFloat: array[3] of float;
#         arrFloat: float;  // error
# """
#         expect = "Undeclared Identifier: i"
#         self.assertTrue(TestChecker.test(input,expect,407))

#     def test_redeclared_function1(self):
#         """test_redeclared_function1"""
#         input = """
#         main: function void(){
#             arrInt: array[3] of integer;
#             while(true){
#                 count = arrInt[0] / 3;
#                 printInteger(count);
#             }
#         }

#         doNothing: function void(){
#             printString("Do nothing bleble!");
#         } 

#         main: function float(a: integer, b: integer)      // error
#         {
#             return 1.1;
#         }
        
# """
#         expect = "Undeclared Identifier: count"
#         self.assertTrue(TestChecker.test(input,expect,408))

#     def test_redeclared_procedure1(self):
#         """test_redeclared_function1"""
#         input = """

# main: function void(){

#         a:  integer;
#         a:  string;
# }
# main: function integer(){
#     return 13e-2;
# }
# """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input,expect,409))

#     def test_undeclared_identifier1(self):
#         """test_undeclared_identifier1"""
#         input = """
# main: function void(){
#     printInteger(1);
#     a =  1998;
#     b = 1998;  // error
# }

# """
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input,expect,410))

#     def test_undeclared_identifier2(self):
#         """test_undeclared_identifier2"""
#         input = """
# asd:integer;
# foo: function integer(x: integer){
#     return x;
# }    

# asd: integer;
# main: function void(x: integer){
#     y : float = 3.5;
#     x = foo();
#     y = x + foo - 1;
# }

# """
#         expect = "Redeclared Variable: asd"
#         self.assertTrue(TestChecker.test(input,expect,411))

#     def test_undeclared_function1(self):
#         """test_undeclared_function1"""
#         input = """
#         main: function void(){
#             x: integer;
#             x = foo(1, 2.2, x , y);
#         }
# """
#         expect = "Undeclared Function: foo"
#         self.assertTrue(TestChecker.test(input,expect,412))

#     def test_undeclared_function2(self):
#         """test_undeclared_function2"""
#         input = """
# boolFuncc: function boolean(x: integer){
#     if ( x > 3){return true;}
#     else {return false;}
# };

# main: function void(){
#     if boolFunc(){
#         printString("Hello world")
#     }
#     else {
#         printString("Oivkl")
#     }
# }
# """
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input,expect,413))

#     def test_undeclared_procedure(self):
#         """test_undeclared_procedure"""
#         input = """
# main: function void() {
#     y: integer = 3;
#     y = y / 3;
#     x = x + y;
# }
# """
#         expect = "Undeclared Identifier: x"
#         self.assertTrue(TestChecker.test(input,expect,414))

#     def test_if_condition_must_be_boolean(self):
#         """test_if_condition_must_be_boolean"""
#         input = """
#         main: function void() {
#             x: float = 3.3;
#             if (false) {
#                 if (x) {
#                     printString("Parser m sai roi hehe");
#                 }
#             }
#         }
#         """
#         expect = "Type mismatch in statement: IfStmt(Id(x), BlockStmt([CallStmt(printString, StringLit(Parser m sai roi hehe))]))"
#         self.assertTrue(TestChecker.test(input,expect,415))

#     def test_id_in_for_must_be_integer(self):
#         """test_id_in_for_must_be_integer"""
#         input = """
#         main: function void() {
#             x: float;
#             y: integer;
#             for (y = 0, y < 100, y + 1){
#                 for (x = 1, x < 10, x + 1){
#                     printString("Chay duoc dong nay thi loi roi");
#                 }
#             }
#         }
#         """
#         expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(x), IntegerLit(1)), BinExpr(<, Id(x), IntegerLit(10)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([CallStmt(printString, StringLit(Chay duoc dong nay thi loi roi))]))"
#         self.assertTrue(TestChecker.test(input,expect,416))

#     def test_expr1_in_for_must_be_integer(self):
#         """test_expr1_in_for_must_be_integer"""
#         input = """
#         main : function void ()  {
#             x: integer = 5;
#             for (x = 0, x < 10, x + 1){
#                 for (x = 0.1, x < 10, x+1){
#                     printString("Chay duoc dong nay thi loi roi cu");
#                 }
#             }
#         }
#         """
        

#         expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(x), FloatLit(0.1)), BinExpr(<, Id(x), IntegerLit(10)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([CallStmt(printString, StringLit(Chay duoc dong nay thi loi roi cu))]))"
#         self.assertTrue(TestChecker.test(input,expect,417))

#     def test_expr2_in_for_must_be_integer(self):
#         """test_expr2_in_for_must_be_integer"""
#         input = """
#         main: function integer() {
#             x: integer = 0;
#             for (x = 1, x < 10, x + 1){
#                 for(x = x + 1, x < 10.5, x + 1){
#                     printString("Cai nay phai ra loi la do float");
#                 }
#             }
#         }
#         """
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input,expect,418))

#     def test_id_in_for_must_be_local(self):
#         """test_id_in_for_must_be_local"""
#         input = """
#         x: integer;
#         main: function void() {
#             y: integer;
#             z: float;
#             for (y = 0, y < 10, y + 1){
#                 for (x = 0, x < 10, x + 1){
#                     for (y = z, y < x, y + 1){
#                         printString("Chay duoc den day thi loi roi ");
#                     }
#                 }
#             }
#         }
#         """
#         expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(y), Id(z)), BinExpr(<, Id(y), Id(x)), BinExpr(+, Id(y), IntegerLit(1)), BlockStmt([CallStmt(printString, StringLit(Chay duoc den day thi loi roi ))]))"
#         self.assertTrue(TestChecker.test(input,expect,419))

#     def test_condition_in_while_must_be_boolean(self):
#         """test_condition_in_while_must_be_boolean"""
#         input = """
#         main: function void() {
#             while (true) {
#                 printString("hehe");
#                 break;
#             }
#             while (1) {
#                 printString("Khong biet chay duoc khong");
#             }
#         }
#         """
#         expect = "Type mismatch in statement: WhileStmt(IntegerLit(1), BlockStmt([CallStmt(printString, StringLit(Khong biet chay duoc khong))]))"
#         self.assertTrue(TestChecker.test(input,expect,420))

#     def test_return_proc_must_no_expr(self):
#         """test_return_proc_must_no_expr"""
#         input = """
#         func1: function void(){
#             doNothing();
#         }
#         main: function void() {
#             func1();
#             return 0; // error
#         }
#         """
#         expect = "Undeclared Function: doNothing"
#         self.assertTrue(TestChecker.test(input,expect,421))

#     def test_return_func_must_expr_with_proper_type1(self):
#         """test_return_func_must_expr_with_proper_type1"""
#         input = """
#         main: function void(){
#             ret: integer = 1;
#             ret = foo();
#             ret = foo1();
#         }

#         foo1: function integer() { 
#             a : integer = 3;
#             for(i = 0, i < 10, i + 1){
#                 a = a + i;
#             }
#             return a;
#         }

#         foo: function float(){
#             return 1;
#         }
#         """
#         expect = "Undeclared Identifier: i"
#         self.assertTrue(TestChecker.test(input,expect,422))

#     def test_return_func_must_expr_with_proper_type2(self):
#         """test_return_func_must_expr_with_proper_type2"""
#         input = """
#         main: function void() {
#             ret: float;
#             b : boolean;
#             ret = foo();
#             b = foo1();
#         }

#         foo: function float(){
#             return 3 / 5;
#         }

#         foo1: function boolean(x: integer){
#             return x;
#         }
#         """
#         expect = "Type mismatch in expression: FuncCall(foo1, [])"
#         self.assertTrue(TestChecker.test(input,expect,423))

#     def test_assign_stmt_lhs_must_not_string_type(self):
#         """test_assign_stmt_lhs_must_not_string_type"""
#         input = """
#         main: function void() {
#             s: string;
#             a: integer;

#             a = 1;
#             s = "random string";

#         }
#         """
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,424))

#     def test_func_45(self):
#         input = """
#         sum: function integer(arr: array[10, 10] of integer) inherit previous_sum
#         {
#             x, y: integer;
#             ans: integer = 0;
#             for (i = 0, i < 10, i + 1)
#             {
#                 for (j = 0, j < 10, j + 1)
#                 {
#                     ans = ans + arr[i, j];
#                 }
#             }
#             return ans;
#         }
#         main: function void()
#         {
#             A: array[10, 10] of integer;
#             printInteger(sum(A));
#         }
#         """
#         expect = "Undeclared Function: previous_sum"
#         self.assertTrue(TestChecker.test(input,expect,425))
#     def test_assign_stmt_type_lhs_and_rhs_must_be_compa(self):
#         """test_assign_stmt_type_lhs_and_rhs_must_be_compa"""
#         input = """
#         main: function void(){
#             a: integer;
#             b : float;
#             a = b;
#             c = a;      // Can float be assigned integer?
#             a = c;
#         }
#         """
#         expect = "Undeclared Identifier: c"
#         self.assertTrue(TestChecker.test(input,expect,426))

#     def test_assign_stmt_type_lhs_and_rhs_must_be_compa2(self):
#         """test_assign_stmt_type_lhs_and_rhs_must_be_compa2"""
#         input = """
#         main: function void()
#         {
#             a, b: integer;
#             c: float;
#             str: string;
#             a = b;
#             c = a;
#             str = b;
#         }
#         """
#         expect = "Type mismatch in statement: AssignStmt(Id(str), Id(b))"
#         self.assertTrue(TestChecker.test(input,expect,427))

#     def test_call_stmt_id_must_be_proc(self):
#         """test_call_stmt_id_must_be_proc"""
#         input = """
#         foo: function integer(a: integer)
#         {
#             return a + 3;
#         }

#         proc: function void()
#         {
#             a: integer;
#         }
        
#         main: function void(){
#             proc();
#             foo1();
#         }
#         """
#         expect = "Undeclared Function: foo1"
#         self.assertTrue(TestChecker.test(input,expect,428))

#     def test_call_stmt_param_len_must_be_the_same(self):
#         """test_call_stmt_param_len_must_be_the_same"""
#         input = """
#         proc: function void (a: integer, b: integer)
#         {
#             printInteger(a + b);
#         }

#         main: function void(){
#             proc(1,0);
#             proc(1);
#         }
#         """
#         expect = "Type mismatch in statement: CallStmt(proc, IntegerLit(1))"
#         self.assertTrue(TestChecker.test(input,expect,429))

#     def test_call_stmt_param_list_must_be_type_comp(self):
#         """test_call_stmt_param_list_must_be_type_comp"""
#         input = """
#         proc: function void(a: float, b: float)
#         {
#             printFloat(a + b);
#         }

#         main: function void() {
#             proc(1.2, 3.0);
#             proc(1.1, "hello man");
#         } 
#         """
#         expect = "Undeclared Function: printFloat"
#         self.assertTrue(TestChecker.test(input,expect,430))

#     def test_expr1_arr_must_be_array_type(self):
#         """test_expr1_arr_must_be_array_type"""
#         input = """
#         main: function void()
#         {
#             a: integer = 0;
#             arr: array[4] of integer;
#             arr[0] = a;
#             a[0] = 1;
#         } 
#         """
#         expect = "Type mismatch in expression: ArrayCell(a, [IntegerLit(0)])"
#         self.assertTrue(TestChecker.test(input,expect,431))

#     def test_expr2_arr_must_be_int_type(self):
#         """test_expr2_arr_must_be_int_type"""
#         input = """
#         main: function void()
#         {
#             a: array[4] of float;
#             a[0] = 1.1;
#             a[1/2] = 1.2;
#         }
#         """
#         expect = "Type mismatch in expression: ArrayCell(a, [BinExpr(/, IntegerLit(1), IntegerLit(2))])"
#         self.assertTrue(TestChecker.test(input,expect,432))

#     def test_type_binary_expr1(self):
#         """test_type_operand_expr1"""
#         input = """
#         run: function void(inherit out p: float, out i: float, out d: float) inherit func{
#             p = 43 * i + d / 328;
#             i = 483 * -0.232 + 32;
#             d = 423 % p * i;
#         }
#         """
#         expect = "Undeclared Function: func"
#         self.assertTrue(TestChecker.test(input,expect,433))

#     def test_type_binary_expr2(self):
#         """test_type_operand_expr2"""
#         input =  """// This is the line comment
#             degreeOfFreedom: auto = 1024;
#             batteryLevel: integer = 100;
#             main: function void() {
#                 prinf("Degree of freedom is");
#                 prinf(degreeOfFreedom);
#                 prinf("\\n");

#                 p: float = 0.328;
#                 i: integer = 0.0;
#                 d: auto = 1.3;

#                 while ((checkCompleted()) && (batteryLevel > 10))
#                     run(p, i, d);
#             }
#             run: function void(inherit out p: float, out i: float, out d: float) inherit func{
#                 p = 43 * i + d / 328;
#                 i = 483 * -0.232 + 32;
#                 d = 423 % p * i;
#             }"""
#         expect = "Undeclared Function: prinf"
#         self.assertTrue(TestChecker.test(input,expect,434))

#     def test_type_binary_expr3(self):
#         """test_type_operand_expr3"""
#         input = """
#         main: function void()
#         {
#             b: integer;
#             c: float;

#             b = b % c;
#         }
#         """
#         expect = "Type mismatch in expression: BinExpr(%, Id(b), Id(c))"
#         self.assertTrue(TestChecker.test(input,expect,435))

#     def test_type_binary_expr4(self):
#         """test_type_operand_expr4"""
#         input = """
#         foo: function void(s: string){
#             printString(s);
#         }

#         main: function void()
#         {
#             foo("ss");
#             foo("s" * 2);
#         }
#         """
#         expect = "Type mismatch in expression: BinExpr(*, StringLit(s), IntegerLit(2))"
#         self.assertTrue(TestChecker.test(input,expect,436))

#     def test_type_unary_expr1(self):
#         """test_type_unary_expr1"""
#         input = """
#         main: function void()
#         {
#             s: string;
#             a: integer;
#             printString(s);
#             printString(a);
#         }
#         """
#         expect = "Type mismatch in statement: CallStmt(printString, Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,437))

#     def test_type_unary_expr2(self):
#         """test_type_unary_expr2"""
#         input = """
#         main: function void()
#         {
#             b: boolean;
#             a: integer;

#             a = -a;
#             b = b;
#             b = -b;
#         }
#         """
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,438))

#     def test_type_unary_expr3(self):
#         """test_type_unary_expr3"""
#         input = """
#         main: function void()
#         {
#             b: boolean;
#             a: integer;

#             b = (!b);
#             a = (!a);
#         }
#         """
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input,expect,439))


#     def test_call_expr_id_must_be_func(self):
#         """test_call_expr_id_must_be_func"""
#         input = """
#         foo: function integer(){
#             return 1;
#         }

#         main: function void(){
#             a: integer = foo();
#             a = foo1();
#         }
#         """
#         expect = "Undeclared Function: foo1"
#         self.assertTrue(TestChecker.test(input,expect,440))

#     def test_call_expr_param_len_must_be_the_same(self):
#         """test_call_expr_param_len_must_be_the_same"""
#         input = """
#         foo: function float()
#         {
#             a: float = 5.5;
#             return a + 1;
#         }

#         main: function void()
#         {
#             a: float;
#             a = foo();
#             a = foo(1,2,3);
#         }
#         """
#         expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])"
#         self.assertTrue(TestChecker.test(input,expect,441))

#     def test_call_expr_param_list_must_be_type_comp(self):
#         """test_call_expr_param_list_must_be_type_comp"""
#         input = """
#         foo: function boolean(a:integer, b:float, c:string)
#         {
#             return (a*b - a/b) <= ((b / a+1) * 3);
#         }
#         main: function void(){
#             a = foo(1,2,"hello");
#             a = foo(1,2,3);
#         }
#         """
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input,expect,442))

#     def test_break_not_in_loop1(self):
#         """test_break_not_in_loop1"""
#         input = """
#         foo: function  void()
#         {
#             a: integer;
#             while(true){
#                 break;
#             }
#             for ( a= 0 , a < 5, a + 1)
#             {
#                 printString("hello world");
#                 break;
#             }
#         }

#         main: function integer()
#         {
#             foo();
#             break;
#             return 1;
#         }
#         """
#         expect = "Must in loop: BreakStmt()"
#         self.assertTrue(TestChecker.test(input,expect,443))

#     def test_break_not_in_loop2(self):
#         """test_break_not_in_loop2"""
#         input = """
#         foo: function void()
#         {
#             a:integer;
#             a = 1 - 1e-1;
#             while (true){
#                 printString("hello world");
#             }    
#             break;
#         }
                
#         main: function void()
#         {
#             foo();
#             if (0.6 > 5/7 ){
#                 break;
#             }
#         }
#         """
#         expect = "Must in loop: BreakStmt()"
#         self.assertTrue(TestChecker.test(input,expect,444))

#     def test_break_not_in_loop3(self):
#         """test_break_not_in_loop3"""
#         input = """
#         foo: function void()
#         {
#             a: integer;
#             while(true){
#                 a: boolean;
#                 break;
#             }

#             for ( a = 0, a < 10, a + 2){
#                 break;
#             }
#         }

#         main: function void()
#         {
#             foo();
#             break;
#         }
#         """
#         expect = "Must in loop: BreakStmt()"
#         self.assertTrue(TestChecker.test(input,expect,445))

#     def test_break_not_in_loop4(self):
#         """test_break_not_in_loop4"""
#         input = """
#         foo: function void()
#         {
#             a : integer = 3;
#             while(true)
#             {
#                 if ( a * 7 - 42 > 1){
#                     break;
#                 }
#                 else{
#                     a = a * 2;
#                 }
#             }
#         }

#         main: function void()
#         {
#             a: integer = 0;
#             for (a = 0, a < 10, a + 1)
#             {
#                 if (a % 3 == 0){
#                     break;
#                 }
#             }
#             break;
#         }
#         """
#         expect = "Must in loop: BreakStmt()"
#         self.assertTrue(TestChecker.test(input,expect,446))

# #     ############################ 61 - 80 #######################################
#     def test_break_not_in_loop5(self):
#         """test_break_not_in_loop5"""
#         input = """
#         main: function void()
#         {
#             if(true)
#             {
#                 while(readInteger() == 1.988){
#                     printString("hello man");
#                     break;
#                 }
#             }
#             else
#             {
#                 a: integer;
#                 for(a = 0, a < 10, a + 1)
#                 {
#                     a = readInteger();
#                     a = a + 2;
#                 }
#                 break;
#             }
#         }
#         """
#         expect = "Type mismatch in expression: BinExpr(==, FuncCall(readInteger, []), FloatLit(1.988))"
#         self.assertTrue(TestChecker.test(input,expect,447))

#     def test_continue_not_in_loop1(self):
#         """test_continue_not_in_loop1"""
#         input = """
#         foo: function void()
#         {
#             a: integer = 0;
#             while(true){
#                 a = a + 1;
#                 if(a < 10){
#                     break;
#                 }
#                 continue;
#             }

#             for (a = 0, a < 10, a + 1){
#                 break;
#             }
#         }

#         main: function void()
#         {
#             foo();
#             continue;
#         }
#         """
#         expect = "Must in loop: ContinueStmt()"
#         self.assertTrue(TestChecker.test(input,expect,448))

#     def test_continue_not_in_loop2(self):
#         """test_continue_not_in_loop2"""
#         input = """
#         main: function void()
#         {
#             foo();
#             continue;
#         }
#         foo: function integer(){
#             return 1;
#         }
#         """
#         expect = "Must in loop: ContinueStmt()"
#         self.assertTrue(TestChecker.test(input,expect,449))

#     def test_continue_not_in_loop3(self):
#         """test_continue_not_in_loop3"""
#         input = """
#         foo: function void()
#         {
#             a: integer = 3;
#             while(true)
#             {
#                 if (a > 3){
#                     continue;
#                 }
#                 else{
#                     break;
#                 }
#             }
#         }

#         main: function void()
#         {
#             a,b: integer  = 3, 4;
#             foo();
#             continue;               // Error
#         }
#         """
#         expect = "Must in loop: ContinueStmt()"
#         self.assertTrue(TestChecker.test(input,expect,450))

#     def test_continue_not_in_loop4(self):
#         """test_continue_not_in_loop4"""
#         input = """
#         foo: function void()
#         {   
#             a: integer;
#             while(true)
#             {
#                 if( 6* 7 -42 < 3){
#                     continue;
#                 }
#                 else{
#                     break;
#                 }
#             }
#             for(a = 0, a < 3, a + 1)
#             {
#                 if (a % 2 == 0)
#                 {
#                     continue;
#                 }
#             }
#         }

#         main: function integer(a: integer)
#         {
#             foo();
#             if (a > 3){
#                 continue;           // error
#             }
#         }
#         """
#         expect = "Must in loop: ContinueStmt()"
#         self.assertTrue(TestChecker.test(input,expect,451))

#     def test_continue_not_in_loop5(self):
#         """test_continue_not_in_loop5"""
#         input = """
#         main: function void()
#         {
#             if(2 > 0)
#             {
#                 while(true)
#                 {
#                     continue;
#                 }
#             }
#             else
#             {
#                 a: integer = 0;
#                 {
#                     {
#                         for (a = 3, a < 10, a + 1)
#                         {
#                             printInteger(a);
#                         }
#                     }
#                 }
#                 continue;           // Error
#             }
#         }
#         """
#         expect = "Must in loop: ContinueStmt()"
#         self.assertTrue(TestChecker.test(input,expect,452))

#     def test_continue_not_in_loop6(self):
#         """test_continue_not_in_loop6"""
#         input = """
#         main2: function integer()
#         {
#             while(true)
#             {
#                 if( a == 6.9)
#                 {
#                     a, b: float;
#                     C: array[100] of integer;
#                     d: integer;
#                     {
#                         a = b / 3;
#                         b = -b;
#                         for(i = C[d], i > 0, i - 1)
#                         {
#                             break;
#                         }
#                     }
#                 }
#                 continue;
#             }
#             return 1;
#         }

#         main1: function float()
#         {
#             while(true)
#             {
#                 if( a == 6.9)
#                 {
#                     a, b: float;
#                     C: array[100] of integer;
#                     d: integer;
#                     {
#                         a = b / 3;
#                         b = -b;
#                         for(i = C[d], i > 0, i - 1)
#                         {
#                             break;
#                         }
#                     }
#                 }
#                 break;
#             }
#             return 1123_123.1;
            
#         }

#         main: function void()
#         {
#             a: integer = main2();
#             b : float = main1();
#             continue;
#         }
#         """
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input,expect,453))

#     def test_no_entry_point1(self):
#         """test_no_entry_point1"""
#         input = """
#         a : boolean = true;
#         """
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input,expect,454))

#     def test_no_entry_point2(self):
#         """test_no_entry_point2"""
#         input = """
#         a: boolean = true;

#         foo: function boolean(a: integer)
#         {
#             return foo(a + 1);
#         }

#         foo2: function boolean(b: integer)
#         {
#             return b + 1;
#         }
#         """
#         expect = "Type mismatch in statement: ReturnStmt(BinExpr(+, Id(b), IntegerLit(1)))"
#         self.assertTrue(TestChecker.test(input,expect,455))

#     def test_no_entry_point3(self):
#         """test_no_entry_point3"""
#         input = """
#         a: boolean = true;

#         main: function boolean(a: integer)
#         {
#             return main3(a);
#         }

#         main3: function boolean(a: integer)
#         {
#             if ( a > 3)
#             {
#                 return true;
#             }
#             return false;
#         }
#         """
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input,expect,456))

#     def test_no_entry_point4(self):
#         """test_no_entry_point4"""
#         input = """
#         a: boolean = true;
#         main: function integer()
#         {
#             return main_next(a);
#         }

#         main_next: function boolean(a: integer)
#         {
#             if (a > 3)
#             {
#                 return true;
#             }
#             else
#             {
#                 return false;
#             }
#         }
#         """
#         expect = "Type mismatch in expression: FuncCall(main_next, [Id(a)])"
#         self.assertTrue(TestChecker.test(input,expect,457))


#     def test_no_entry_point6(self):
#         """test_no_entry_point6"""
#         input = """
#         main: boolean;
#         """
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input,expect,458))

#     def test_no_entry_point7(self):
#         """test_no_entry_point7"""
#         input = """
#         main : integer = 3;
#         """
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input,expect,459))

#     def test_401_test_vardecl_1(self):
#         input = """
#             foo: integer = 5;
#             main: function void(){
#                 a: integer = foo();
#             }
#         """
#         expect = "Type mismatch in expression: FuncCall(foo, [])"
#         self.assertTrue(TestChecker.test(input, expect, 460))

#     def test_all_1(self):
#         input = """
#             foo: function auto() {}
#             main: function void(){
#                 foo: integer;
#                 a: auto = foo;
#                 b: auto = foo();
#             }
#         """
#         expect = "Type mismatch in expression: FuncCall(foo, [])"
#         self.assertTrue(TestChecker.test(input, expect, 461))

#     def test_all_2(self):
#         input = """
#             foo: integer = 5;
#             main: function void(){
#                 a: integer = foo();
#                 a = foo;
#             }
#             foo: function auto() {}
#         """
#         expect = "Type mismatch in expression: FuncCall(foo, [])"
#         self.assertTrue(TestChecker.test(input, expect, 463))

#     def test_test_vardecl_1(self):
#         input = """
#             goo: function auto() {}
#             main: function void(){
#                 a: integer = goo();
#                 a = foo;
#             }
#             goo: integer = 5;
#         """
#         expect = "Undeclared Identifier: foo"
#         self.assertTrue(TestChecker.test(input, expect, 464))

#     def test_all3(self):
#         input = """
#             foo: function auto() {}
#             main: function void(){
#                 a: integer = foo;
#             }
#         """
#         expect = "Undeclared Identifier: foo"
#         self.assertTrue(TestChecker.test(input, expect, 465))

#     def test_all_4(self):
#         input = """
#             main: function void() {
#                 a: auto = {1, 2};
#                 a[goo(1,2,3)] = 2;
#                 x: string = true;
#             }
#             goo: function auto(x: float, y: float, z: float) {
#                 return x + y + z;
#             }
#         """
#         expect = "Type mismatch in expression: ArrayCell(a, [FuncCall(goo, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])])"
#         self.assertTrue(TestChecker.test(input, expect, 466))

#     def test_all_5(self):
#         input = """
#             main: function void() {
#                 a: auto = foo(1,2,3) + 2;
#                 x: string = true;
#             }
#             foo: function auto(x: float, y: float, z: float) {
#                 return x + y + z;
#             }
#         """
#         expect = "Type mismatch in Variable Declaration: VarDecl(x, StringType, BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 467))

#     def test_all_6(self):
#         input = """
#             main: function void() {
#                 a: auto = {goo(1,2,3), 2};
#                 x: string = true;
#             }
#             goo: function auto(x: float, y: float, z: float) {
#                 return x + y + z;
#             }
#         """
#         expect = "Type mismatch in Variable Declaration: VarDecl(x, StringType, BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 468))

#     def test_all_7(self):
#         input = """
#             main: function void() {
#                 a: integer;
#                 a = foo(1,2,3);
#                 x: string = true;
#             }
#             foo: function auto(x: float, y: float, z: float) {
#                 return x + y + z;
#             }
#         """
#         expect = "Type mismatch in Variable Declaration: VarDecl(x, StringType, BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 469))

#     def test_all_8(self):
#         input = """
#             main: function void() {
#                 a: boolean = !doo(1,2,3);
#                 x: string = true;
#             }
#             doo: function auto(x: float, y: float, z: float) {
#                 return x + y + z;
#             }
#         """
#         expect = expect = "Type mismatch in Variable Declaration: VarDecl(a, BooleanType, UnExpr(<class 'str'>, FuncCall(doo, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])))"
#         self.assertTrue(TestChecker.test(input, expect, 470))

    def test_all_9(self):
        input = """
            no_main: function void() {
                x: auto = x + x;
                x = 12;
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(x), IntegerLit(12))"
        self.assertTrue(TestChecker.test(input, expect, 471))

#     def test_all_10(self):
#         input = """
#             main: function void(b: auto, c: auto) {
#                 a: string = b + c;
#             }
#         """
#         expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(+, Id(b), Id(c)))"
#         self.assertTrue(TestChecker.test(input, expect, 472))

#     def test_all_11(self):
#         input = """
#             main: function auto(x: float, y: float, z: float) {
#                 return 1;
#                 return "abc";
#                 return true;
#                 a: string = true;
#             }
#         """
#         expect = """Type mismatch in Variable Declaration: VarDecl(a, StringType, BooleanLit(True))"""
#         self.assertTrue(TestChecker.test(input, expect, 473))

#     def test_all_12(self):
#         input = """
#             main: function void(b: auto, c: auto) {
#                 x: auto = x + 10;
#                 y: string;
#                 y = b * c;
#             }
#         """
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 474))

#     def test_all_13(self):
#         input = """
#             goo: function auto() {
#                 if (true) {
#                     return 1;
#                     return "abc";
#                 }
#                 else return 2;
                
#                 return true;
#                 return "abc";
#             }
#         """
#         expect = "Type mismatch in statement: ReturnStmt(StringLit(abc))"
#         self.assertTrue(TestChecker.test(input, expect, 475))

#     def test_all_14(self):
#         input = """
#             main: function auto(b: float, c: auto) {
#                 do {
#                     x: integer = 1;
#                 } while (x + 1);
#             }
#         """
#         expect = """Undeclared Identifier: x"""
#         self.assertTrue(TestChecker.test(input, expect, 476))

#     def test_all_15(self):
#         input = """
#             goo: function auto(b: float, c: auto) {
#                 do {
#                     x: integer = "abc";
#                 } while (x + 1 == 2);
#             }
#         """
#         expect = "Undeclared Identifier: x"
#         self.assertTrue(TestChecker.test(input, expect, 477))

#     def test_all_16(self):
#         input = """
#             foo: function auto(b: float, c: auto) {
#                 do {
#                     x: integer = "abc";
#                 } while (x + 1);
#             }
#         """
#         expect = "Undeclared Identifier: x"
#         self.assertTrue(TestChecker.test(input, expect, 478))


#     def test_all_17(self):
#         input = '''goo: function void(a: auto, a: auto) inherit foo{}'''
#         expect = 'Undeclared Function: foo'
#         self.assertTrue(TestChecker.test(input, expect, 479))

#     def test_all_18(self):
#         input = '''goo: function integer(){}
#             a: auto = goo;'''
#         expect = "Undeclared Identifier: goo"
#         self.assertTrue(TestChecker.test(input, expect, 480))

#     def test_all_19(self):
#         input = '''goo: function integer() {}
#             a: auto = {goo, 1, 3};'''
#         expect = 'Undeclared Identifier: goo'
#         self.assertTrue(TestChecker.test(input, expect, 481))

#     def test_all_20(self):
#         input = '''goo: function integer(){}
#             main: function void(){
#                 goo = 3;
#             }'''
#         expect = 'Undeclared Identifier: goo'
#         self.assertTrue(TestChecker.test(input, expect, 482))

#     def test_all_21(self):
#         input = '''goo: function integer(){}
#             main: function void(){
#                 n: integer;
#                 n = goo() + 1;
#             }'''
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input, expect, 483))

#     def test_all_22(self):
#         input = '''foo: function integer(){}
#             main: function void(){
#                 foo: integer = 3;
#                 a: integer;
#                 a = foo(); // line 5
#             }'''
#         expect = 'Type mismatch in expression: FuncCall(foo, [])'
#         self.assertTrue(TestChecker.test(input, expect, 484))

#     def test_all_23(self):
#         input = '''inc : function void (out n : integer, a: float) inherit foo{}
#             foo : function auto (inherit n: float, n: integer){}'''
#         expect = "Type mismatch in expression: "
#         self.assertTrue(TestChecker.test(input, expect, 485))

#     def test_all_24(self):
#         input = '''foo: function void (a: auto) {}
#             main: function void() {
#                 foo();
#             }'''
#         expect = "Type mismatch in statement: CallStmt(foo, )"
#         self.assertTrue(TestChecker.test(input, expect, 486))

#     def test_all_25(self):
#         input = '''occho: function void (a: auto) {}
#             main: function void() {
#                 occho(1,2);
#             }'''
#         expect = "Type mismatch in statement: CallStmt(occho, IntegerLit(1), IntegerLit(2))"
#         self.assertTrue(TestChecker.test(input, expect, 487))

#     def test_all_26(self):
#         input = '''dc : auto={4,5,6};
#             y:  auto=dc[1,2];'''
#         expect = "Type mismatch in expression: ArrayCell(dc, [IntegerLit(1), IntegerLit(2)])"
#         self.assertTrue(TestChecker.test(input, expect, 488))
        
#     def test_all_27(self):
#         input = '''a: array[2,2] of integer;
#             b: array[2] of integer = a[0];'''
#         expect = 'No entry point'
#         self.assertTrue(TestChecker.test(input, expect, 489))
        
#     def test_all_28(self):
#         input = '''foo: function integer() {
#                 a: integer = 12;
#                 return 3;
#                 a: float = 14;
#             }'''
#         expect = 'Redeclared Variable: a'
#         self.assertTrue(TestChecker.test(input, expect, 490))
        
#     def test_all_29(self):
#         input = '''main: function integer(a: integer) {
#                 if (a < 13) return 16;
#                 else a = a + 1;
#                 a: float = 12;
#                 return 10;
#             }'''
#         expect = 'Redeclared Variable: a'
#         self.assertTrue(TestChecker.test(input, expect, 491))
        
#     def test_all_30(self):
#         input = '''main: function integer() {
#                 a: integer = 1;
#                 while(a < 10) {
#                     a = a + 1;
#                     continue;
#                     a: float = b;
#                 }
#             }'''
#         expect = 'Undeclared Identifier: b'
#         self.assertTrue(TestChecker.test(input, expect, 492))
        
#     def test_all_31(self):
#         input = '''foo: function integer(inherit x: integer) inherit bar { super(2); }
#             bar: function integer(inherit y: integer) inherit foo2 { super("Hi"); }
#             foo2: function integer(inherit z: float) {}'''
#         expect = "Type mismatch in statement: CallStmt(super, IntegerLit(2))"
#         self.assertTrue(TestChecker.test(input, expect, 493))

#     def test_all_32(self):
#         input = '''a: float = foo(1, 2) + 1.5;
#             main: function auto(a: integer, b: integer) {
#                 return a + b; 
#             }'''
#         expect = "Undeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 494))

#     def test_all_33(self):
#         input = '''a: float = 2.3; //1
#             b: auto; //2
#             foo: function void(a: integer, b: float) {} //3
#             ddd: function void() inherit foo {} //4
#             a: function void() {} //5'''
#         expect = 'Invalid Variable: b'
#         self.assertTrue(TestChecker.test(input, expect, 495))

#     def test_all_34(self):
#         input = '''x, y: integer = 1, foo(1, 2, 3);  // 1
#             x, y: string; // 2
#             main: function integer (x: integer, y: integer, x: integer) {} // 3'''
#         expect = "Undeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 496))

#     def test_all_35(self):
#         input = '''x: integer = foo();
#             main: function integer (){}'''
#         expect = "Undeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 497))

#     def test_all_36(self):
#         input = '''foo: function void (){
#                 x = 5;
#                 x: integer;
#             }'''
#         expect = 'Undeclared Identifier: x'
#         self.assertTrue(TestChecker.test(input, expect, 498))

#     def test_all_37(self):
#         input = """goo: auto = !true&&!false||!(!true)&&"true";"""
 
#         expect = "Type mismatch in expression: BinExpr(&&, UnExpr(<class 'str'>, BooleanLit(True)), UnExpr(<class 'str'>, BooleanLit(False)))"
#         self.assertTrue(TestChecker.test(input, expect, 499))
    
#     def test_all_38(self):
#         input = """

#            _var: integer;

#             inc: function void(out x: integer)
#             // Increase input by 1
#             {
#                 x = x + 1;
#             }

#             main: function void()
#             {
#                 a, b: integer = 1, 2;
#                 inc(a);
#                 if (a == b) inc(b);
#                 else inc(a);

#                 for (_var = 0, _var < 5, _var + 1)
#                 {
#                     inc(a);
#                     a = a - b * 2;
#                 }

#                 /* My useless block */
#                 {
#                     {
#                         {
#                             _var = a - 1;
#                         }
#                     }
#                 }
#             }""" 
#         expect = "[]"
#         self.assertTrue(TestChecker.test(input, expect, 500))

#     def test_all_39(self):
#         input = """x: integer = 123;
#         fact: function integer (n: integer) {
#             if (n == 0) return 1;
#             else return n * fact(n - 1);
#         }
#         increase: function void(out n: integer, delta: integer) {
#             n = n + delta;
#             printBoolean(n);
#         }
#         main: function void() {
#             delta: integer = fact(3);
#             increase(x, delta);
#             printInteger(x);
#             preventDefault();
#         }"""
#         expect = "Type mismatch in statement: CallStmt(printBoolean, Id(n))"
#         self.assertTrue(TestChecker.test(input, expect, 501))

#     def test_all_40(self):
#         input = """
#         main: function void() {
#             for(i[1, 1+(foo("string"::"string")+i[0])] = 0, i <= 1, i+1)
#                 for(j = 0, j <= i, j+1) {
#                     printf(j);
#                 }
#         }
#         """
#         expect = "Undeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 502))
