from src.autogen.gmarParser import gmarParser
from src.autogen.gmarVisitor import gmarVisitor
from src.symbol_table.class_record import ClassRecord
from src.symbol_table.method_record import MethodRecord
from src.symbol_table.record import Record
from src.symbol_table.variable_record import VariableRecord

INT = "int"
INT_ARRAY = "int_array"
CHAR = "char"
BOOLEAN = "boolean"
STRING = "String"


class TypeCheckVisitor(gmarVisitor):

    def __init__(self, stable):
        self.symbol_table = stable

    def visitProg(self, ctx: gmarParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gmarParser#main_class.
    def visitMainClass(self, ctx:gmarParser.MainClassContext):
        self.symbol_table.enter_scope()

        result = self.visitChildren(ctx)

        self.symbol_table.exit_scope()

        return result

    # Visit a parse tree produced by gmarParser#main_method.
    def visitMainMethod(self, ctx:gmarParser.MainMethodContext):
        self.symbol_table.enter_scope()

        result = self.visitChildren(ctx)

        self.symbol_table.exit_scope()

        return result

    # Visit a parse tree produced by gmarParser#class_declaration.
    def visitClassDecl(self, ctx:gmarParser.ClassDeclContext):
        self.symbol_table.enter_scope()

        result = self.visitChildren(ctx)

        self.symbol_table.exit_scope()

        return result


    # Visit a parse tree produced by gmarParser#field_declaration.
    def visitFieldDecl(self, ctx:gmarParser.FieldDeclContext):
        identifier = str(self.visit(ctx.getChild(1)))
        if self.symbol_table.lookup(identifier) is not None:
            print(f"Identifier [{identifier}] already exists")
            return None

        return self.visitChildren(ctx)

    # Visit a parse tree produced by gmarParser#identifier.
    def visitIdentifier(self, ctx: gmarParser.IdentifierContext):
        identifier = str(ctx.getChild(0))
        rec = self.symbol_table.lookup(identifier)
        if rec is None:
            print(f"Identifier {rec} already exists")
            return None
        return rec

    # Visit a parse tree produced by gmarParser#method_declaration.
    def visitMethodDecl(self, ctx:gmarParser.MethodDeclContext):
        self.symbol_table.enter_scope()

        inner_body = ctx.getChild(6)

        ret_statement = self.visit(inner_body.getChild(inner_body.getChildCount() - 1))
        meth_type = str(ctx.getChild(0).getChild(0).getChild(0))

        if ret_statement is None or meth_type is None:
            print("Error on return statement")
            return None
        if ret_statement.getType != meth_type:
            print("Method and return types mismatch")
            return None

        result = self.visitChildren(ctx)

        self.symbol_table.exit_scope()
        return result

    # Visit a parse tree produced by gmarParser#blockStatement.
    def visitBlockStatement(self, ctx: gmarParser.BlockStatementContext):
        return self.visit(ctx.getChild(1))

    # Visit a parse tree produced by gmarParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx: gmarParser.DoWhileStatementContext):
        dwhile_type = self.visit(ctx.getChild(4))
        if dwhile_type.type != BOOLEAN:
            print("Do-while arg is not boolean.")
            return None
        self.visit(ctx.getChild(4))
        return Record("do_while", BOOLEAN)

    # Visit a parse tree produced by gmarParser#whileStatement.
    def visitWhileStatement(self, ctx: gmarParser.WhileStatementContext):
        while_type = self.visit(ctx.getChild(2))
        if while_type is None:
            print("NULL of while expr.")
            return None
        elif while_type.type != BOOLEAN:
            print("While args needs to be boolean.")
            return None
        self.visit(ctx.getChild(4))

        return Record("while", BOOLEAN)

    # Visit a parse tree produced by gmarParser#ifStatement.
    def visitIfStatement(self, ctx: gmarParser.IfStatementContext):
        iftype = self.visit(ctx.getChild(2))
        if iftype is None:
            print("if statement error.")
            return None
        if iftype.type != BOOLEAN:
            print("if statement arg is not boolean.")
            return None

        self.visit(ctx.getChild(4))

        return Record("if", BOOLEAN)

    # Visit a parse tree produced by gmarParser#assignStatement.
    def visitAssignStatement(self, ctx: gmarParser.AssignStatementContext):
        lval = self.visit(ctx.getChild(0))
        rval = self.visit(ctx.getChild(2))
        if lval is None:
            print("lval not found")
            return None
        elif rval is None:
            print("rval not found")
            return None
        if lval.type != rval.type:
            print("lval and rval types mismatch.")
            return None
        return None

    # Visit a parse tree produced by gmarParser#assignArrayStatement.
    def visitAssignArrayStatement(self, ctx: gmarParser.AssignArrayStatementContext):
        lval = self.visit(ctx.getChild(0))
        rval = self.visit(ctx.getChild(2))
        if lval is None:
            print("lval not found")
            return None
        elif rval is None:
            print("rval not found")
            return None

        if lval == INT_ARRAY or rval == INT:
            print("I'm tired.")
            return None

        return None

    # Visit a parse tree produced by gmarParser#printStatement.
    def visitPrintStatement(self, ctx: gmarParser.PrintStatementContext):
        print_type = self.visit(ctx.getChild(2))
        if print_type is not None:
            if print_type.type == INT or \
                    print_type.type == STRING or \
                    print_type.type == CHAR:
                return print_type
        print("sout can only print ints and strings")
        return None

    # Visit a parse tree produced by gmarParser#breakStatement.
    def visitBreakStatement(self, ctx: gmarParser.BreakStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gmarParser#return_statement.
    def visitReturnStatement(self, ctx:gmarParser.ReturnStatementContext):
        return self.visit(ctx.getChild(1))

    # Visit a parse tree produced by gmarParser#parameter_list.
    def visitParamList(self, ctx:gmarParser.ParamListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gmarParser#parameters.
    def visitParameters(self, ctx: gmarParser.ParametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gmarParser#parameter.
    def visitParameter(self, ctx: gmarParser.ParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gmarParser#newCallExpression.
    def visitNewCallExpression(self, ctx: gmarParser.NewCallExpressionContext):
        return self.visit(ctx.getChild(1))

    # Visit a parse tree produced by gmarParser#minusExpression.
    def visitMinusExpression(self, ctx: gmarParser.MinusExpressionContext):
        typeRec = self.visit(ctx.getChild(1))
        if typeRec.type != INT:
            print("Minus operator can preceen int value")
            return None
        return Record("minusInt", INT)

    # Visit a parse tree produced by gmarParser#boolExpression.
    def visitBoolExpression(self, ctx: gmarParser.BoolExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gmarParser#arrayCreateExpression.
    def visitArrayCreateExpression(self, ctx: gmarParser.ArrayCreateExpressionContext):
        tr = self.visit(ctx.getChild(3))
        if tr.type != INT:
            print("array size must be an integer")
            return None
        return Record("int_array", INT_ARRAY)

    # Visit a parse tree produced by gmarParser#methodCallExpression.
    def visitMethodCallExpression(self, ctx: gmarParser.MethodCallExpressionContext):
        class_ret = self.visit(ctx.getChild(0))

        meth_name = str(ctx.getChild(2).getChild(0).getChild(0))

        if meth_name is None:
            print(f"Method [{meth_name}] was not found")
            return None
        if class_ret is None:
            print(f"Class [{class_ret}] was not found")
            return None

        class_record = None

        if type(class_ret) == VariableRecord:
            class_record = self.symbol_table.lookup(class_ret.type)
        elif type(class_ret) == MethodRecord:
            class_record = self.symbol_table.lookup(class_ret.type)
        else:
            class_record = class_ret

        if class_record is None:
            print(f"Class record [{class_record}] was not found.")
            return None

        meth_record: MethodRecord = class_record.get_method(meth_name)

        if meth_name is None:
            print(f"Method [{meth_name}] was not found in class [{class_ret.id}]")
            return None

        ccount = ctx.getChild(2).getChildCount()

        seps = 0
        param_num = 0
        for i in range(2, ccount - 1):
            temp = str(ctx.getChild(2).getChild(i))
            if temp != ',':
                paramIden = self.visit(ctx.getChild(2).getChild(i))
                if not meth_record.contains_parameter(param_num, paramIden):
                    print(f"Invalid parameter [{paramIden.id}]")
                    return None
                param_num += 1
            else:
                seps += 1

        params_count = ccount - seps - 3
        if params_count != len(meth_record):
            print(f"Unmatched number of params for method [{meth_record.id}]")
            return None

        return meth_record

    # Visit a parse tree produced by gmarParser#notExpression.
    def visitNotExpression(self, ctx: gmarParser.NotExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gmarParser#multiplicationExpression.
    def visitMulExpression(self, ctx:gmarParser.MulExpressionContext):
        ltype = self.visit(ctx.getChild(0))
        sym = str(ctx.getChild(1))
        rtype = self.visit(ctx.getChild(2))

        if ltype is None or rtype is None or sym is None:
            print("null on multiplication")
            return None
        if ltype.type == INT and rtype.type == INT:
            return Record("int arithmetic", INT)

        print("type error on multiplication")
        return None


    # Visit a parse tree produced by gmarParser#comparisonExpression.
    def visitDisjunctionExpression(self, ctx:gmarParser.DisjunctionExpressionContext):
        ltype = self.visit(ctx.getChild(0))
        rtype = self.visit(ctx.getChild(2))

        if ltype is None or rtype is None:
            print("Null on logical expr")
            return None
        if ltype.type == BOOLEAN:
            if rtype.type == BOOLEAN:
                return Record("logical", BOOLEAN)
            print("type different from boolean on a logical expression")
            return None
        print("error on logical expression")
        return None

    # Visit a parse tree produced by gmarParser#comparisonExpression.
    def visitConjunctionExpression(self, ctx:gmarParser.ConjunctionExpressionContext):
        ltype = self.visit(ctx.getChild(0))
        rtype = self.visit(ctx.getChild(2))

        if ltype is None or rtype is None:
            print("Null on logical expr")
            return None
        if ltype.type == BOOLEAN:
            if rtype.type == BOOLEAN:
                return Record("logical", BOOLEAN)
            print("type different from boolean on a logical expression")
            return None
        print("error on logical expression")
        return None

    # Visit a parse tree produced by gmarParser#braquetedExpression.
    def visitBracketExpression(self, ctx:gmarParser.BracketExpressionContext):
        return self.visit(ctx.getChild(1))


    # Visit a parse tree produced by gmarParser#integerExpression.
    def visitIntegerExpression(self, ctx: gmarParser.IntegerExpressionContext):
        return Record("int", INT)

    # Visit a parse tree produced by gmarParser#substractionExpression.
    def visitSubtractExpression(self, ctx:gmarParser.SubtractExpressionContext):
        ltype = self.visit(ctx.getChild(0))
        sym = str(ctx.getChild(1))
        rtype = self.visit(ctx.getChild(2))

        if ltype is None or rtype is None or sym is None:
            print("null on subtraction")
            return None
        if ltype.type == INT and rtype.type == INT:
            return Record("int arithmetic", INT)

        print("type error on subtraction")
        return None

    # Visit a parse tree produced by gmarParser#variableCallExpression.
    def visitVariableCallExpression(self, ctx: gmarParser.VariableCallExpressionContext):
        class_rec: Record = self.visit(ctx.getChild(0))
        var_name = str(ctx.getChild(2))

        if var_name is None:
            print(f"Variable [{var_name}] record was not found.")
            return None

        if class_rec is None:
            print(f"Class [{class_rec.id}] was not found.")
            return None

        class_record: ClassRecord = None

        if type(class_rec) == VariableRecord:
            class_record = self.symbol_table.lookup(class_rec.type)
        elif type(class_rec) == MethodRecord:
            class_record = self.symbol_table.lookup(class_rec.type)
        else:
            class_record = class_rec

        if class_record is None:
            print(f"class record [{class_record.id}] was not found.")
            return None

        var_record = class_record.get_field(var_name)

        if var_record is None:
            print(f"Variable record [{var_record}] was not found.")
            return None

        return var_record


    # Visit a parse tree produced by gmarParser#thisExpression.
    def visitThisExpression(self, ctx: gmarParser.ThisExpressionContext):
        return self.symbol_table.lookup("this")

    # Visit a parse tree produced by gmarParser#lessThanExpression.
    def visitLtExpression(self, ctx:gmarParser.LtExpressionContext):
        ltype = self.visit(ctx.getChild(0))
        rtype = self.visit(ctx.getChild(2))

        if ltype is None or rtype is None:
            print("None on \lt expression")
            return None
        if ltype.type == INT:
            if rtype.type == INT:
                return Record("less_than", BOOLEAN)
            print("Evaluate INT or CHARs")
            return None
        elif ltype.type == CHAR:
            if rtype == CHAR:
                return Record("less_than", BOOLEAN)
            print("Evaluate INT or CHARs")
            return None

        print("Erro on \lt expression")
        return None

    # Visit a parse tree produced by gmarParser#sumExpression.
    def visitSumExpression(self, ctx: gmarParser.SumExpressionContext):
        ltype = self.visit(ctx.getChild(0))
        sym = str(ctx.getChild(1))
        rtype = self.visit(ctx.getChild(2))

        if ltype is None or rtype is None or sym is None:
            print("null on addition")
            return None

        if ltype.type == STRING or ltype == CHAR:
            if rtype == STRING or rtype == CHAR:
                return Record("StringAdd", STRING)
        else:
            if ltype.type == INT and rtype.type == INT:
                return Record("intAdd", INT)

        print("type error on addition")
        return None


    # Visit a parse tree produced by gmarParser#arrayLengthExpression.
    def visitArrayLengthExpression(self, ctx: gmarParser.ArrayLengthExpressionContext):
        tp = self.visit(ctx.getChild(0))
        if tp.type != INT_ARRAY:
            print("Length can be called on int arrays")
            return None
        return Record("arrayLength", INT)

    # Visit a parse tree produced by gmarParser#charExpression.
    def visitCharExpression(self, ctx: gmarParser.CharExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#arraySelectExpression.
    def visitArraySelectExpression(self, ctx: gmarParser.ArraySelectExpressionContext):
        ltype = self.visit(ctx.getChild(0)) # int_arr
        rtype = self.visit(ctx.getChild(2)) # int

        if ltype is None:
            print("array error")
            return None
        if rtype is None:
            print("array index error")
            return None

        if ltype.type != INT_ARRAY:
            print("argument is no an int array")
            return None
        if rtype.type != INT:
            print("array index can only be an integer")
            return None
        return Record("int_array", INT)


    # Visit a parse tree produced by gmarParser#equalExpression.
    def visitEqualExpression(self, ctx: gmarParser.EqualExpressionContext):
        ltype = self.visit(ctx.getChild(0))
        rtype = self.visit(ctx.getChild(2))

        if ltype is None or rtype is None:
            print("None on \eq expression")
            return None
        if ltype.type == INT:
            if rtype.type == INT:
                return Record("equals", BOOLEAN)
            print("Compare same types")
            return None
        elif ltype.type == CHAR:
            if rtype == CHAR:
                return Record("equals", BOOLEAN)
            print("Compare same types")
            return None

        print("Error on \eq expression")
        return None


    # Visit a parse tree produced by gmarParser#equalExpression.
    def visitNotEqualExpression(self, ctx:gmarParser.NotEqualExpressionContext):
        ltype = self.visit(ctx.getChild(0))
        rtype = self.visit(ctx.getChild(2))

        if ltype is None or rtype is None:
            print("None on \neq expression")
            return None
        if ltype.type == INT:
            if rtype.type == INT:
                return Record("not_equals", BOOLEAN)
            print("Compare same types")
            return None
        elif ltype.type == CHAR:
            if rtype == CHAR:
                return Record("not_equals", BOOLEAN)
            print("Compare same types")
            return None

        print("Error on \\neq expression")
        return None

    # Visit a parse tree produced by gmarParser#divisionExpression.
    def visitDivExpression(self, ctx:gmarParser.DivExpressionContext):
        ltype = self.visit(ctx.getChild(0))
        sym = str(ctx.getChild(1))
        rtype = self.visit(ctx.getChild(2))

        if ltype is None or rtype is None or sym is None:
            print("null on division")
            return None
        if ltype.type == INT and rtype.type == INT:
            return Record("int arithmetic", INT)

        print("type error on division")
        return None

    # Visit a parse tree produced by gmarParser#call_a_method.
    def visitMethodCall(self, ctx:gmarParser.MethodCallContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by gmarParser#integral.
    def visitIntegral(self, ctx: gmarParser.IntegralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gmarParser#boolean.
    def visitBoolean(self, ctx: gmarParser.BooleanContext):
        return Record('char', CHAR)

    # Visit a parse tree produced by gmarParser#character.
    def visitCharacter(self, ctx: gmarParser.CharacterContext):
        return self.visitChildren(ctx)
