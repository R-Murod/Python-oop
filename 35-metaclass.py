# def create_class_point(name, base, attrs):  # это всё через функции, но надо исп класс
#     attrs.update({'Max_coord': 100, 'Min_coord': 0})
#     return type(name, base, attrs)


class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(cls, name, base, attrs)

    # def __init__(cls, name, base, attrs):  # cls - ссылка на класс уже созданный (Point), attrs - все атрибуты внутри этого класса(Point), base - кортеж из базовых классов, name - имя класса(Point)
    #     super().__init__(name, base, attrs)
    #     cls.MAX_COORD = 100
    #     cls.MIN_COORD = 100


class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)


pt = Point()
print(pt.get_coords())
print(pt.MAX_COORD)
