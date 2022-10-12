class Base():
    def __init__(self, value):
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)
    
    def __repr__(self):
        return self.value
    
    @classmethod
    def is_valid(cls):
        pass



class Operator(Base):
    def __init__(self, value):
        super().__init__(value)
    
    @classmethod
    def is_valid(cls, value):
        return value in "+-*/"
    
    @classmethod        # class method는 독립된 함수처럼 작동함
    def check_priority(cls, value):
        priority = {'+':1, '-':1, '*':2, '/':2}
        return priority[str(value)]





class Operand(Base):
    def __init__(self, value):
        super().__init__(value)

    def __add__(self, other):
        return float(other.value) + float(self.value)

    def __sub__(self, other):
        return float(other.value) - float(self.value)

    def __mul__(self, other):
        return float(other.value) * float(self.value)

    def __truediv__(self, other):
        return float(other.value) / float(self.value)

    @classmethod
    def is_valid(cls, value):
        value = value.replace(".", "")      # 소수점 처리
        return value.isdigit() or value.isnumeric()
