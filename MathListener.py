# Generated from Math.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MathParser import MathParser
else:
    from MathParser import MathParser

# This class defines a complete listener for a parse tree produced by MathParser.
class MathListener(ParseTreeListener):

    # Enter a parse tree produced by MathParser#program.
    def enterProgram(self, ctx:MathParser.ProgramContext):
        pass

    # Exit a parse tree produced by MathParser#program.
    def exitProgram(self, ctx:MathParser.ProgramContext):
        pass


    # Enter a parse tree produced by MathParser#expression.
    def enterExpression(self, ctx:MathParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MathParser#expression.
    def exitExpression(self, ctx:MathParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MathParser#function.
    def enterFunction(self, ctx:MathParser.FunctionContext):
        pass

    # Exit a parse tree produced by MathParser#function.
    def exitFunction(self, ctx:MathParser.FunctionContext):
        pass


    # Enter a parse tree produced by MathParser#matrix.
    def enterMatrix(self, ctx:MathParser.MatrixContext):
        pass

    # Exit a parse tree produced by MathParser#matrix.
    def exitMatrix(self, ctx:MathParser.MatrixContext):
        pass


    # Enter a parse tree produced by MathParser#row.
    def enterRow(self, ctx:MathParser.RowContext):
        pass

    # Exit a parse tree produced by MathParser#row.
    def exitRow(self, ctx:MathParser.RowContext):
        pass


    # Enter a parse tree produced by MathParser#element.
    def enterElement(self, ctx:MathParser.ElementContext):
        pass

    # Exit a parse tree produced by MathParser#element.
    def exitElement(self, ctx:MathParser.ElementContext):
        pass



del MathParser