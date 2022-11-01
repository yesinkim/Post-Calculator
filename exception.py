class ExpressionError(Exception):
    pass

class ParenthesesError(ExpressionError):
    pass

class OperatorError(ExpressionError):
    pass

class OperandError(ExpressionError):
    pass