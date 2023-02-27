# Магические методы арифметических операций

# x + y = __add__(self, other) - для операции сложения, преимущество является если у нас много экземпляров класса, __radd__(self, other), __iadd__(self, other)
# x - y = __sub__(self, other) - для операции вычитания, __iadd__(self, other)
# x * y = __mul__(self, other) - для операции умножения, __imul__(self, other)
# x / y = __truediv__(self, other) - для операции деления, __itruediv__(self, other)
# x // y = __floordiv__(self, other), __ifloordiv__(self, other)
# x % y = __mod__(self, other), __imod__(self, other)

class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):  # seconds: int - нотация, для чтение программиста
        if not isinstance(seconds, int):  # проверяем действительно ли является вот эти секунды целыми числами
            raise TypeError("Секунды должны быть целым числом")  # если не так, то мы генерируем исключение TypeError
        self.seconds = seconds % self.__DAY  # если проходят, то создаём в экземпляре seconds

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod  # уровень метода класса, декоратор
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):  # other - это значение который стоить справа от +, self - будет ссылаться экземпляр класса c1
        if not isinstance(other, (int, Clock)):  # для проверки можно было оставить int, но для сложения экземпляров нужен само класс
            raise ArithmeticError("Правый операнд должен быть int")

        sc = other  # если other простой число sc будет ссылаться целое число
        if isinstance(other, Clock):  # если other Clock
            sc = other.seconds  # то sc будет ссылаться на свойство seconds
        return Clock(self.seconds + sc)  # self.seconds - c1

    def __radd__(self, other):  # будем использовать в таком случае с1 = 100 + с1
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")

        sc = other  # если other простой число sc будет ссылаться целое число
        if isinstance(other, Clock):  # если other Clock
            sc = other.seconds  # то sc будет ссылаться на свойство seconds

        self.seconds += sc
        return self


c1 = Clock(1000)
c2 = Clock(2000)
# c1.seconds = c1.seconds + 100  # можно сделать так
# c1 = c1 + 100 # экземпляру класса мы не можем использовать некие операции, но можно исправить, если это строка то нужно прописать условию
# c3 = c1 + c2 # ошибка, и это мы будем исправить в __add__
# c1 = 100 + c1 # we use magic method __radd__
c1 += c1

print(c1.get_time())

