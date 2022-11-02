import re

class LexicalAnalyzer:
    """Find wrong expression and change expression to postfix"""

    def __init__(self, expression=None):
        """Initialize LexicalAnalyzer

        Args:
            expression (str): expression to calculate
        """
        self.expression = expression if expression else self.get_expression()
        self.check_expression()

    def get_expression(self):
        """get expression from user"""
        self.expression = input("Enter an expression: ").replace(" ", "")
        return self.expression

    def tokenize(self):
        """tokenize expression

        Returns:
            list: tokenized expression list contains operand and operator objects
        """
        expr = re.findall(r"[0-9.]+|[\+\-\*\/\(\)]", self.expression)
        
