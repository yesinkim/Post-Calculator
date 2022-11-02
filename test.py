import unittest

from calculator import LexicalAnalyzer, calculate
from tokens import Operand, Operator
from exception import ExpressionError, ParenthesesError, OperatorError, OperandError

# unittest example
# https://docs.python.org/ko/3/library/unittest.html
class TestExpression(unittest.TestCase):
    # 함수명은 꼭 test로 시작해야 함 (신기하네요)
    def test_wrong_expression(self):
        ex = "333+"
        ex2 = ")3 s* 4"
        ex3 = "2^3"
        with self.assertRaises(ExpressionError):
            LexicalAnalyzer(ex)
            LexicalAnalyzer(ex2)
            LexicalAnalyzer(ex3)

    def test_parentheses_error(self):
        ex = "2.7-(2)+1)+(2"
        ex2 = "(1+2"
        with self.assertRaises(ParenthesesError):
            LexicalAnalyzer(ex)
            LexicalAnalyzer(ex2)

    def test_operator_error(self):
        ex = "2.7 *- 3"
        with self.assertRaises(OperatorError):
            LexicalAnalyzer(ex)

    def test_to_postfix(self):
        ex = "2.4 + 3 * 2"
        post = [Operand("2.4"), Operand("3"), Operand("2"), Operator("*"), Operator("+")]
        self.assertEqual(LexicalAnalyzer(ex).to_postfix(), post)

    def test_calculate(self):
        ex = "2.4 + 03 * 2"
        self.assertEqual(calculate(LexicalAnalyzer(ex).to_postfix()), Operand(8.4))

    def test_zero_division_error(self):
        ex = "2 / 0"
        with self.assertRaises(ZeroDivisionError):
            calculate(calculate(LexicalAnalyzer(ex).to_postfix()))

    def test_operand_error(self):
        ex = "2..3"
        with self.assertRaises(OperandError):
            LexicalAnalyzer(ex)






if __name__ == '__main__':
    unittest.main(verbosity=2)




"""
# Error list
# 1. 
Traceback (most recent call last):
  File "/Users/yeshinkim/Post_Calculator/test.py", line 74, in test_calculate
    self.assertEqual(calculate(LexicalAnalyzer(ex).to_postfix()), Operand(8.4))
AssertionError: 8.4 != 8.4
> 메모리 주소로 같은지를 판별하는 건가? 아닌듯> 
__eq__를 정의해주지 않아서 그럼

# 2.
======================================================================
FAIL: test_calculate (__main__.TestExpression)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/yeshinkim/Post_Calculator/test.py", line 73, in test_calculate
    self.assertEqual(calculate(LexicalAnalyzer(ex).to_postfix()), Operand("8.4"))
AssertionError: <tokens.Operand object at 0x101e39be0> != 8.4

----------------------------------------------------------------------
class와 8.4를 비교해줘서 -> class로 바꾸고, __eq__ 정의했더니 해결 됨.
"""