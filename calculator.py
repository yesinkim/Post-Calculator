import re

from tokens import Operand, Operator


class ExpressionError(Exception):
    pass


class LexicalAnalyzer:
    """Find wrong expression and change expression to postfix"""

    def __init__(self):
        # self.expression = "2.7 - 3 * (1+2)"        # temp test expression
        # self.expression = "2+2 + 4"
        # self.expression = " 02 + 4 + 5"
        self.expression = input("Enter an expression: ").replace(" ", "")
        self.check_expression()

    def check_expression(self):
        expression = self.expression.replace(" ", "")
        print(expression)
        pattern = re.compile("[^\d.\/\+\*\-\(\)]")
        pattern2 = re.compile(r"([\+\-\*\/])\1+")

        if expression == "":
            raise ExpressionError("Empty expression")       # error 세부화

        elif pattern.search(expression):
            raise ExpressionError("Unexpected character")

        elif pattern2.search(expression):
            raise ExpressionError("Overlap operator")

        elif expression.startswith(("*", "/", "+", "-", ")")) or expression.endswith(("*", "/", "+", "-", "(")):
            raise ExpressionError("Wrong expression")

        elif expression.count("(") != expression.count(")") or expression.find("(") > expression.find(")"):       # ") 1 + 2 (" 같은 경우 걸러지지 않음
            raise ExpressionError("Parentheses error")

    def to_postfix(self):
        """_summary_

        Returns:
            _type_: _description_
        """
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
                # "(" stack에서 제거
                stack.pop()
            
            # 연산자 일 때에는 stack에 추가
            else:
                while stack and stack[-1]!='('and Operator.check_priority(token) <= Operator.check_priority(stack[-1]):
                    postfix.append(stack.pop())
                stack.append(Operator(token))
            
        while stack:
            postfix.append(stack.pop())
        
        return postfix


def Calculate(expression):
    stack = []

    for token in expression:
        if token.value == '+':
            stack.append(Operand(stack.pop()+stack.pop()))

        elif token.value == '-':
            stack.append(Operand(stack.pop()-stack.pop()))

        elif token.value == '*':
            stack.append(Operand(stack.pop()*stack.pop()))

        elif token.value == '/':
            # 0으로 나눌 수 없음. -> Zero Division Error 발생 예외처리
            rv = stack.pop()
            stack.append(Operand(stack.pop()/rv))

        else:
            stack.append(token)

    return stack.pop()







# test code 작성하기
# input spec에서 정의한 것들을 테스트케이스로 보여줘야 함
# input spec에 정의한 것들은 모두 실행할 수 있어야 하고
# test case 를 꼼꼼하게 작성!! => 예외처리하는 것에 대한 통찰을 기를 수 있음
if __name__ == "__main__":
    calc = LexicalAnalyzer()
    post_expression = calc.to_postfix()
    print(f"Postfix expression: {post_expression}")
    print(f"result: {Calculate(post_expression)}")
