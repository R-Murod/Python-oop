# __slots__ с property и при наследовании

# Пример с property

# class Point2D:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.__length = (x * x + y * y) ** 0.5
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p = Point2D(1, 2)
# print(p.length)
# p.length = 10
# print(p.length)


# Пример с наследованием
class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    __slots__ = ()  # в нем будут разрешены эти два свойства х и у

