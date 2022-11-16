"""test 항목
1. 올바른 수식을 잘 파싱하는 지
1.1. 올바른 수식이 들어가지 않았을 때 적절한 에러가 나는 지
2. 수식을 파싱하는 지
3. 수식을 계산하는 지
"""
import unittest

from parser import CalculatorParser
from exceptions import InvalidExpressionError


class Test(unittest.TestCase):
    # def __init__(self):
    #     self.parser = CalculatorParser()
    #     self.sample = ["1+2", "1-1", "1+2", "1/2", "(1.2+1)*2)/3-3"]
    
    
    def test_raise_error(self):
        parser = CalculatorParser()
        with self.assertRaises(InvalidExpressionError):
            parser.parse('1+*2')
            parser.parse('1+2+')
            parser.parse('0.1+2+3+')

    def test_tokenize(self):
        parser = CalculatorParser()
        self.assertEqual(parser.tokenize('1+2'), '[NumberToken(type=Number, value=1), OperatorToken(type=Add, value=+), NumberToken(type=Number, value=2)]')


if __name__ == '__main__':
    unittest.main(verbosity=2)