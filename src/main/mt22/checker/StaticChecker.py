from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC

class StaticChecker(Visitor):
    
    
    # typ1 = typ2
    def compareNotAuto(self, typ1, typ2):
        if type(typ1) is not type(typ2):
            if not(type(typ1) is FloatType and type(typ2) is IntegerType):
                return False
        elif type(typ1) is ArrayType:
            if typ1.dimensions == typ2.dimensions and type(typ1.typ) is FloatType and type(typ2.typ) is IntegerType:
                return True 
            if typ1.dimensions != typ2.dimensions or type(typ1.typ) is not type(typ2.typ):
                return False
        else:
            return True
    
    # def searchName(self, name, scope, typ): #return true if name in the given scope, false if otherwise
    #     if typ is FuncDecl:
    #         if name in [func.name for func in list(filter(lambda x: type(x) is FuncDecl, scope))]:
    #             return True
    #         else:
    #             return False
    #     else:
    #         if name in [var.name for var in list(filter(lambda x: type(x) is not FuncDecl, scope))]:
    #             return True
    #         else:
    #             return False
            
    def searchName(self, name, scope, typ): #return true if name in the given scope, false if otherwise
            if name in [var.name for var in scope]:
                return True
            else:
                return False
    
            
    def searchSetAuto(self, name, typ, scope, target): 
        if target == "var":   
            for env in scope: 
                for decl in env:
                    if type(decl) is not FuncDecl and decl.name == name:
                        decl.typ = typ #update type in env scope
                        #check if it is a func param
                        if type(decl) is ParamDecl and decl.inherit == False:
                            for param in scope[-1][-1].params: #most recently funcdecl
                                if param.name == name:
                                    param.typ = typ #update type in funcdecl
                                    return
                        elif type(decl) is ParamDecl and decl.inherit == True:
                            inherit_name = scope[-1][-1].inherit #name of inherit function
                            inherit_func = self.findFunc(inherit_name, scope)
                            
                            for param in inherit_func.params:
                                if param.name == name:
                                    param.typ = typ
                                    return
                        else:
                            return  
                            
        else:
            #change return type
            decl = self.findFunc(name, scope)
            decl.return_type = typ

    
        
        
    def findFunc(self, name, scope):
        #find and return the same name function
        #find in global scope
        for decl in scope[-1]:
            if type(decl) is FuncDecl and decl.name == name:
                return decl
        #find in prototype scope
        for decl in self.funcPro:
            if decl.name == name:
                return decl
        #if dont exist
        return None
              
    def findVar(self, name, param):
        for scope in param:
            for decl in scope:
                if type(decl) is not FuncDecl and decl.name == name:
                    return decl.typ
        return None
    
    def findName(self, name, param):
        #find and return the same name function
        #find in global scope
        for scope in param:
            for decl in scope:
                if decl.name == name:
                    return decl
        #find in prototype scope
        for decl in self.funcPro:
            if decl.name == name:
                return decl
        #if dont exist
        return None
    
    def inferTypeExp(self, exp, typ, param):
        if type(exp) is Id: # has a problem ? Id can be inherited id
            self.searchSetAuto(exp.name, typ, param, 'var')
        elif type(exp) is FuncCall: #if funcall -> find the function and set return type
            self.searchSetAuto(exp.name, typ, param, 'func')
    
    def __init__(self, ast):
        self.ast = ast
        
        self.loopDepth = 0 #current loop block depth
        #funcPro list of function prototype
        self.funcPro = [FuncDecl(func.name, func.return_type, func.params, func.inherit, BlockStmt([])) for func in list(filter(lambda x: type(x) is FuncDecl, ast.decls))] 
        
        
        self.glob = [[
                        FuncDecl("readInteger", IntegerType(), [], None, BlockStmt([])),
                        FuncDecl("printInteger", VoidType(), [ParamDecl('anArg', IntegerType())], None, BlockStmt([])),
                        FuncDecl("readFloat", FloatType(), [], None, BlockStmt([])),
                        FuncDecl("writeFloat", VoidType(), [ParamDecl('anArg', FloatType())], None, BlockStmt([])),
                        FuncDecl("readBoolean", BooleanType(), [], None, BlockStmt([])),
                        FuncDecl("printBoolean", VoidType(), [ParamDecl('anArg', BooleanType())], None, BlockStmt([])),
                        FuncDecl("readString", StringType(), [], None, BlockStmt([])),
                        FuncDecl("printString", VoidType(), [ParamDecl('anArg', StringType())], None, BlockStmt([])),
                        
                        FuncDecl("super", VoidType(), [], None, BlockStmt([])),
                        FuncDecl("preventDefault", VoidType(), [], None, BlockStmt([])),
                        
                    ]] # init global scope
        #handle special function -> add them at the beginning ?? 
        
        self.hasEntry = False # if encounter void main func -> True
        
        self.return_type = None
        
        
 
    def check(self):
        return self.visitProgram(self.ast, self.glob)
    
    #Program: decls : List[Decl]
    def visitProgram(self, ctx, param):

        for decl in ctx.decls:
            self.visit(decl, param)

        if not self.hasEntry:
            raise NoEntryPoint()
        
        return []
        
    
    # VarDecl: name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ctx, param):
        # param is a stack scope [[local], [nonlocal], [global]]
        # check if redecl variale in the first scope -> param[0] 
        if self.searchName(ctx.name, param[0], VarDecl):
            raise Redeclared(Variable(), ctx.name)
        
        # 2 cases, type is auto or not auto
        if type(ctx.typ) is not AutoType: 
            #INTEGER | FLOAT | BOOLEAN | STRING | array_typ; 
            
            param[0].append(VarDecl(ctx.name, ctx.typ, None)) # !!!
            
            if ctx.init is not None: #has init so check type
                initType = self.visit(ctx.init, param)
                if type(initType) is not AutoType:
                    
                    if not(self.compareNotAuto(ctx.typ, initType)):
                        raise TypeMismatchInVarDecl(ctx) 
                    
                    
                else: #if type of init is auto -> can only be Id or funcall
                    self.inferTypeExp(ctx.init, ctx.typ, param)
                           
            #append param to current env               
        else: #if type of vardecl is Auto :D
            if ctx.init is None:
                raise Invalid(Variable(), ctx.name)
            
            param[0].append(VarDecl(ctx.name, ctx.typ, None))
            
            initType = self.visit(ctx.init, param) # what if return AutoType ??
            
            if type(initType) is not AutoType: 
                self.searchSetAuto(ctx.name, initType, param, 'var')
            
        return param
            
            
                   

  
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ctx, param):
        
        # check if redecl in the current scope ? 
        if self.searchName(ctx.name, param[-1], FuncDecl):
            raise Redeclared(Function(), ctx.name)
        
        for funcdecl in self.funcPro: #update if changed was made in funcPro
            if funcdecl.name == ctx.name:
                ctx.return_typ = funcdecl.return_type
                ctx.params = funcdecl.params
                break
        
        env = []
        
        for decl in ctx.params:
            if self.searchName(decl.name, env, ParamDecl):
                raise Redeclared(Parameter(), decl.name)
            else:
                env.append(ParamDecl(decl.name, decl.typ, decl.out, decl.inherit))
        
        param.insert(0,env) #append para of func to scope
        
        param[-1].append(FuncDecl(ctx.name, ctx.return_typ, ctx.params, ctx.inherit, BlockStmt([])))

        body_func = ctx.body.body #List[Stmt or VarDecl]
        len_body = len(ctx.body.body)
        
        if ctx.inherit is not None:
            inherit_func = self.findFunc(ctx.inherit, param)
            if inherit_func is None:
                raise Undeclared(Function(), ctx.inherit)
            else:
                #check paramlist when call
                for decl in inherit_func.params:
                    temp = []
                    if self.searchName(decl.name, temp, ParamDecl):
                        temp.append(decl)
                        raise Redeclared(Parameter(), decl.name)

                inherit_para = [para for para in list(filter(lambda x: x.inherit, inherit_func.params))]

                #check if redecl inherit in paralist
                for decl in env:
                    if self.searchName(decl.name, inherit_para, ParamDecl):
                        raise Invalid(Parameter(), decl.name)
                
                #append inherit param to local scope
                for param_decl in inherit_para:
                    param[0].append(param_decl)
                
                len_inherit = len(inherit_func.params)
                
                len_func = len(ctx.params)
                
                if(len_inherit != 0):
                    
                    if(len_body > 0):
                        if type(body_func[0]) is CallStmt and body_func[0].name in ["super", "preventDefault"]: 
                            if body_func[0].name == "super":
                                super_args = body_func[0].args
                                if len(super_args) > len_inherit:
                                    raise TypeMismatchInExpression(super_args[len_inherit])
                                elif len(super_args) < len_inherit:
                                    raise TypeMismatchInExpression("")
                                else:
                                    for i, arg in enumerate(super_args):
                                        # arg vs inherit_func.params[i]
                                        
                                        argType = self.visit(arg, param)
                                        paramType = inherit_func.params[i].typ
                                        
                                        if type(argType) is not AutoType and type(paramType) is not AutoType and type(argType) is not type(paramType):
                                            if type(paramType) is FloatType and type(argType) is IntegerType:
                                                pass
                                            else:
                                                raise TypeMismatchInExpression(arg)
                                        elif type(argType) is AutoType and type(paramType) is not AutoType:
                                            if type(arg) is Id:
                                                self.searchSetAuto(arg.name, paramType, param, 'var')
                                            elif type(arg) is FuncCall: #if funcall -> find the function and set return type
                                                self.searchSetAuto(arg.name, paramType, param, 'func')  
                                        elif type(paramType) is AutoType and type(argType) is not AutoType:
                                            
                                            
                                            
                                            if inherit_func.params[i].inherit:
                                                self.searchSetAuto(inherit_func.params[i].name, argType, param, 'var')
                                            else:
                                                inherit_func.params[i].typ = argType
                                                
                                                          
                                        else: #2 thang type nhu nhau :D
                                            if type(argType) is ArrayType:
                                                if argType.dimensions != paramType.dimensions or type(argType.typ) is not type(paramType.typ): 
                                                    if not(argType.dimensions == paramType.dimensions and type(paramType.typ) is FloatType and type(argType.typ) is IntegerType):
                                                        raise TypeMismatchInExpression(arg)
                            else:
                                if len(body_func[0].args) > 0:
                                    #error do co arg
                                    raise TypeMismatchInExpression(body_func[0].args[0])
                        else:
                            #ko co super hay prevent -> raise loi mismatch ?
                            raise TypeMismatchInExpression("")
                    else: #check super truoc hay check inherit truoc ??
                        #ham rong 
                        raise TypeMismatchInExpression("")
            
            #bo cai stmt dau tien
            body_func = body_func[1:]
                
        else:
            
            #check neu goi super hay prevent thi throw loi invalid first
            if(len_body > 0):
                if type(body_func[0]) is CallStmt and body_func[0].name in ["super", "preventDefault"]: 
                    raise InvalidStatementInFunction(ctx.name)
        
        #handle stmt in body of function
        
        self.return_type = ctx.return_type
        flag_return = False
        for stmt in body_func:
            
            if type(stmt) is ReturnStmt:
                
                if not(flag_return):
                    flag_return = True
                    #handle first return stmt
                    if stmt.expr is not None:
                        returnType = self.visit(stmt.expr, param)
                    else:
                        returnType = VoidType()
                    
                    if type(returnType) is AutoType:
                        if type(ctx.return_type) is not AutoType:
                            self.inferTypeExp(stmt.expr, ctx.return_type, param)
                    else:
                        if type(ctx.return_type) is AutoType: 
                            ctx.return_type = returnType
                            current_func = findFunc(ctx.name, param)
                            current_func.return_type = returnType
                            self.return_type = returnType
                        else:
                            if not(self.compareNotAuto(ctx.return_type, returnType)):
                                raise TypeMismatchInStatement(stmt)
                            
                            # if type(returnType) is not type(ctx.return_type):
                            #     if type(ctx.return_type) is FloatType and type(returnType) is IntegerType:
                            #         pass
                            #     else:
                            #         raise TypeMismatchInStatement(stmt)
                            # elif type(returnType) is ArrayType:
                            #     if returnType.dimensions != ctx.return_type.dimensions or type(returnType.typ) is not type(ctx.return_type.typ):
                            #         raise TypeMismatchInStatement(stmt)
                else:
                    continue
            else:
                
                self.visit(stmt, param)
                
        #done visiting all stmt in the body:
        
        #reset return_type
        self.return_type = None
        #pop the local environment
        param.pop(0)
        
        
        #check if this is the entry point
        if ctx.name == "main" and type(ctx.return_type) is VoidType and len(ctx.params) == 0:
            self.hasEntry = True
        
                
        


    def visitBinExpr(self, ctx, param):
        op = ctx.op
        leftType = self.visit(ctx.left, param)
        rightType = self.visit(ctx.right, param)
        print(type(leftType))
        if op in ["+", "-", "*", "/"]:
            operandType = [AutoType, IntegerType, FloatType]
            if type(leftType) not in operandType and type(rightType) not in operandType:
                raise TypeMismatchInExpression(ctx)
            operandType.pop(0)
            if type(leftType) is not AutoType and type(rightType) is not AutoType:
                if type(leftType) is FloatType or type(rightType) is FloatType:
                    return FloatType()
                else:
                    return IntegerType()
            elif type(leftType) is AutoType and type(rightType) is not AutoType:
                self.inferTypeExp(ctx.left, rightType, param)   
                return rightType
            elif type(leftType) is not AutoType and type(rightType) is AutoType:     
                self.inferTypeExp(ctx.right, leftType, param)
                return leftType
            else: #ca hai deu auto :D
                pass
        elif op in  ["%"]:
            operandType = [AutoType, IntegerType]
            if type(leftType) not in operandType and type(rightType) not in operandType:
                raise TypeMismatchInExpression(ctx)
            operandType.pop(0)
            if type(leftType) is not AutoType and type(rightType) is not AutoType:
                return IntegerType()
            elif type(leftType) is AutoType and type(rightType) is not AutoType:     
                self.inferTypeExp(ctx.left, rightType, param)   
                return rightType
            elif type(leftType) is not AutoType and type(rightType) is AutoType:     
                self.inferTypeExp(ctx.right, leftType, param)
                return leftType
            else: #ca hai deu auto :D
                pass
        elif op in ["&&", "||"]:
            operandType = [AutoType, BooleanType]
            if type(leftType) not in operandType and type(rightType) not in operandType:
                raise TypeMismatchInExpression(ctx)
            operandType.pop(0)
            if type(leftType) is not AutoType and type(rightType) is not AutoType:
                return BooleanType()
            elif type(leftType) is AutoType and type(rightType) is not AutoType:     
                self.inferTypeExp(ctx.left, rightType, param)
                return rightType
            elif type(leftType) is not AutoType and type(rightType) is AutoType:     
                self.inferTypeExp(ctx.right, leftType, param)
                return leftType
            else: #ca hai deu auto :D -> infer both is boolean
                self.inferTypeExp(ctx.right, BooleanType(), param)
                self.inferTypeExp(ctx.left, BooleanType(), param)
                return BooleanType() 
        elif op in ["::"]:
            operandType = [AutoType, StringType]
            if type(leftType) not in operandType and type(rightType) not in operandType:
                raise TypeMismatchInExpression(ctx)
            operandType.pop(0)
            if type(leftType) is not AutoType and type(rightType) is not AutoType:
                return StringType()
            elif type(leftType) is AutoType and type(rightType) is not AutoType:     
                self.inferTypeExp(ctx.left, rightType, param)
                return rightType
            elif type(leftType) is not AutoType and type(rightType) is AutoType:     
                self.inferTypeExp(ctx.right, leftType, param)
                return leftType
            else: #ca hai deu auto :D -> infer both is string
                self.inferTypeExp(ctx.right, StringType(), param)
                self.inferTypeExp(ctx.left, StringType(), param)
                return StringType() 
        elif op in ["==", "!="]:
            operandType = [AutoType, BooleanType, IntegerType]
            if type(leftType) not in operandType and type(rightType) not in operandType:
                raise TypeMismatchInExpression(ctx)
            operandType.pop(0)
            if type(leftType) is not AutoType and type(rightType) is not AutoType:
                return BooleanType()
            elif type(leftType) is AutoType and type(rightType) is not AutoType:     
                self.inferTypeExp(ctx.left, rightType, param)
                return BooleanType()
            elif type(leftType) is not AutoType and type(rightType) is AutoType:     
                self.inferTypeExp(ctx.right, leftType, param)
                return BooleanType()
            else: #ca hai deu auto :D
                pass
        elif op in ["<", "<=", ">", ">="]:
            operandType = [AutoType, FloatType, IntegerType]
            if type(leftType) not in operandType and type(rightType) not in operandType:
                raise TypeMismatchInExpression(ctx)
            operandType.pop(0)
            if type(leftType) is not AutoType and type(rightType) is not AutoType:
                return BooleanType()
            elif type(leftType) is AutoType and type(rightType) is not AutoType:     
                self.inferTypeExp(ctx.left, rightType, param)
                return BooleanType()
            elif type(leftType) is not AutoType and type(rightType) is AutoType:     
                self.inferTypeExp(ctx.right, leftType, param)
                return BooleanType()
            else: #ca hai deu auto :D
                pass
            
            

    def visitUnExpr(self, ctx, param):
        op = ctx.op
        valType = self.visit(ctx.val, param)
        
        if op == '!':
            if type(valType) is BooleanType:
                return BooleanType()
            elif type(valType) is AutoType:
                self.inferTypeExp(ctx.val, BooleanType(), param)
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ctx)
        elif op == '-':
            if type(valType) in [FloatType, IntegerType]:
                return valType
            elif type(valType) is AutoType:
                self.inferTypeExp(ctx.val, FloatType(), param)
                return FloatType()
            else:
                raise TypeMismatchInExpression(ctx)
        

    def visitId(self, ctx, param):
        # res = self.findVar(ctx.name, param)
        res = self.findVar(ctx.name, param)
        if res is None:
            raise Undeclared(Identifier(), ctx.name)
        else:
            return res
    # name: str, cell: List[Expr]
    def visitArrayCell(self, ctx, param):
        #check name
        arr_type = self.findVar(ctx.name, param)
        if arr_type is None:
            raise Undeclared(Identifier(), ctx.name)
        
        if type(arr_type) is not ArrayType:
            #raise loi cc gi o day :D??
            raise TypeMismatchInExpression(ctx.name)
        
        dimen = arr_type.dimensions 
        if len(ctx.cell) > len(dimen):
            raise TypeMismatchInExpression(ctx.cell)
        
        for expr in ctx.cell:
            expr_typ = self.visit(expr, param)
            # co ra auto duoc ko :D??
            if type(expr_typ) is not IntegerType:
                raise TypeMismatchInExpression(expr)
            
        if len(dimen) == len(ctx.cell):
            return arr_type.typ
        else:
            dimen.pop(0)
            return ArrayType(dimen, arr_type.typ)
            
        

    def visitIntegerLit(self, ctx, param):
        return IntegerType()
    
    def visitFloatLit(self, ctx, param):
        return FloatType()
    
    def visitStringLit(self, ctx, param):
        return StringType()
    
    def visitBooleanLit(self, ctx, param):
        return BooleanType()
    
    def visitFloatLit(self, ctx, param):
        return FloatType()
    
    # explist: List[Expr]
    def visitArrayLit(self, ctx, param):
        len_exp = len(ctx.explist)
        if len_exp == 0:
            pass # deo biet tra ve type kieu gi
        
        typs = []
        mutual_typ = None
        #check type
        for exp in ctx.explist:
            exp_typ = self.visit(exp, param)
            if type(exp_typ) is not AutoType:
                mutual_typ = exp_typ
                typs.append(exp_typ)
        
        if mutual_typ is None:
            pass # cai nay la toan bo phan tu trong array deu la Auto
        elif AutoType() in typs:
            typs_no_auto = list(filter(lambda x : type(x) is not AutoType, typs))
            
            if(len(list(filter(lambda x : type(x) is not type(mutual_typ), typs_no_auto))) != 0):
                raise IllegalArrayLiteral(ctx)
            else: # all same type
                if type(mutual_typ) is not ArrayType:
                    #suy dien auto
                    for i, expr in enumerate(ctx.explist):
                        if type(typs[i]) is AutoType:
                            if type(expr) is Id: # has a problem ? Id can be inherited id
                                self.searchSetAuto(expr.name, mutual_typ, param, 'var')
                            elif type(expr) is FuncCall: #if funcall -> find the function and set return type
                                self.searchSetAuto(expr.name, mutual_typ, param, 'func') 
                    
                    return ArrayType([len_exp], mutual_typ)
                else:
                    dimen = mutual_typ.dimensions
                    arr_type = mutual_typ.typ
                    
                    if(len(list(filter(lambda x : x.dimensions != dimen or type(x.typ) is not type(arr_type), typs_no_auto))) != 0):
                        raise IllegalArrayLiteral(ctx)
                    else:
                        
                        #suy dien kieu auto
                        for i, expr in enumerate(ctx.explist):
                            if type(typs[i]) is AutoType:
                                if type(expr) is Id: # has a problem ? Id can be inherited id
                                    self.searchSetAuto(expr.name, mutual_typ, param, 'var')
                                elif type(expr) is FuncCall: #if funcall -> find the function and set return type
                                    self.searchSetAuto(expr.name, mutual_typ, param, 'func') 
                        dimen.insert(0, len_exp)
                        return ArrayType(dimen, arr_type)
  
        else:
            if(len(list(filter(lambda x : type(x) is not type(mutual_typ), typs))) != 0):
                raise IllegalArrayLiteral(ctx)
            else: # all same type
                if type(mutual_typ) is not ArrayType:
                    return ArrayType([len_exp], mutual_typ)
                else:
                    dimen = mutual_typ.dimensions
                    arr_type = mutual_typ.typ
                    
                    if(len(list(filter(lambda x : x.dimensions != dimen or type(x.typ) is not type(arr_type), typs))) != 0):
                        raise IllegalArrayLiteral(ctx)
                    else:
                        dimen.insert(0, len_exp)
                        return ArrayType(dimen, arr_type)
            
                
        
    
    #name: str, args: List[Expr]
    def visitFuncCall(self, ctx, param):
        func = self.findName(ctx.name, param)
        if func is None:
            raise Undeclared(Function(), ctx.name)
        elif type(func) is not FuncDecl:
            raise TypeMismatchInExpression(ctx)
        
        if len(func.params) != len(ctx.args):
            raise TypeMismatchInExpression(ctx)
        
        returnType = func.return_type
        
        for i, arg in enumerate(ctx.args):
            paramType = func.params[i].typ
            argType = self.visit(arg, param)
            
            if type(argType) is not AutoType and type(paramType) is not AutoType and type(argType) is not type(paramType):
                if not(type(paramType) is FloatType and type(argType) is IntegerType):
                    raise TypeMismatchInExpression(ctx)
            elif type(argType) is AutoType and type(paramType) is not AutoType:
                if type(arg) is Id:
                    self.searchSetAuto(arg.name, paramType, param, 'var')
                elif type(arg) is FuncCall: #if funcall -> find the function and set return type
                    self.searchSetAuto(arg.name, paramType, param, 'func')  
            elif type(paramType) is AutoType and type(argType) is not AutoType:
                    func.params[i].typ = argType
                                
            else: #2 thang type nhu nhau :D
                if type(argType) is ArrayType:
                    if argType.dimensions != paramType.dimensions or type(argType.typ) is not type(paramType.typ): 
                        if not(argType.dimensions == paramType.dimensions and type(paramType.typ) is FloatType and type(argType.typ) is IntegerType):
                            raise TypeMismatchInExpression(ctx)              
        return returnType
    
    #name: str, args: List[Expr]
    def visitCallStmt(self, ctx, param):
        func = self.findName(ctx.name, param)
        if func is None:
            raise Undeclared(Function(), ctx.name)
        elif type(func) is not FuncDecl:
            raise TypeMismatchInExpression(ctx)
        
        if len(func.params) != len(ctx.args):
            raise TypeMismatchInStatement(ctx)
        
        for i, arg in enumerate(ctx.args):
            paramType = func.params[i].typ
            argType = self.visit(arg, param)
            
            if type(argType) is not AutoType and type(paramType) is not AutoType and type(argType) is not type(paramType):
                if not(type(paramType) is FloatType and type(argType) is IntegerType):
                    raise TypeMismatchInStatement(ctx)
            elif type(argType) is AutoType and type(paramType) is not AutoType:
                if type(arg) is Id:
                    self.searchSetAuto(arg.name, paramType, param, 'var')
                elif type(arg) is FuncCall: #if funcall -> find the function and set return type
                    self.searchSetAuto(arg.name, paramType, param, 'func')  
            elif type(paramType) is AutoType and type(argType) is not AutoType:
                    func.params[i].typ = argType              
            else: #2 thang type nhu nhau :D
                if type(argType) is ArrayType:
                    if argType.dimensions != paramType.dimensions or type(argType.typ) is not type(paramType.typ): 
                        if not(argType.dimensions == paramType.dimensions and type(paramType.typ) is FloatType and type(argType.typ) is IntegerType):
                            raise TypeMismatchInStatement(ctx)  
    
    #lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ctx, param):
        leftType = self.visit(ctx.lhs, param)
        rightType = self.visit(ctx.rhs, param)
        
        
        if type(leftType) in [ArrayType, VoidType]:
            raise TypeMismatchInStatement(ctx)
        if type(leftType) is AutoType and type(rightType) is not AutoType:
            self.inferTypeExp(ctx.lhs, rightType, param)
        elif type(leftType) is not AutoType and type(rightType) is AutoType:
            self.inferTypeExp(ctx.rhs, leftType, param)
        elif type(leftType) is not AutoType and type(rightType) is not AutoType:
            if type(leftType) is not type(rightType):
                if not(type(leftType) is FloatType and type(rightType) is IntegerType):
                    raise TypeMismatchInStatement(ctx)
        else: # 2 thang deu auto
            pass
        
    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None    
    def visitIfStmt(self, ctx, param):
        condType = self.visit(ctx.cond, param)
        if type(condType) is AutoType:
            self.inferTypeExp(ctx.cond, BooleanType, param)
        elif type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        
        self.visit(ctx.tstmt, param)
        
        if ctx.fstmt is not None : 
            self.visit(ctx.fstmt, param)
    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ctx, param):
        initRhsType = self.visit(ctx.init.rhs, param)
        initLhsType = self.visit(ctx.init.rhs, param)
        if type(initRhsType) is not IntegerType:
            raise TypeMismatchInStatement(ctx)
        if type(initLhsType) is AutoType:
            self.inferTypeExp(ctx.init.lhs, IntegerType, param)
        elif type(initLhsType) is not IntegerType:
            raise TypeMismatchInStatement(ctx)
        
        condType = self.visit(ctx.cond, param)
        if type(condType) is AutoType:
            self.inferTypeExp(ctx.cond, BooleanType, param)
        elif type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        
        updType = self.visit(ctx.upd, param)
        if type(updType) is AutoType:
            self.inferTypeExp(ctx.upd, IntegerType, param)
        elif type(updType) is not IntegerType:
            raise TypeMismatchInStatement(ctx)
        
        self.loopDepth += 1
        
        self.visit(ctx.stmt, param)
        
        self.loopDepth -= 1
        
    #cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ctx, param):
        condType = self.visit(ctx.cond, param)
        if type(condType) is AutoType:
            self.inferTypeExp(ctx.cond, BooleanType, param)
        elif type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        
        self.loopDepth += 1
        
        self.visit(ctx.stmt, param)
        
        self.loopDepth -= 1
        
    def visitDoWhileStmt(self, ctx, param):
        condType = self.visit(ctx.cond, param)
        if type(condType) is AutoType:
            self.inferTypeExp(ctx.cond, BooleanType, param)
        elif type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        
        self.loopDepth += 1
        
        self.visit(ctx.stmt, param)
        
        self.loopDepth -= 1
        
    def visitBreakStmt(self, ctx, param):
        if self.loopDepth == 0:
            raise MustInLoop(ctx)
        
    def visitContinueStmt(self, ctx, param):
        if self.loopDepth == 0:
            raise MustInLoop(ctx)
    # expr: Expr or None = None
    def visitReturnStmt(self, ctx, param):
        funcType = self.return_type
        if ctx.expr is not None:
            returnType = self.visit(ctx.expr, param)
        else:
            returnType = VoidType()
            
        if type(returnType) is AutoType:
            if type(funcType) is not AutoType:
                self.inferTypeExp(stmt.expr, funcType, param)
        else:
            if type(funcType) is AutoType: 
                self.return_type = returnType
                current_func = findFunc(param[-1][-1].name, param)
                current_func.return_type = returnType
                self.return_type = returnType
            else:
                if not(self.compareNotAuto(funcType, returnType)):
                    raise TypeMismatchInStatement(ctx)
                
    def visitBlockStmt(self, ctx, param):
        env = [] 
        
        param.insert(0,env)
        
        for stmt in ctx.body:
            self.visit(stmt, param)
            
        param.pop(0)
        
        
        