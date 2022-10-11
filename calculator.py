"""
질문1. 여러 토큰 변수가 존재할 때 임시로 사용하는 토큰에 대한 변수를 지정하고 싶음. 
    이 때 변수명은 tmp_token , token_tmp 어떤 것이 좋은 방법인가?
    => 아무거나 사용하세요!
질문2. Token의 판별은 Token class 내부에서 하는 것? --> 해결
ㅠㅠㅠㅠㅠㅠㅠ
"""

# value class Token 
# 더 여러가지 일을 해야 한다면?

import re

from tokens import Operand, Operator


class ExpressionError(Exception):
    pass


class LexicalAnalyzer:
    """Find wrong expression and change expression to postfix"""

    def __init__(self):
        # self.expression = "27 - 3 * (1+2)"        # temp test expression
        self.expression = input("Enter an expression: ").replace(" ", "")
        self.check_expression()

    def check_expression(self):
        expression = self.expression.replace(" ", "")
        pattern = re.compile("[^\d.\/\+\*\-\(\)]")

        if expression == "":
            raise ExpressionError("Empty expression")
        elif pattern.search(expression):
            raise ExpressionError("Unexpected character")
        elif expression.startswith(("*", "/", "+", "-",")")) or expression.endswith(("*", "/", "+", "-","(")):
            raise ExpressionError("Wrong expression")
        elif expression.count("(") != expression.count(")") or expression.index("(") > expression.index(")"):       # ") 1 + 2 (" 같은 경우 걸러지지 않음
            raise ExpressionError("Parentheses error")


    def to_postfix(self):
        stack = []
        postfix = []
        expression = re.findall(r"[0-9.]+|[\+\-\*\/\(\)]", self.expression)

        for token in expression:
            # 피연산자 일 때에는 postfix에 추가
            if Operand.is_valid(token):
                postfix.append(Operand(token))
            
            # "("를 만나면 stack에 추가
            elif token == "(":
                stack.append(token)
            
            # ")"를 만나면 stack에서 "("를 만날 때까지 pop
            elif token == ")":
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
                # "("를 만나면 pop
                stack.pop()
            
            # 연산자 일 때에는 stack에 추가
            else:
                while stack and stack[-1]!='('and Operator.check_priority(token) <= Operator.check_priority(stack[-1]):
                    postfix.append(stack.pop())
                stack.append(Operator(token))
            
        while stack:
            postfix.append(stack.pop())
        
        print(f"Postfix expression: {postfix}")
        return postfix


def Calculate(tokens):
    stack = []
    for token in tokens:
        if token == '+':
            stack.append(stack.pop()+stack.pop())
        elif token == '-':
            stack.append(-(stack.pop()-stack.pop()))
        elif token == '*':
            stack.append(stack.pop()*stack.pop())
        elif token == '/':
            rv = stack.pop()
            stack.append(stack.pop()/rv)
        else:
            stack.append(int(token))
    return stack.pop()

# print(Calculate(["2", "3", "5", "*", "+", "7", "-"]))


if __name__ == "__main__":
    calc = LexicalAnalyzer()
    # calc.check_expression()
    post_expression = calc.to_postfix()
    print(Calculate(post_expression))
