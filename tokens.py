class Base():
    def __init__(self, value):
        self.value = value
    
    def __repr__(self) -> str:
        return str(self.value)
    
    def __call__(self):
        return self.value

    def __eq__(self, other):
        if type(other) == type(self):
            return self.value == other.value
        else:
            return self.value == other
    
    @classmethod
    def is_valid(cls):
        pass


class Operator(Base):
    def __init__(self, value):
        super().__init__(value)


    @classmethod
    def is_valid(cls, value):
        return value in "+-*/"
    
    @classmethod        # classmethod는 독립된 함수처럼 작동함
    def check_priority(cls, value):
        priority = {'+':1, '-':1, '*':2, '/':2}
        return priority[str(value)]


class Operand(Base):
    def __init__(self, value):
        super().__init__(value)

    def __add__(self, other):
        return Operand(float(self.value) + float(other.value))

    def __sub__(self, other):
        return Operand(float(self.value) - float(other.value))

    def __mul__(self, other):
        return Operand(float(self.value) * float(other.value))

    def __truediv__(self, other):
        return Operand(float(self.value) / float(other.value))

    @classmethod
    def is_valid(cls, value):
        value = value.replace(".", "")      # 소수점 처리
        return value.isdigit() or value.isnumeric()