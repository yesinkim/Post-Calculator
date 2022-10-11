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
        
    
    @classmethod            # class method는 하나의 class 처럼 동작함
    def is_valid(cls, value):
        return value in "+-*/"
    
    @classmethod
    def check_priority(cls, value):
        priority = {'+':1, '-':1, '*':2, '/':2}
        return priority[value]





class Operand(Base):
    def __init__(self, value):
        super().__init__(value)


    @classmethod
    def is_valid(cls, value):
        return value.isdigit() or value.isnumeric()
