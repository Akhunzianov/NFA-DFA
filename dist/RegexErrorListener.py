from antlr4.error.ErrorListener import ErrorListener

class RegexErrorListener(ErrorListener):
    def __init__(self):
        super(RegexErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Syntax error at line {line}, column {column}: {msg}"
        self.errors.append(error_message)