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

value = dict()

"""


test_expession = "* 2 3 + 4 5"          # wrong expression
test_expession2 = "2 3 + 4 5 + 6 7"


def lexical_analyzer(expression):
    operator = ["+", "-", "*", "/", "(", ")"]
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    """input spec:
    1. 공백이 아닌 값
    2. 연산자나 피연산자가 포함되어야 함
    3. 연산자나 피연산자가 아닌 문자는 허용하지 않음
    4. 연산자가 연속으로 나와서는 안 됨
    5. -, +가 아닌 연산자가 맨 앞에 나오면 안 됨 => 그냥 연산자는 앞에 등장할 수 없는 것으로 하자!
    """
    # 수식에 필요한 연산자들이 들어오지 않았을 때
    while any(i in expression for i in number+operator) == False:
        expression = (input("수식을 입력하세요: "))
        if expression == "":
            print("Please enter an expression")
        elif any(i in expression for i in number+operator) == False or expression.endswith(tuple(operator)) == True:
            print("Wrong expression!")
        elif any(i in expression for i in operator) == False:
            print("Please enter an operator!")
        elif any(i in expression for i in number) == False:
            print("Please enter a number!")
        elif expression.startswith(("*", "/")):
            raise ValueError("Wrong expression")

    # 수식에 필요한 연산자들이 들어왔을 때
    expression = expression.strip().replace(" ", "")
    if expression.startswith("+"):
        expression = expression[1:]
    expression


expression = input("Enter an expression: ")
lexical_analyzer(expression)


# class LexicalAnaylzer:     # 여기서 구현해야 하는 것은? 잘못 된 infix expession을 찾는 것.
#     # 연산자가 나오는 것을 찾기
#     def __init__(self, expression):
#         self.expression = expression
#         print("expression: ", self.expression)

#     def check_expression(self):
#         expression = self.expression.replace(" ", "")
#         if expression.startswith(("*", "/")):
#             raise ValueError("Wrong expression")

#         return expression


class Operate:
    def __init__(self):
        pass

    def __repr__(self):
        return self.operator


class Operator(Operate):
    def __init__(self, operator, operand1, operand2):
        super().__init__()
        self.operator = operator


class PostfixCalculator:
    def __init__(self, expression):
        self.expression = expression
