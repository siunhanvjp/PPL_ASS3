from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC

class StaticChecker(Visitor):
    
    
    
    def searchParam(self, name, scope, typ): #return true if name in the given scope, false if otherwise
        if typ is FuncDecl:
            if name in [func.name for func in filter(lambda x: type(x) is FuncDecl, scope)]:
                return True
            else:
                return False
        else:
            if name in [var.name for var in filter(lambda x: type(x) is not FuncDecl, scope)]:
                return True
            else:
                return False
            
    def searchSetAuto(self): pass
    
    def __init__(self, ast):
        self.ast = ast
        
        self.loopDepth = 0 #current loop block depth
        #funcPro list of function prototype
        self.funcPro = [FuncDecl(func.name, func.return_type, func.params, func.inherit, BlockStmt([])) for func in filter(lambda x: type(x) is FuncDecl, ast.decls)] 
        
        
        self.glob = [[]] # init global scope
        #handle special function -> add them at the beginning ?? 
        
        self.hasEntry = False # if encounter void main func -> True
        
        
 
    def check(self):
        return self.visitProgram(self.ast, self.glob)
    
    #Program: decls : List[Decl]
    def visitProgram(self, ctx, param):
        
        
        for decl in ctx.decls:
            self.visit(decl, param)

        if not self.hasEntry:
            raise NoEntryPoint()
        
    
    # VarDecl: name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ctx, param):
        # param is a stack scope [[local], [nonlocal], [global]]
        # check if redecl variale in the first scope -> param[0] 
        if self.searchParam(ctx.name, param[0], VarDecl):
            raise Redeclared(Variable(), ctx.name)
        
        # check if there is init value, if yes -> visit ctx.init and check type, 
        if ctx.init != None:
            initType = self.visit(ctx.init, param)
            
            if type(ctx.typ) is AutoType:
                param[0].append(VarDecl(ctx.name, initType, None))
            elif type(ctx.typ) is ArrayType:
                pass
            else:
                pass
            
        else: # if not -> append to the current param VarDecl(ctx.name, ctx.typ, None)
            param[0].append(VarDecl(ctx.name, ctx.typ, None))
            
        
        
        
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ctx, param):
        # check if redecl in the current param ? 
        
        
        pass
    












    def visitIntegerLit(self, ctx, param):
        return IntegerType()
    
    def visitFloatLit(self, ctx, param):
        return FloatType()
    
    def visitStringLit(self, ctx, param):
        return StringType()
    
    def visitBooleanLit(self, ctx, param):
        return BooleanType()
    
    def visitFloatLit(self, ctx, param):
        return FloatLit()
    
    

    
    