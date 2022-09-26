"""
Object: infix로 표기되어 있는 식을 입력 받을 수 있는 인터페이스와 입력 받은 식을 계산하는 함수를 개발 
Input: infix로 표기되어 있는 식
Output: 계산 결과

구현 해야 하는 것
1. Lexical Analyzer?
-> 입력을 어떻게 받지??? (input)
2. Postfix Calculator
-> 입력 받은 식을 postfix로 변환 및 계산해서 output

연산자(Operator)와 피연산자(Operand)는 모두 Class로 구현되어야 함.
# 고려해야하는 연산자 (+, -, *,  /,  ( , ) )
# 1. 괄호
# 2. 곱셈, 나눗셈
# 3. 덧셈, 뺄셈
# 4. 연산자를 기준으로 왼쪽계산
"""

# expression = input("Enter an expression: ")
test_expession = "* 2 3 + 4 5"
test_expession2 = "2 3 + 4 5 + 6 7"

class Lexical_Anaylzer:     # 여기서 구현해야 하는 것은? 잘못 된 infix expession을 찾는 것.
    def __init__(self, expression):
        self.expression = expression

    def check_expression(self):




class Operand:
    def __init__(self, num):
        self.num = num

class Operator:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        self.add = "+"
        self.sub = "-"
        self.mul = "*"
        self.div = "/"
        self.lpar = "("
        self.rpar = ")"