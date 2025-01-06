from antlr4.error.ErrorListener import ErrorListener

class ErrorCollector(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error = {
            'line': line,
            'column': column,
            'message': msg,
            'offendingSymbol': offendingSymbol.text if offendingSymbol else None
        }
        self.errors.append(error)
