from antlr4 import *
from MathLexer import MathLexer
from MathParser import MathParser
from MathListener import MathListener
import math

class MathEvaluator(MathListener):
    def __init__(self):
        self.stack = []
        self.current_matrix = None
        self.current_row = None

    def exitNUMBER(self, ctx):
        self.stack.append(float(ctx.getText()))

    def exitVARIABLE(self, ctx):
        # For now, we'll just use a simple variable mapping
        self.stack.append(0.0)  # Default value for variables

    def exitFunction(self, ctx):
        # Handle NUMBER
        if ctx.NUMBER():
            self.stack.append(float(ctx.NUMBER().getText()))
            return
        # Handle VARIABLE
        if ctx.VARIABLE():
            self.stack.append(0.0)  # Default value for variables
            return

        if ctx.getChildCount() == 2:  # Unary operations
            if ctx.getChild(0).getText() == '-':
                self.stack.append(-self.stack.pop())
            elif ctx.getChild(0).getText() == 'exp':
                self.stack.append(math.exp(self.stack.pop()))
            elif ctx.getChild(0).getText() == 'sqrt':
                self.stack.append(math.sqrt(self.stack.pop()))
            elif ctx.getChild(0).getText() == 'sin':
                self.stack.append(math.sin(self.stack.pop()))
            elif ctx.getChild(0).getText() == 'cos':
                self.stack.append(math.cos(self.stack.pop()))
            elif ctx.getChild(0).getText() == 'tan':
                self.stack.append(math.tan(self.stack.pop()))
            elif ctx.getChild(0).getText() == 'log':
                self.stack.append(math.log(self.stack.pop()))
        elif ctx.getChildCount() == 3:  # Binary operations
            right = self.stack.pop()
            left = self.stack.pop()
            op = ctx.getChild(1).getText()
            if op == '+':
                self.stack.append(left + right)
            elif op == '-':
                self.stack.append(left - right)
            elif op == '*':
                self.stack.append(left * right)
            elif op == '/':
                self.stack.append(left / right)
            elif op == '**':
                self.stack.append(left ** right)

    # Matrix handling
    def enterMatrix(self, ctx):
        self.current_matrix = []

    def exitMatrix(self, ctx):
        if self.current_matrix is not None:
            self.stack.append(self.current_matrix)
            self.current_matrix = None

    def enterRow(self, ctx):
        self.current_row = []

    def exitRow(self, ctx):
        if self.current_row is not None:
            if self.current_matrix is not None:
                self.current_matrix.append(self.current_row)
            else:
                self.stack.append(self.current_row)
            self.current_row = None

    def exitElement(self, ctx):
        if ctx.NUMBER():
            value = float(ctx.NUMBER().getText())
            if self.current_row is not None:
                self.current_row.append(value)
            else:
                self.stack.append(value)
        elif ctx.row():
            # For nested matrices, the row is already added to current_matrix
            pass

def evaluate_expression(expression):
    input_stream = InputStream(expression)
    lexer = MathLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MathParser(token_stream)
    tree = parser.program()
    evaluator = MathEvaluator()
    walker = ParseTreeWalker()
    walker.walk(evaluator, tree)
    return evaluator.stack[0] if evaluator.stack else None

if __name__ == "__main__":
    test_expressions = [
        "2 + 3",
        "2 * (3 + 4)",
        "sin(0)",
        "exp(1)",
        "sqrt(16)",
        "log(10)",
        # "[[1,2],[3,4]]"  # Matrix test
        "[[(-1),(-2)],[3,(-4)]]" # Matrix with negative numbers test
    ]
    for expr in test_expressions:
        try:
            result = evaluate_expression(expr)
            print(f"Expression: {expr}")
            print(f"Result: {result}\n")
        except Exception as e:
            print(f"Error evaluating {expr}: {str(e)}\n") 