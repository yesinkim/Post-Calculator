class Base():
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return self.value
    
    @classmethod
    def is_valid(cls):
        pass



class Operator(Base):
    def __init__(self, value):
        super().__init__(value)
        
    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value
    
    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value
    
    @classmethod
    def is_valid(cls, value):
        return value in "+-*/"
    
    @classmethod        # class method는 하나의 class 처럼 동작함
    def check_priority(cls, value):
        priority = {'+':1, '-':1, '*':2, '/':2}
        return priority[str(value)]





class Operand(Base):
    def __init__(self, value):
        super().__init__(value)


    @classmethod
    def is_valid(cls, value):
        return value.isdigit() or value.isnumeric()
