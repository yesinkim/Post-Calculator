"""test 항목 (내가 원하는 기능이 원하는 목적을 달성하는 지 확인하는 것)
1. 올바른 수식을 잘 파싱하는 지
1.1. 올바른 수식이 들어가지 않았을 때 적절한 에러가 나는 지 (예외 case가 부족 -> 다다익선!) 
    예를들면 아무것도 없는 것. 
2. 수식을 파싱하는 지
3. 수식을 계산하는 지

한 가지 test에 한 가지 
"""
import unittest

from calculate_parser import CalculatorParser
from exceptions import InvalidExpression
from tokens import NumberToken, OperatorToken


class ParserTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ParserTest, self).__init__(*args, **kwargs)
        self.parser = CalculatorParser()
        self.sample = ["1+2", "1-1", "1*2", "1 /2 ", "(1.2+1)* 2 / 3 - 3"]
    
    def test_raise_error(self):
        operator_error = ["1+2+", "1+*2"]
        point_error = ['.3']
        with self.assertRaises(InvalidExpression):
            for case in operator_error:
                self.parser.tokenize(case)

        with self.assertRaises(ZeroDivisionError):
            self.parser.parse(1/0)

    def test_tokenize(self):
        # token별로 분리
        self.assertEqual(self.parser.tokenize("9")[0].token_type, "Number")
        self.assertEqual(self.parser.tokenize("9")[0].value, "9")
        self.assertEqual(self.parser.tokenize("+")[0].token_type, "Plus")
        self.assertEqual(self.parser.tokenize("-")[0].token_type, "Minus")
        self.assertEqual(self.parser.tokenize("*")[0].token_type, "Multiply")
        self.assertEqual(self.parser.tokenize("/")[0].token_type, "Divide")
        self.assertEqual(self.parser.tokenize('1+2'), [NumberToken("1"), OperatorToken("+"), NumberToken("2")])

    def test_calculate(self):
        # 기능별로 test를 자세하게 구현
        self.assertEqual(self.parser.parse('1+2').evaluate(), 3)
        self.assertEqual(self.parser.parse('1-1').evaluate(), 0)
        self.assertEqual(self.parser.parse('1*2').evaluate(), 2)
        self.assertEqual(self.parser.parse('1/2').evaluate(), 0.5)
        self.assertEqual(round(self.parser.parse('(1.2+1)*2/3-3').evaluate(),1), -1.5)

    def test_add(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)