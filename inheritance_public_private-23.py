# Модификатор доступа
# public
# protected - _attribute
# private - __attribute


class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f'инициализатор Geom for {self.__class__}')  # для проверки из какого дочернего класса был вызван
        self.__x1 = x1  # они доступны только внутри этого класса, для доступа к дочерним класса это - self._x1 = x1 - с одним подчеркиванием
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def _verify_coord(self, coord):  # методами точно также, private protected public
        return 0 <= coord < 100


class Rect(Geom):  # наследует от класса Geom
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._verify_coord(x1)
        self.__fill = fill

    # def get_coords(self):  # в дочерних класса мы не можем обращаться к приватному атрибуту
    #     return (self.__x1, self.__y1)


r = Rect(0, 0, 10, 20)
print(r.__dict__)
