# Magic method __call__
# dunder методы (от англ. double underscope)
# counter - счетчик
import math


# class Counter:
#     def __init__(self):
#         self.__counter = 0  # private
#
#     def __call__(self, step=1, *args, **kwargs):
#         print("__call__")
#         self.__counter += step
#         return self.__counter
#
#
# c = Counter()  # когда мы вставляем () после имени класса, то активизируется метод __call__
# c2 = Counter()
# c()  # экземпляр класса мы не можем вызвать подобно функцию, потому что они не вызываемые, у нас неопр магический метод __call__
# c(10)
# res = c()
# res2 = c2(-5)
# print(res, res2) # не зависимо друг друга

# Где и как используется
# Через класс, мы можем удалить указанных во функции
# class StripChars:
#     def __init__(self, chars):
#         self.__counter = 0
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise TypeError("Аргумент должен быть строкой")  # исключение
#         return args[0].strip(self.__chars)
#
#
# s1 = StripChars("?:!.; ")
# s2 = StripChars(" ")
# res = s1(" Hello World! ")
# res2 = s2("Murod Rakhmetov! ")
# print(res, res2, sep="\n")

# которые позволяет вычислять производное определенные функции в некой точки х
class Derivate:
    def __init__(self, func):  # func ссылается на функцию df_sin()
        self.__fn = func  # сслыка на эту функцию мы сохраняем вот этой приватной переменной __fn

    def __call__(self, x, dx=0.0001, *args, **kwargs):  # x = pi/3
        return (self.__fn(x + dx) - self.__fn(x)) / dx  # и тут вычисляется

@Derivate  # вместо это df_sin = Derivate(df_sin), если это тоже уберем, то получим просто pi/3
def df_sin(x):
    return math.sin(x)


# df_sin = Derivate(df_sin)
print(df_sin(math.pi/3))  # когда вызывается экземпляр класса df_sin, мы попадем в метод __call__