# Generated from /home/eugene/workspace/Code/PyProjects/code_gen/gmar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gmarParser import gmarParser
else:
    from gmarParser import gmarParser

# This class defines a complete generic visitor for a parse tree produced by gmarParser.

class gmarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gmarParser#program.
    def visitProgram(self, ctx:gmarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#mainClass.
    def visitMainClass(self, ctx:gmarParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#mainMethod.
    def visitMainMethod(self, ctx:gmarParser.MainMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#classBody.
    def visitClassBody(self, ctx:gmarParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#classDecl.
    def visitClassDecl(self, ctx:gmarParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#methodDecl.
    def visitMethodDecl(self, ctx:gmarParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#fieldDecl.
    def visitFieldDecl(self, ctx:gmarParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#identifier.
    def visitIdentifier(self, ctx:gmarParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#methodBody.
    def visitMethodBody(self, ctx:gmarParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#blockStatement.
    def visitBlockStatement(self, ctx:gmarParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#whileStatement.
    def visitWhileStatement(self, ctx:gmarParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:gmarParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#ifStatement.
    def visitIfStatement(self, ctx:gmarParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#assignStatement.
    def visitAssignStatement(self, ctx:gmarParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#printStatement.
    def visitPrintStatement(self, ctx:gmarParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#breakStatement.
    def visitBreakStatement(self, ctx:gmarParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#assignArrayStatement.
    def visitAssignArrayStatement(self, ctx:gmarParser.AssignArrayStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#returnStatement.
    def visitReturnStatement(self, ctx:gmarParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#paramList.
    def visitParamList(self, ctx:gmarParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#parameters.
    def visitParameters(self, ctx:gmarParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#parameter.
    def visitParameter(self, ctx:gmarParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#disjunctionExpression.
    def visitDisjunctionExpression(self, ctx:gmarParser.DisjunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#conjunctionExpression.
    def visitConjunctionExpression(self, ctx:gmarParser.ConjunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#equalExpression.
    def visitEqualExpression(self, ctx:gmarParser.EqualExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#notEqualExpression.
    def visitNotEqualExpression(self, ctx:gmarParser.NotEqualExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#ltExpression.
    def visitLtExpression(self, ctx:gmarParser.LtExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#gtExpression.
    def visitGtExpression(self, ctx:gmarParser.GtExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#leExpression.
    def visitLeExpression(self, ctx:gmarParser.LeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#geExpression.
    def visitGeExpression(self, ctx:gmarParser.GeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#sumExpression.
    def visitSumExpression(self, ctx:gmarParser.SumExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#subtractExpression.
    def visitSubtractExpression(self, ctx:gmarParser.SubtractExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#mulExpression.
    def visitMulExpression(self, ctx:gmarParser.MulExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#divExpression.
    def visitDivExpression(self, ctx:gmarParser.DivExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#notExpression.
    def visitNotExpression(self, ctx:gmarParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#minusExpression.
    def visitMinusExpression(self, ctx:gmarParser.MinusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#plusExpression.
    def visitPlusExpression(self, ctx:gmarParser.PlusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#arraySelectExpression.
    def visitArraySelectExpression(self, ctx:gmarParser.ArraySelectExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#arrayLengthExpression.
    def visitArrayLengthExpression(self, ctx:gmarParser.ArrayLengthExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#methodCallExpression.
    def visitMethodCallExpression(self, ctx:gmarParser.MethodCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#variableCallExpression.
    def visitVariableCallExpression(self, ctx:gmarParser.VariableCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#factorToAtomExpression.
    def visitFactorToAtomExpression(self, ctx:gmarParser.FactorToAtomExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#integerExpression.
    def visitIntegerExpression(self, ctx:gmarParser.IntegerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#boolExpression.
    def visitBoolExpression(self, ctx:gmarParser.BoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#charExpression.
    def visitCharExpression(self, ctx:gmarParser.CharExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:gmarParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#thisExpression.
    def visitThisExpression(self, ctx:gmarParser.ThisExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#newCallExpression.
    def visitNewCallExpression(self, ctx:gmarParser.NewCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#arrayCreateExpression.
    def visitArrayCreateExpression(self, ctx:gmarParser.ArrayCreateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#bracketExpression.
    def visitBracketExpression(self, ctx:gmarParser.BracketExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#methodCall.
    def visitMethodCall(self, ctx:gmarParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#integral.
    def visitIntegral(self, ctx:gmarParser.IntegralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#boolean.
    def visitBoolean(self, ctx:gmarParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#character.
    def visitCharacter(self, ctx:gmarParser.CharacterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#vartype.
    def visitVartype(self, ctx:gmarParser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#integralType.
    def visitIntegralType(self, ctx:gmarParser.IntegralTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#integralArrayType.
    def visitIntegralArrayType(self, ctx:gmarParser.IntegralArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#characterType.
    def visitCharacterType(self, ctx:gmarParser.CharacterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gmarParser#booleanType.
    def visitBooleanType(self, ctx:gmarParser.BooleanTypeContext):
        return self.visitChildren(ctx)



del gmarParser