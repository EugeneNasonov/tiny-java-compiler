# Generated from /home/eugene/workspace/Code/PyProjects/code_gen/gmar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gmarParser import gmarParser
else:
    from gmarParser import gmarParser

# This class defines a complete listener for a parse tree produced by gmarParser.
class gmarListener(ParseTreeListener):

    # Enter a parse tree produced by gmarParser#program.
    def enterProgram(self, ctx:gmarParser.ProgramContext):
        pass

    # Exit a parse tree produced by gmarParser#program.
    def exitProgram(self, ctx:gmarParser.ProgramContext):
        pass


    # Enter a parse tree produced by gmarParser#mainClass.
    def enterMainClass(self, ctx:gmarParser.MainClassContext):
        pass

    # Exit a parse tree produced by gmarParser#mainClass.
    def exitMainClass(self, ctx:gmarParser.MainClassContext):
        pass


    # Enter a parse tree produced by gmarParser#mainMethod.
    def enterMainMethod(self, ctx:gmarParser.MainMethodContext):
        pass

    # Exit a parse tree produced by gmarParser#mainMethod.
    def exitMainMethod(self, ctx:gmarParser.MainMethodContext):
        pass


    # Enter a parse tree produced by gmarParser#classBody.
    def enterClassBody(self, ctx:gmarParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by gmarParser#classBody.
    def exitClassBody(self, ctx:gmarParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by gmarParser#classDecl.
    def enterClassDecl(self, ctx:gmarParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by gmarParser#classDecl.
    def exitClassDecl(self, ctx:gmarParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by gmarParser#methodDecl.
    def enterMethodDecl(self, ctx:gmarParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by gmarParser#methodDecl.
    def exitMethodDecl(self, ctx:gmarParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by gmarParser#fieldDecl.
    def enterFieldDecl(self, ctx:gmarParser.FieldDeclContext):
        pass

    # Exit a parse tree produced by gmarParser#fieldDecl.
    def exitFieldDecl(self, ctx:gmarParser.FieldDeclContext):
        pass


    # Enter a parse tree produced by gmarParser#identifier.
    def enterIdentifier(self, ctx:gmarParser.IdentifierContext):
        pass

    # Exit a parse tree produced by gmarParser#identifier.
    def exitIdentifier(self, ctx:gmarParser.IdentifierContext):
        pass


    # Enter a parse tree produced by gmarParser#methodBody.
    def enterMethodBody(self, ctx:gmarParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by gmarParser#methodBody.
    def exitMethodBody(self, ctx:gmarParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by gmarParser#blockStatement.
    def enterBlockStatement(self, ctx:gmarParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by gmarParser#blockStatement.
    def exitBlockStatement(self, ctx:gmarParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by gmarParser#whileStatement.
    def enterWhileStatement(self, ctx:gmarParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by gmarParser#whileStatement.
    def exitWhileStatement(self, ctx:gmarParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by gmarParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:gmarParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by gmarParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:gmarParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by gmarParser#ifStatement.
    def enterIfStatement(self, ctx:gmarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by gmarParser#ifStatement.
    def exitIfStatement(self, ctx:gmarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by gmarParser#assignStatement.
    def enterAssignStatement(self, ctx:gmarParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by gmarParser#assignStatement.
    def exitAssignStatement(self, ctx:gmarParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by gmarParser#printStatement.
    def enterPrintStatement(self, ctx:gmarParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by gmarParser#printStatement.
    def exitPrintStatement(self, ctx:gmarParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by gmarParser#breakStatement.
    def enterBreakStatement(self, ctx:gmarParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by gmarParser#breakStatement.
    def exitBreakStatement(self, ctx:gmarParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by gmarParser#assignArrayStatement.
    def enterAssignArrayStatement(self, ctx:gmarParser.AssignArrayStatementContext):
        pass

    # Exit a parse tree produced by gmarParser#assignArrayStatement.
    def exitAssignArrayStatement(self, ctx:gmarParser.AssignArrayStatementContext):
        pass


    # Enter a parse tree produced by gmarParser#returnStatement.
    def enterReturnStatement(self, ctx:gmarParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by gmarParser#returnStatement.
    def exitReturnStatement(self, ctx:gmarParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by gmarParser#paramList.
    def enterParamList(self, ctx:gmarParser.ParamListContext):
        pass

    # Exit a parse tree produced by gmarParser#paramList.
    def exitParamList(self, ctx:gmarParser.ParamListContext):
        pass


    # Enter a parse tree produced by gmarParser#parameters.
    def enterParameters(self, ctx:gmarParser.ParametersContext):
        pass

    # Exit a parse tree produced by gmarParser#parameters.
    def exitParameters(self, ctx:gmarParser.ParametersContext):
        pass


    # Enter a parse tree produced by gmarParser#parameter.
    def enterParameter(self, ctx:gmarParser.ParameterContext):
        pass

    # Exit a parse tree produced by gmarParser#parameter.
    def exitParameter(self, ctx:gmarParser.ParameterContext):
        pass


    # Enter a parse tree produced by gmarParser#disjunctionExpression.
    def enterDisjunctionExpression(self, ctx:gmarParser.DisjunctionExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#disjunctionExpression.
    def exitDisjunctionExpression(self, ctx:gmarParser.DisjunctionExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#conjunctionExpression.
    def enterConjunctionExpression(self, ctx:gmarParser.ConjunctionExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#conjunctionExpression.
    def exitConjunctionExpression(self, ctx:gmarParser.ConjunctionExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#equalExpression.
    def enterEqualExpression(self, ctx:gmarParser.EqualExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#equalExpression.
    def exitEqualExpression(self, ctx:gmarParser.EqualExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#notEqualExpression.
    def enterNotEqualExpression(self, ctx:gmarParser.NotEqualExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#notEqualExpression.
    def exitNotEqualExpression(self, ctx:gmarParser.NotEqualExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#ltExpression.
    def enterLtExpression(self, ctx:gmarParser.LtExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#ltExpression.
    def exitLtExpression(self, ctx:gmarParser.LtExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#gtExpression.
    def enterGtExpression(self, ctx:gmarParser.GtExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#gtExpression.
    def exitGtExpression(self, ctx:gmarParser.GtExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#leExpression.
    def enterLeExpression(self, ctx:gmarParser.LeExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#leExpression.
    def exitLeExpression(self, ctx:gmarParser.LeExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#geExpression.
    def enterGeExpression(self, ctx:gmarParser.GeExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#geExpression.
    def exitGeExpression(self, ctx:gmarParser.GeExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#sumExpression.
    def enterSumExpression(self, ctx:gmarParser.SumExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#sumExpression.
    def exitSumExpression(self, ctx:gmarParser.SumExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#subtractExpression.
    def enterSubtractExpression(self, ctx:gmarParser.SubtractExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#subtractExpression.
    def exitSubtractExpression(self, ctx:gmarParser.SubtractExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#mulExpression.
    def enterMulExpression(self, ctx:gmarParser.MulExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#mulExpression.
    def exitMulExpression(self, ctx:gmarParser.MulExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#divExpression.
    def enterDivExpression(self, ctx:gmarParser.DivExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#divExpression.
    def exitDivExpression(self, ctx:gmarParser.DivExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#notExpression.
    def enterNotExpression(self, ctx:gmarParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#notExpression.
    def exitNotExpression(self, ctx:gmarParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#minusExpression.
    def enterMinusExpression(self, ctx:gmarParser.MinusExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#minusExpression.
    def exitMinusExpression(self, ctx:gmarParser.MinusExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#plusExpression.
    def enterPlusExpression(self, ctx:gmarParser.PlusExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#plusExpression.
    def exitPlusExpression(self, ctx:gmarParser.PlusExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#arraySelectExpression.
    def enterArraySelectExpression(self, ctx:gmarParser.ArraySelectExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#arraySelectExpression.
    def exitArraySelectExpression(self, ctx:gmarParser.ArraySelectExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#arrayLengthExpression.
    def enterArrayLengthExpression(self, ctx:gmarParser.ArrayLengthExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#arrayLengthExpression.
    def exitArrayLengthExpression(self, ctx:gmarParser.ArrayLengthExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#methodCallExpression.
    def enterMethodCallExpression(self, ctx:gmarParser.MethodCallExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#methodCallExpression.
    def exitMethodCallExpression(self, ctx:gmarParser.MethodCallExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#variableCallExpression.
    def enterVariableCallExpression(self, ctx:gmarParser.VariableCallExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#variableCallExpression.
    def exitVariableCallExpression(self, ctx:gmarParser.VariableCallExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#factorToAtomExpression.
    def enterFactorToAtomExpression(self, ctx:gmarParser.FactorToAtomExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#factorToAtomExpression.
    def exitFactorToAtomExpression(self, ctx:gmarParser.FactorToAtomExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#integerExpression.
    def enterIntegerExpression(self, ctx:gmarParser.IntegerExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#integerExpression.
    def exitIntegerExpression(self, ctx:gmarParser.IntegerExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#boolExpression.
    def enterBoolExpression(self, ctx:gmarParser.BoolExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#boolExpression.
    def exitBoolExpression(self, ctx:gmarParser.BoolExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#charExpression.
    def enterCharExpression(self, ctx:gmarParser.CharExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#charExpression.
    def exitCharExpression(self, ctx:gmarParser.CharExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:gmarParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:gmarParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#thisExpression.
    def enterThisExpression(self, ctx:gmarParser.ThisExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#thisExpression.
    def exitThisExpression(self, ctx:gmarParser.ThisExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#newCallExpression.
    def enterNewCallExpression(self, ctx:gmarParser.NewCallExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#newCallExpression.
    def exitNewCallExpression(self, ctx:gmarParser.NewCallExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#arrayCreateExpression.
    def enterArrayCreateExpression(self, ctx:gmarParser.ArrayCreateExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#arrayCreateExpression.
    def exitArrayCreateExpression(self, ctx:gmarParser.ArrayCreateExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#bracketExpression.
    def enterBracketExpression(self, ctx:gmarParser.BracketExpressionContext):
        pass

    # Exit a parse tree produced by gmarParser#bracketExpression.
    def exitBracketExpression(self, ctx:gmarParser.BracketExpressionContext):
        pass


    # Enter a parse tree produced by gmarParser#methodCall.
    def enterMethodCall(self, ctx:gmarParser.MethodCallContext):
        pass

    # Exit a parse tree produced by gmarParser#methodCall.
    def exitMethodCall(self, ctx:gmarParser.MethodCallContext):
        pass


    # Enter a parse tree produced by gmarParser#integral.
    def enterIntegral(self, ctx:gmarParser.IntegralContext):
        pass

    # Exit a parse tree produced by gmarParser#integral.
    def exitIntegral(self, ctx:gmarParser.IntegralContext):
        pass


    # Enter a parse tree produced by gmarParser#boolean.
    def enterBoolean(self, ctx:gmarParser.BooleanContext):
        pass

    # Exit a parse tree produced by gmarParser#boolean.
    def exitBoolean(self, ctx:gmarParser.BooleanContext):
        pass


    # Enter a parse tree produced by gmarParser#character.
    def enterCharacter(self, ctx:gmarParser.CharacterContext):
        pass

    # Exit a parse tree produced by gmarParser#character.
    def exitCharacter(self, ctx:gmarParser.CharacterContext):
        pass


    # Enter a parse tree produced by gmarParser#vartype.
    def enterVartype(self, ctx:gmarParser.VartypeContext):
        pass

    # Exit a parse tree produced by gmarParser#vartype.
    def exitVartype(self, ctx:gmarParser.VartypeContext):
        pass


    # Enter a parse tree produced by gmarParser#integralType.
    def enterIntegralType(self, ctx:gmarParser.IntegralTypeContext):
        pass

    # Exit a parse tree produced by gmarParser#integralType.
    def exitIntegralType(self, ctx:gmarParser.IntegralTypeContext):
        pass


    # Enter a parse tree produced by gmarParser#integralArrayType.
    def enterIntegralArrayType(self, ctx:gmarParser.IntegralArrayTypeContext):
        pass

    # Exit a parse tree produced by gmarParser#integralArrayType.
    def exitIntegralArrayType(self, ctx:gmarParser.IntegralArrayTypeContext):
        pass


    # Enter a parse tree produced by gmarParser#characterType.
    def enterCharacterType(self, ctx:gmarParser.CharacterTypeContext):
        pass

    # Exit a parse tree produced by gmarParser#characterType.
    def exitCharacterType(self, ctx:gmarParser.CharacterTypeContext):
        pass


    # Enter a parse tree produced by gmarParser#booleanType.
    def enterBooleanType(self, ctx:gmarParser.BooleanTypeContext):
        pass

    # Exit a parse tree produced by gmarParser#booleanType.
    def exitBooleanType(self, ctx:gmarParser.BooleanTypeContext):
        pass


