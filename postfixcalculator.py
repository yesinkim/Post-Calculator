"""
Calculator Code
(https://github.com/est-ai/PostfixCalculator_HS/blob/main/main.py)
Object: infix로 표기되어 있는 식을 입력 받을 수 있는 인터페이스와 입력 받은 식을 계산하는 함수를 개발 
Input: infix로 표기되어 있는 식
Output: 계산 결과

구현 해야 하는 것
1. Lexical Analyzer?
-> 입력을 어떻게 받지??? (input)
-> 입력받아서 연산자와 피연산자를 구별 (계속?)  # 여기를 수정했는데 풀 해볼거임!

2. Postfix Calculator
-> 입력 받은 식을 postfix로 변환 및 계산해서 output

연산자(Operator)와 피연산자(Operand)는 모두 Class로 구현되어야 함.
# 고려해야하는 연산자 (+, -, *,  /,  ( , ) )
# 1. 괄호
# 2. 곱셈, 나눗셈
# 3. 덧셈, 뺄셈
# 4. 연산자를 기준으로 왼쪽계산
"""

test_expression = "1 * (-2 + (4 / 2))"
# => 1 * (-2 + (4 + 2)) -> 1 * (-2 + 42+) -> 1 * ()

test_expession = "* 2 3 + 4 5"          # wrong expression
test_expession2 = "2 3 + 4 5 + 6 7"


def lexical_analyzer(expression: str):
    # infix -> postfix 바꾸는 method
    # postfix -> 계산하는 method
    """regonize the expression

    Args:
        expression (str): infix expression
    """
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    operator = ["+", "-", "*", "/", "(", ")"]
    tmp = [1, 1, 2, 2, 3, 3]
    priority = dict(zip(operator, tmp))
    """input spec:
    1. 공백이 아닌 값
    2. 연산자나 피연산자가 포함되어야 함
    3. 연산자나 피연산자가 아닌 문자는 허용하지 않음
    4. 연산자가 연속으로 나와서는 안 됨
    5. -, +가 아닌 연산자가 맨 앞에 나오면 안 됨 => 그냥 연산자는 앞에 등장할 수 없는 것으로 하자!
    """

    # 수식에 필요한 연산자들이 들어왔을 때
    """
    0. 이 때, 문제는 괄호임! 괄호는 먼저 따로 처리해주는 과정이 필요함...

    1. 가장 높은 순서의 연산자를 찾는다. 
    2. 연산자를 기준으로 왼쪽과 오른쪽을 나눈다. (왼쪽, 오른쪽: 피연산자, 가운데: 연산자)
    """
    expression = expression.strip().replace(" ", "")
    if expression.startswith("+"):
        expression = expression[1:]



def find_operator(expression):
    pass

    # expression에 3의 값을 가진 연산자가 있음 -> 그것은 괄호임 괄호 일 때 어떻게 처리를 할 것인가?
    print(expression)


expression = input("Enter an expression: ")
lexical_analyzer(expression)


class LexicalAnaylzer:     # 여기서 구현해야 하는 것은? 잘못 된 infix expession을 찾는 것.
    # 연산자가 나오는 것을 찾기
    def __init__(self, expression):
        self.expression = expression
        print("expression: ", self.expression)

    def check_expression(self):
        expression = self.expression.replace(" ", "")
        if expression.startswith(("*", "/")):
            raise ValueError("Wrong expression")

        return expression


class BaseToken:
    def __init__(self, value):
        self.value = value
        pass

    def __repr__(self):
        return self.value

    @classmethod
    def is_valied(cls, value):
        pass


class Operator(BaseToken):
    def __init__(self, value):
        super().__init__()
        self.value = value




class Operand(BaseToken):
    def __init__(self, operand):
        super().__init__()
        self.operand = operand


class PostfixCalculator:
    """식을 입력받고 계산하는 method"""
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return self.expression

    def tokenize(self):
        pass

    def calculate(self):
        pass


