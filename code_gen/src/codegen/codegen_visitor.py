from src.autogen.gmarVisitor import gmarVisitor
from src.autogen.gmarParser import gmarParser
from src.codegen.class_file import ClassFile
from src.codegen.instruction import Instruction
from src.codegen.method import Method
from src.symbol_table.method_record import MethodRecord
from .config import *


class CodeGenerationVisitor(gmarVisitor):
    def __init__(self, table):
        self.symbol_table = table
        self.current_method = None
        self.current_class = ''
        self.class_file = None
        self.field_declaration = False

    # Visit a parse tree produced by gmarParser#program.
    def visitProgram(self, ctx: gmarParser.ProgramContext):
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))

    # Visit a parse tree produced by gmarParser#mainClass.
    def visitMainClass(self, ctx: gmarParser.MainClassContext):
        self.current_class = ctx.getChild(1).getText()
        self.class_file = ClassFile()
        self.symbol_table.enter_scope()
        self.visit(ctx.getChild(3))
        self.symbol_table.exit_scope()
        self.current_method.add_instruction(Instruction(STOP, None))

    # Visit a parse tree produced by gmarParser#mainMethod.
    def visitMainMethod(self, ctx: gmarParser.MainMethodContext):
        method_name = ctx.getChild(3).getText()
        method_record = self.symbol_table.lookup(method_name)
        if method_record is None:
            print("error on method")
            exit(0)
        self.current_method = Method()
        self.symbol_table.enter_scope()
        self.visit(ctx.getChild(11))
        self.symbol_table.exit_scope()
        self.class_file.add_method(f"{self.current_class}.{method_name}", self.current_method)

    # Visit a parse tree produced by gmarParser#classDecl.
    def visitClassDecl(self, ctx: gmarParser.ClassDeclContext):
        self.current_class = ctx.getChild(1).getText()
        self.symbol_table.enter_scope()
        self.visit(ctx.getChild(3))
        self.symbol_table.exit_scope()

    # Visit a parse tree produced by gmarParser#methodDecl.
    def visitMethodDecl(self, ctx: gmarParser.MethodDeclContext):
        method_name = ctx.getChild(1).getText()
        method_record: MethodRecord = self.symbol_table.lookup(method_name)
        if method_name is None:
            print("error 1")
            exit(0)
        self.current_method = Method()
        self.current_method.variables = method_record.get_local_variables()
        self.symbol_table.enter_scope()
        self.visit(ctx.getChild(3))
        self.visit(ctx.getChild(6))
        self.symbol_table.exit_scope()
        self.class_file.add_method(f'{self.current_class}.{method_name}', self.current_method)

    # Visit a parse tree produced by gmarParser#fieldDecl.
    def visitFieldDecl(self, ctx: gmarParser.FieldDeclContext):
        self.field_declaration = True
        self.visit(ctx.getChild(0))
        self.field_declaration = False

    # Visit a parse tree produced by gmarParser#whileStatement.
    def visitWhileStatement(self, ctx: gmarParser.WhileStatementContext):
        whilelabel = self.current_method.get_index()
        self.visit(ctx.getChild(2))
        iffalse = self.current_method.get_index()
        self.current_method.add_instruction(Instruction(IF_FALSE, None))
        self.visit(ctx.getChild(4))
        instr = self.current_method.get_instruction(iffalse)
        instr.argument = self.current_method.get_index() + 1

        gotolabel = self.current_method.get_index()
        self.current_method.add_instruction(Instruction(GOTO, None))
        instr = self.current_method.get_instruction(gotolabel)
        instr.argument = whilelabel

    def visitDoWhileStatement(self, ctx:gmarParser.DoWhileStatementContext):
        beginbody = self.current_method.get_index()
        self.visit(ctx.getChild(1))
        self.visit(ctx.getChild(4))
        iffalse = self.current_method.get_index()
        self.current_method.add_instruction(Instruction(IF_FALSE, iffalse + 2))
        self.current_method.add_instruction(Instruction(GOTO, beginbody))

    # Visit a parse tree produced by gmarParser#ifStatement.
    def visitIfStatement(self, ctx: gmarParser.IfStatementContext):
        self.visit(ctx.getChild(2))
        iflabel = self.current_method.get_index()
        self.current_method.add_instruction(Instruction(IF_FALSE, None))
        self.visit(ctx.getChild(4))
        instr = self.current_method.get_instruction(iflabel)
        instr.argument = self.current_method.get_index() + 1

        gotolabel = self.current_method.get_index()
        self.current_method.add_instruction(Instruction(GOTO, None))
        if ctx.getChild(6) is not None:
            self.visit(ctx.getChild(6))
            instr = self.current_method.get_instruction(gotolabel)
            instr.argument = self.current_method.get_index()

    # Visit a parse tree produced by gmarParser#assignStatement.
    def visitAssignStatement(self, ctx: gmarParser.AssignStatementContext):
        lhs = ctx.getChild(0).getText()
        self.visit(ctx.getChild(2))
        index = self.current_method.get_index_of(lhs)
        self.current_method.add_instruction(Instruction(ISTORE, index))

    # Visit a parse tree produced by gmarParser#printStatement.
    def visitPrintStatement(self, ctx: gmarParser.PrintStatementContext):
        self.visit(ctx.getChild(2))
        self.current_method.add_instruction(Instruction(PRINT, None))

    # Visit a parse tree produced by gmarParser#returnStatement.
    def visitReturnStatement(self, ctx: gmarParser.ReturnStatementContext):
        self.visit(ctx.getChild(1))
        self.current_method.add_instruction(Instruction(IRETURN, None))

    # Visit a parse tree produced by gmarParser#parameters.
    def visitParameters(self, ctx: gmarParser.ParametersContext):
        params = ctx.getChildCount()
        i = params - 1
        while i >= 0:
            self.visit(ctx.getChild(i))
            i -= 2

    # Visit a parse tree produced by gmarParser#parameter.
    def visitParameter(self, ctx: gmarParser.ParameterContext):
        num_children = ctx.getChildCount()
        vname = str(ctx.getChild(1).getChild(0))
        index = self.current_method.get_index_of(vname)
        self.current_method.add_instruction(Instruction(ISTORE, index))

    # Visit a parse tree produced by gmarParser#conjuctionExpression.
    def visitConjunctionExpression(self, ctx: gmarParser.ConjunctionExpressionContext):
        num_cildren = ctx.getChildCount()
        self.visit(ctx.getChild(0))
        i = 2
        while i < num_cildren:
            self.visit(ctx.getChild(i))
            self.current_method.add_instruction(Instruction(IAND, None))
            i += 2

    # Visit a parse tree produced by gmarParser#conjuctionExpression.
    def visitDisjuntionExpression(self, ctx: gmarParser.DisjunctionExpressionContext):
        num_cildren = ctx.getChildCount()
        self.visit(ctx.getChild(0))
        i = 2
        while i < num_cildren:
            self.visit(ctx.getChild(i))
            self.current_method.add_instruction(Instruction(IOR, None))
            i += 2

    # Visit a parse tree produced by gmarParser#methodCallExpression.
    def visitMethodCallExpression(self, ctx: gmarParser.MethodCallExpressionContext):
        numchi = ctx.getChildCount()
        invclassname = ''
        if ctx.getChild(0).getChild(0).getText() == 'this':
            invclassname = self.current_class
        else:
            # print(ctx.getText())
            invclassname = str(ctx.getChild(0).getChild(1).getChild(0))
        paramnum = ctx.getChild(numchi - 1).getChildCount() - 3
        i = 0
        while i < paramnum:
            self.visit(ctx.getChild(numchi - 1).getChild(i + 2))
            i += 2
        imn = str(ctx.getChild(2).getChild(0).getChild(0))
        self.current_method.add_instruction(Instruction(INVOKEVIRTUAL, f'{invclassname}.{imn}'))

    # Visit a parse tree produced by gmarParser#equalExpression.
    def visitEqualExpression(self, ctx: gmarParser.EqualExpressionContext):
        num_cildren = ctx.getChildCount()
        self.visit(ctx.getChild(0))
        i = 2
        while i < num_cildren:
            self.visit(ctx.getChild(i))
            self.current_method.add_instruction(Instruction(IEQ, None))
            i += 2

    # Visit a parse tree produced by gmarParser#notEqualExpression.
    def visitNotEqualExpression(self, ctx: gmarParser.NotEqualExpressionContext):
        num_cildren = ctx.getChildCount()
        self.visit(ctx.getChild(0))
        i = 2
        while i < num_cildren:
            self.visit(ctx.getChild(i))
            self.current_method.add_instruction(Instruction(IEQ, None))
            self.current_method.add_instruction(Instruction(INOT, None))
            i += 2

    # Visit a parse tree produced by gmarParser#ltExpression.
    def visitLtExpression(self, ctx: gmarParser.LtExpressionContext):
        num_cildren = ctx.getChildCount()
        self.visit(ctx.getChild(0))
        i = 2
        while i < num_cildren:
            self.visit(ctx.getChild(i))
            self.current_method.add_instruction(Instruction(ILT, None))
            i += 2

    # Visit a parse tree produced by gmarParser#gtExpression.
    def visitGtExpression(self, ctx: gmarParser.GtExpressionContext):
        num_cildren = ctx.getChildCount()
        self.visit(ctx.getChild(0))
        i = 2
        while i < num_cildren:
            self.visit(ctx.getChild(i))
            self.current_method.add_instruction(Instruction(ILE, None))
            self.current_method.add_instruction(Instruction(INOT, None))
            i += 2

    # Visit a parse tree produced by gmarParser#leExpression.
    def visitLeExpression(self, ctx: gmarParser.LeExpressionContext):
        num_cildren = ctx.getChildCount()
        self.visit(ctx.getChild(0))
        i = 2
        while i < num_cildren:
            self.visit(ctx.getChild(i))
            self.current_method.add_instruction(Instruction(ILE, None))
            i += 2

    # Visit a parse tree produced by gmarParser#geExpression.
    def visitGeExpression(self, ctx: gmarParser.GeExpressionContext):
        num_cildren = ctx.getChildCount()
        self.visit(ctx.getChild(0))
        i = 2
        while i < num_cildren:
            self.visit(ctx.getChild(i))
            self.current_method.add_instruction(Instruction(IGE, None))
            i += 2

    # Visit a parse tree produced by gmarParser#sumExpression.
    def visitSumExpression(self, ctx: gmarParser.SumExpressionContext):
        num_cildren = ctx.getChildCount()
        self.visit(ctx.getChild(0))
        i = 2
        while i < num_cildren:
            self.visit(ctx.getChild(i))
            self.current_method.add_instruction(Instruction(IADD, None))
            i += 2

    # Visit a parse tree produced by gmarParser#subtractExpression.
    def visitSubtractExpression(self, ctx: gmarParser.SubtractExpressionContext):
        num_cildren = ctx.getChildCount()
        self.visit(ctx.getChild(0))
        i = 2
        while i < num_cildren:
            self.visit(ctx.getChild(i))
            self.current_method.add_instruction(Instruction(ISUB, None))
            i += 2

    # Visit a parse tree produced by gmarParser#mulExpression.
    def visitMulExpression(self, ctx: gmarParser.MulExpressionContext):
        num_cildren = ctx.getChildCount()
        self.visit(ctx.getChild(0))
        i = 2
        while i < num_cildren:
            self.visit(ctx.getChild(i))
            self.current_method.add_instruction(Instruction(IMUL, None))
            i += 2

    # Visit a parse tree produced by gmarParser#divExpression.
    def visitDivExpression(self, ctx: gmarParser.DivExpressionContext):
        num_cildren = ctx.getChildCount()
        self.visit(ctx.getChild(0))
        i = 2
        while i < num_cildren:
            self.visit(ctx.getChild(i))
            self.current_method.add_instruction(Instruction(IDIV, None))
            i += 2

    # Visit a parse tree produced by gmarParser#notExpression.
    def visitNotExpression(self, ctx: gmarParser.NotExpressionContext):
        self.visit(ctx.getChild(1))
        self.current_method.add_instruction(Instruction(INOT, None))

    # Visit a parse tree produced by gmarParser#minusExpression.
    def visitMinusExpression(self, ctx: gmarParser.MinusExpressionContext):
        pass

    # Visit a parse tree produced by gmarParser#plusExpression.
    def visitPlusExpression(self, ctx: gmarParser.PlusExpressionContext):
        pass

    # Visit a parse tree produced by gmarParser#factorToAtomExpression.
    def visitFactorToAtomExpression(self, ctx: gmarParser.FactorToAtomExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gmarParser#identifierExpression.
    def visitIdentifier(self, ctx: gmarParser.IdentifierContext):
        index = self.current_method.get_index_of(ctx.getText())
        self.current_method.add_instruction(Instruction(ILOAD, index))

    # Visit a parse tree produced by gmarParser#integral.
    def visitIntegral(self, ctx: gmarParser.IntegralContext):
        if not self.field_declaration:
            value = int(str(ctx.getChild(0)))
            self.current_method.add_instruction(Instruction(ICONST, value))
