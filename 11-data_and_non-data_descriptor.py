# Дескрипторы - data descriptor and non-data descriptor
# verify - проверять
# что бы 10 раз не прописать координаты, нам нужны дескриптор

# Разница между data descriptor and non-data descriptor - не имеет сеттера или делитера
# class ReadIntX - представляет собой не-дескриптор данных(non-data descriptor)
class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


# class Integer - представляет собой дескриптор данных(data descriptor)
class Integer:
    # простейшие реализация дескриптора данных
    # преимущество с классом Integer можем создать 10 или 20 координаты, и он имеет такой уникальный интерфейс
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")  # исключение

    def __set_name__(self, owner,
                     name):  # что бы мы смогли смформировать этот set_name, через который потом будем обращаться в геттере и сеттере
        self.name = "_" + name

    def __get__(self, instance, owner):  # getter
        # return instance.__dict__[self.name] # вместо __dict__ можно использовать
        return getattr(instance, self.name)  # instance - область видимость

    def __set__(self, instance, value):  # setter
        self.verify_coord(value)
        # print(f"__set__: {self.name} = {value}")
        # instance.__dict__[self.name] = value # instance - ссылается на текущий экземпляр класса Point3D
        # вместо __dict__ можно использовать
        return setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):  # инициализатор с 3я параметрами
        # self._x = x # protected
        # self._y = y
        # self._z = z

        # мы можем просто исп.

        self.x = x  # protected
        self.y = y  # можна воспользоваться сущ. объектом
        self.z = z

    # закомментирую что бы использовать дескрипторе
    # @classmethod
    # def verify_coord(cls, coord):
    #     if type(coord) != int:
    #         raise TypeError("Координата должна быть целым числом")  # исключение

    # закомментирую что бы использовать дескрипторе
    # @property
    # def x(self):
    #     return self._x
    #
    # @x.setter
    # def x(self, coord):
    #     self.verify_coord(coord)  # для проверки
    #     self._x = coord  # если проверка успешно проходить, то мы присваиваем coord
    #
    # @property
    # def y(self):
    #     return self._y
    #
    # @y.setter
    # def y(self, coord):
    #     self.verify_coord(coord)  # для проверки
    #     self._y = coord  # если проверка успешно проходить, то мы присваиваем coord
    #
    # @property
    # def z(self):
    #     return self._z
    #
    # @z.setter
    # def z(self, coord):
    #     self.verify_coord(coord)  # для проверки
    #     self._z = coord  # если проверка успешно проходить, то мы присваиваем coord


p = Point3D(1, 2, 3)
p.xr = 5
print(p.__dict__, p.xr)
