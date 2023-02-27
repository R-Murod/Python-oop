# Magic method - __str__(), __repr__(), __len__(), __abs__()
# dunder-method ( от англ double underscope)

# __str__() - для отображения информации об объекте класса для пользователей (exp for function print, str)
# __repr__() - для отображения информации об объекте класса в режиме отладки (для разработчиков)
# __len__() - позволяет применять функцию len() к экземплярам класса
# __abs__() - позволяет применять функцию abs() к экземплярам класса

# class Cat:
#     def __init__(self, name):  # для формирования в каждом экземпляре этого класса
#         self.name = name
#
#     def __repr__(self):  # должен возвращать строку
#         return f"{self.__class__}: {self.name}"  # __class__ - хранить имя класса
#
#     def __str__(self):  # должен возвращать определенную строку
#         return f"{self.name}"

class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(1, 2, -3)
print(len(p))
print(abs(p))