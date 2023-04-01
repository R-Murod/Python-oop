# Date - 12/02/2023
# Режимы доступа - access modes
# Механизм инкапсуляции
# Что бы пользователь или программист не имел доступ к экземпляру, нужно сделать это закрытым
# attribute(без подчеркиваний) - публичное свойство (public)
# _attribute(с одним подчеркиванием) - доступно во внутри класса и во всех дочерних классов (protected)
# __attribute(с двумя подчеркиваниями) - доступно в внутри класса (private)
# Интерфейсные методы - геттеры и сеттеры
# raise - исключение
# модуль accessify - pip install accessify - будут доступно два декоратора - нужно только тогда когда очень надежно защитить методы


from accessify import private, protected
# @private - более защищенный чем __


class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):  # будет ссылка на класс Point
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Numbersssss")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(100, 200)
print(dir(pt))  # можно посмотреть каким образом можно обратится к атрибутам
pt._Point__check_value(5)