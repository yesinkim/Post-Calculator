import unittest

from calculator import LexicalAnalyzer
from exception import ExpressionError, ParenthesesError

# unittest example
# https://docs.python.org/ko/3/library/unittest.html


class TestExpression(unittest.TestCase):
    # def setUp(self):
    #     print("*==== test를 시작합니다.. ====*")

    def test_wrong_expression(self):
        ex = "333+"
        ex2 = ")3 * 4"
        with self.assertRaises(ExpressionError):
            LexicalAnalyzer(ex).check_expression()
            LexicalAnalyzer(ex2).check_expression()

    
    def parentheses_error(self):
        ex = "2.7 - (2 )-1)+(2"
        with self.assertRaises(ParenthesesError):
            LexicalAnalyzer(ex).check_expression()




if __name__ == '__main__':
    unittest.main()
