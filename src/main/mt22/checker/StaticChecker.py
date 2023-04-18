from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC

class StaticChecker(Visitor):
    
    def __init__(self, ast):
        self.ast = ast
 
    def check(self):
        return self.visitProgram(self.ast, [])
    
    #Program: decls : List[Decl]
    def visitProgram(self, ctx, o):
        pass