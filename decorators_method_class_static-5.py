# Date - 10/02/2023
# decorators - декораторы
# Decorators - @classmethod and #staticmethod

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):  # Vector.validate(x) and Vector.validate(y) - лучше исп. self and cls, чтобы не вызывать название класса в классе
            self.x = x
            self.y = y

        print(self.norm2(self.x, self.y))

    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


v = Vector(1, 20)
print(Vector.norm2(5, 2))
print(Vector.validate(5))
# res = v.get_coords()  # res = Vector.get_coords(v)
# print(res)
