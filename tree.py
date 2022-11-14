from __future__ import annotations
from operator import add, mul, sub, truediv
from typing import List, Union

from exceptions import FullTreeError
from tokens import BaseToken, NumberToken, OperatorToken

class BaseTree:
    def __init__(self, root: BaseToken) -> None:
        self.root = root
        self.left = None
        self.right = None

    def insert(self, value: Union[BaseToken, BaseTree]):
        if self.left is None:
            self.left = value

        elif self.right is None:
            self.right = value

        else:
            raise FullTreeError("Tree is full")

    def print_tree(self, idx: int = 0) -> None:
        print(f"{idx}: {'-'*idx}>  {self.root}")
        if self.left is not None:
            self.left.print_tree(idx+1)

        if self.right is not None:
            self.right.print_tree(idx+1)

    def evaluate(self) -> float:
        result = self.traverse()
        return result[0]

    def traverse(self) -> List[Union[str, float]]:
        result = []

        if self.left:
            if isinstance(self.left, NumberToken):
                result += [float(self.left.value)]

            elif isinstance(self.left, OperatorToken):
                result += [self.left.value]

            else:   # NonTerminalToken
                result += self.left.traverse()

        if self.right:
            if isinstance(self.right, NumberToken):
                result += [float(self.right.value)]

            elif isinstance(self.right, OperatorToken):
                result += [self.right.value]

            else:
                result += self.right.traverse()
        
        print(f"{self.data}: {result}")
        return self.calculate(result)

    def calculate(self, expression):
        result = expression


class FactorTree(BaseTree):
    pass

class FactorsTree(BaseTree):
    """Factors -> factor | -factor
    1. factor: 숫자
    2. -factor: 음수"""
    def calculate(self, expression):
            if len(expression) == 2:
                return [float(expression[1]) * -1]
            return expression

class EnclosedTree(BaseTree):
    def calculate(expression):
        return super().calculate()


class ScalingsTree(BaseTree):
    """Scalings -> Scaling Scalings | epsilon
    1. [숫자, *, /, 숫자]
    2. [*, / , 숫자]
    """
    def __init__(self, data: BaseToken):
        super().__init__(data)
        self.binary_calculte_map = {"*": mul, "/": truediv}

    def calculate(self, expression):
        if len(expression) == 4:
            result = self.binary_calculte_map[expression[2]](expression[1], expression[3])
            if expression[0] == "*":
                return [expression[0], result]

            else:       # 나누기를 역수취해 곱하기로 바꿔줌
                return ["*", 1/result]
        return super().calculate()

class TermTree(ScalingsTree):
    """Term-> Factors Scalings
    1. [숫자, epsilon]
    2. [숫자, * /, 숫자]"""
    def calculate(self, expression):
        if len(expression) == 3:
            result = self.binary_calculte_map[expression[1]](expression[0], expression[2])
            return [result]
        return expression


class ScalingTree(BaseTree):
    """Scaling -> MulOp Factors
    1. epsilon -> []
    2. * | / , 숫자
    3. * | / , 숫자, *, /, 숫자
    """
    pass


class IncrementsTree(BaseTree):
    """Increments: Increment Increments | epsilon
    1. [+ -, 숫자]
    2. [+ -, 숫자, + -, 숫자]=> [+ -, 숫자]
    """
    def __init__(self, data: BaseToken) -> None:
        super().__init__(data)
        self.binary_calculte_map = {"+": add, "-": sub}
    def calculate(self, expression):
        if len(expression) == 4:
            result = self.binary_calculte_map[expression[2]](expression[1], expression[3])
            return [expression[0], result]
        return expression

class IncrementTree(BaseTree):
    """Increment -> AddOp Term"""
    pass


class ExpressionTree(IncrementsTree):
    """Expression -> Term | Increments
    """
    def calculate(self, expression):
        if len(expression) == 3:
            result = self.binary_calculte_map[expression[1]](expression[0], expression[2])
            return [result]
        return expression