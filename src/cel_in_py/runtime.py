import sys
from antlr4 import *
from .parser.CELLexer import CELLexer
from .parser.CELParser import CELParser
from .parser.CELListener import CELListener
from .visitor_interp import VisitorInterp

class Runtime:
    def __init__(self, cel_expression):
        input_stream = InputStream(cel_expression)
        lexer = CELLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = CELParser(token_stream)

        parser.removeErrorListeners()
        error_listener = CELListener()
        parser.addErrorListener(error_listener)

        try:
            self.ast = parser.start()
        except Exception as e:
            print(f"Parsing failed: {e}")
            self.ast = None

    @staticmethod
    def can_parse(cel_expression):
        try:
            runtime = Runtime(cel_expression)
            return runtime.ast is not None
        except Exception:
            return False

    @staticmethod
    def parse_string(cel_expression):
        try:
            runtime = Runtime(cel_expression)
            if runtime.ast is not None:
                return {"success": True}
            else:
                return {"success": False, "error": "Parsing failed without an exception"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def evaluate(self, context):
        if not self.ast:
            raise Exception("AST is not available. Parsing might have failed.")
        visitor = VisitorInterp(context)
        return visitor.visit(self.ast)
