import re

from exceptions import InvalidTokenError

class BaseToken():
    def __init__(self, value: str):
        if not self.is_valid:
            raise InvalidTokenError(f"{value} is not {self.__class__}")
        self.type = self.select_token(value)
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, BaseToken):
            return NotImplemented
        return self.type == other.type and self.value == other.value

    def __repr__(self):
        return f"{self.__class__.__name__}(type={self.type}, value={self.value})"

    @classmethod
    def is_valid(cls, value: str)-> bool:
        pass

    @classmethod
    def select_token(self, value: str) -> str:
        pass


class NumberToken(BaseToken):
    def __init__(self, value: str):
        super().__init__(value)
        self.type = 'Number'

    @classmethod
    def is_valid(cls, value: str)-> bool:
        return True if re.match("^[1-9]\d*(\.?\d+)?$|^0(\.\d+)?$", value) else False

    @classmethod
    def select_token(self, value: str) -> str:
        return "Number"


class OperatorToken(BaseToken):
    @classmethod
    def is_valid(cls, value: str)-> bool:
        return value in "+-*/"

    @classmethod
    def select_token(self, value: str) -> str:
        if value == "+":
            return "Add"
        elif value == "-":
            return "Sub"
        elif value == "*":
            return "Mul"
        elif value == "/":
            return "Div"
        else:
            raise InvalidTokenError(f"{value} is not {self.__class__}")

class ParenToken(BaseToken):
    @classmethod
    def is_valid(cls, value: str)-> bool:
        return value in "()"

    @classmethod
    def select_token(self, value: str) -> str:
        if value == "(":
            return "LParen"

        elif value == ")":
            return "RParen"

        else:
            raise InvalidTokenError(f"{value} is not {self.__class__.__name__}")

class NonTerminalToken():
    def __init__(self, type: str):
        self.type = type
    
    def __repr__(self):
        return f"{self.__class__.__name__}(type={self.type})"

class NonTerminalToken2(BaseToken):
    def __init__(self, select_type: str):
        self.type = select_type

    @classmethod
    def is_valid(cls, value: str)-> bool:
        return True