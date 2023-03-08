# __setattr__(self, key, value)__ - автоматически вызывается при изменении свойство key класса
# __getattribute__(self, item) - автоматически вызывается при получении свойство класса с именем item
# __getattr__(self, item) - автоматически вызывается при получении несуществующего свойство item класса
# __delattr__(self, item) - автоматически вызывается при удалении свойство item (не важно: существует оно или нет)
# Access is denied - доступ запрещен
# invalid attribute name - недопустимое имя атрибута

class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if Point.MAX_COORD <= x <= self.MIN_COORD:
            self.x = x
            self.y = y

    # def set_bound(self, left): - изменили значение на экземпляре класса
    #     self.MIN_COORD = left

    # @classmethod
    # def set_bound(cls, left):  # - изменили значение на уровне класса
    #     cls.MIN_COORD = left

    def __getattribute__(self, item):  # через этот магически метод мы можем управлять обращение к тому или иному атрибуту
        if item == "x":
            raise ValueError("Access is denied")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value): # с помощью этого магическог метода мы можем запретить создавать какой либо локальный атрибут в экземпляр класса
        if key == "z":
            raise AttributeError("invalid attribute name")
        else:
            return object.__setattr__(self, key, value)

    def __getattr__(self, item): # если идет обращение к несуществующим атрибута экземпляр класса, пусть в этом случае возвращает False
        return False

    def __delattr__(self, item): # мы можем контролировать удаление тех или иных атрибутов из экземпляров класса
        print("__delattr__: " + item)
        object.__delattr__(self, item) # это и удалить наш атрибут


pt1 = Point(1, 2)
pt2 = Point(10, 20)
del pt2.x
print(pt2.__dict__)