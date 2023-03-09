# Meta classes - Мета классы

#                                   Мета классы

# False       |     bool              |
# "Hello"     |     str               |      Мета класс
# 123         |     int               |
# [1, 2, 3]   |     list              |
# ______________________________________________________
# объекты     |    классы, объекты    |   Мета класс, класс, объект


class Point:
    MAX_COORD = 100
    MIN_COORD = 0


class B1:
    pass


class B2:
    pass


def method1(self):
    print(self.__dict__)


A = type('Point', (B1, B2), {'MAX_COORD': 100, 'method1': lambda self: self.MAX_COORD})
# с помощью объекта type() мы можем динамически создавать новые классы в нашей программе
pt = A()
print(pt.MAX_COORD)
print(A.__mro__)  # Point -> B1 -> B2 -> object
