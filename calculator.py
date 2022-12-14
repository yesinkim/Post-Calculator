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
            # ???????????? ??? ????????? postfix??? ??????
            if Operand.is_valid(token):
                postfix.append(Operand(token))
            
            # "("??? ????????? stack??? ??????
            elif token == "(":
                stack.append(token)
            
            # ")"??? ????????? stack?????? "("??? ?????? ????????? pop
            elif token == ")":
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
                # "(" stack?????? ??????
                stack.pop()
            
            # ????????? ??? ????????? stack??? ??????
            else:
                while stack and stack[-1]!='('and Operator.check_priority(token) <= Operator.check_priority(stack[-1]):
                    postfix.append(stack.pop())
                stack.append(Operator(token))
            
        while stack:
            postfix.append(stack.pop())
        
        return postfix



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







# test code ????????????
# input spec?????? ????????? ????????? ????????????????????? ???????????? ???
# input spec??? ????????? ????????? ?????? ????????? ??? ????????? ??????
# test case ??? ???????????? ??????!! => ?????????????????? ?????? ?????? ????????? ?????? ??? ??????
if __name__ == "__main__":
    calc = LexicalAnalyzer()
    post_expression = calc.to_postfix()
    print(f"Postfix expression : {post_expression}")
    print(f"result             : {calculate(post_expression)}")
