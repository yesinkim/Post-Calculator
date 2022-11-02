import re

from tokens import Operand, Operator
from exception import ExpressionError, ParenthesesError, OperatorError, OperandError

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
        return re.findall(r"[0-9.]+|[\+\-\*\/\(\)]", self.expression)



    def check_expression(self) -> None:
        """check expression is valid or not

        Raises:
            ExpressionError: When expression is not valid
            OperatorError: When operators are overlapped
            ParenthesesError: When Parentheses are not matched
            OperandError: When points are overlapped
        """
        expression = self.expression.replace(" ", "")
        pattern = re.compile("[^\d.\/\+\*\-\(\)]")
        pattern2 = re.compile(r"([\+\-\*\/]){2}")

        if pattern.search(expression):
            raise ExpressionError("Unexpected character")

        elif pattern2.search(expression):
            raise OperatorError("Overlap operator")

        elif re.search(r"[\+\-\*\/\(\)].*(-)[0-9]", expression):
            raise OperandError("Negative number")

        elif expression.startswith(("*", "/", "+", "-", ")")) or expression.endswith(("*", "/", "+", "-", "(")):
            raise ExpressionError("Wrong expression")

        elif expression.count("(") != expression.count(")"):
            raise ParenthesesError("Wrong parentheses match")
        
        elif expression.find("(") + expression.find(")") >= 0:
            x = 0
            for i in expression:
                if i == "(":
                    x += 1
                elif i == ")":
                    x -= 1
                if x < 0:
                    raise ParenthesesError("Wrong Parentheses")

        elif expression.find("..") >= 0:
            raise OperandError("Double dot")

    def to_postfix(self) -> list:
        """make expression to postfix

        Returns:
            list: postfix expression list contains operand and operator objects
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



class Parser():
    def __init__(self):
        self.lexical_analyzer = LexicalAnalyzer()

    def parse(self):
        pass



class Caculator():
    def __init__(self):
        pass
        

def calculate(expression) -> Operand:
    """Calculate postfix expression
    
    Returns: 
Returns: 
    Returns: 
        Operand: result of expression
    """
    stack = []

    for token in expression:
        if type(token) == Operand:
            stack.append(token)
            continue
        
        if len(stack) < 2:
            stack.insert(0, Operand(0))
        op1, op2 = stack.pop(), stack.pop()

        if token.value == '+':
            stack.append(op2 + op1)

        elif token.value == '-':
            stack.append(op2 - op1)

        elif token.value == '*':
            stack.append(op2 * op1)

        elif token.value == '/':
            if op1.value == 0:
                raise ZeroDivisionError("Zero Division Error")
            stack.append(op2 / op1)

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
    print(f"Postfix expression : {post_expression}")
    print(f"result             : {calculate(post_expression)}")
