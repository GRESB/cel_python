import antlr4
from .parser.CELLexer import CELLexer
from .parser.CELParser import CELParser
from .context import Context
from .type_checker import TypeChecker
from .interpreter import Interpreter
from .error_collector import ErrorCollector
from antlr4.error.ErrorListener import ErrorListener
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Runtime:
    def __init__(self, cel_expression: str):
        self.cel_expression = cel_expression
        self.ast = None
        self.errors = []

        try:
            input_stream = antlr4.InputStream(cel_expression)
            lexer = CELLexer(input_stream)
            tokens = antlr4.CommonTokenStream(lexer)
            parser = CELParser(tokens)
            parser.buildParseTrees = True

            # Remove default error listeners and add custom ErrorCollector
            parser.removeErrorListeners()
            error_collector = ErrorCollector()
            parser.addErrorListener(error_collector)

            # Parse the expression
            self.ast = parser.start()
            logger.debug(f"AST: {self.ast.toStringTree(recog=parser)}")  # Log the AST

            # If there are errors, collect them and invalidate the AST
            if error_collector.errors:
                self.errors = error_collector.errors
                self.ast = None
                logger.error(f"Parsing failed with errors: {self.errors}")

        except Exception as e:
            # Catch any unexpected parsing exceptions
            self.ast = None
            self.errors.append({
                'line': 0,
                'column': 0,
                'message': str(e),
                'offendingSymbol': None
            })
            logger.exception("Exception during parsing")

    @staticmethod
    def can_parse(cel_expression: str) -> bool:
        runtime = Runtime(cel_expression)
        return runtime.ast is not None

    @staticmethod
    def parse_string(cel_expression: str) -> dict:
        runtime = Runtime(cel_expression)
        if runtime.ast is not None:
            return {"success": True}
        else:
            error_msg = runtime.errors[0]['message'] if runtime.errors else "Parsing failed with errors"
            return {
                "success": False,
                "error": error_msg
            }

    @staticmethod
    def type_check(expression: str, context_vars=None, types=None) -> dict:
        runtime = Runtime(expression)
        if runtime.ast is not None:
            try:
                context = Context(context_vars or {}, types or {})
                type_checker = TypeChecker(context)
                type_checker.visit(runtime.ast)
                logger.debug("Type checking succeeded")
                return {"success": True}
            except Exception as e:
                logger.error(f"Type checking failed: {str(e)}")
                return {"success": False, "error": str(e)}
        else:
            error_message = runtime.errors[0]['message'] if runtime.errors else "Parsing failed with errors"
            logger.error(f"Type checking failed: {error_message}")
            return {"success": False, "error": error_message}

    def evaluate(self, context_vars=None, types=None):
        if not self.ast:
            raise ValueError("AST is not available. Parsing might have failed.")
        context = Context(context_vars or {}, types or {})
        type_check_result = Runtime.type_check(self.cel_expression, context_vars, types)
        if type_check_result["success"]:
            interpreter = Interpreter(context)
            result = interpreter.visit(self.ast)
            logger.debug(f"Evaluation result: {result}")
            return result
        else:
            raise TypeError(type_check_result["error"])
