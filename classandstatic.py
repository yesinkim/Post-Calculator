# staticmethod

class test:
    n = 10
    t = "안녕하세요. 상속합니다."

    @staticmethod
    def add_s(x):
        return x + 10

    @classmethod
    def add_c(cls, x):
        return x + 10


# 둘 다 결과는 같음
print(test.add_s(5))
print(test.add_c(5))


class hello:
    t = '내가 상속해 줬어'

    @classmethod
    def calc(cls):
        return cls.t


class hello_2(hello):
    t = '나는 상속 받았어'

    @classmethod
    def calc(cls):
        return cls.t


print(hello_2.calc())


class Date:
    word = 'date :'

    def __init__(self, date):
        self.date = self.word + date

    @staticmethod
    def now():
        return Date("today")

    def show(self):
        print(self.date)



class DateClass:
    word = 'date :'

    def __init__(self, date):
        self.date = self.word + date

    @classmethod
    def now(cls):
        return cls("today")

    def show(self):
        print(self.date)




class KoreanDate(Date):
    word = '날짜 :'


class KoreanDateClass(DateClass):
    word = '날짜 :'


a = Date("2022, 10, 02")
a.show()
b = Date.now()
b.show()
c = KoreanDate.now()
c.show()
d = KoreanDateClass.now()
d.show()