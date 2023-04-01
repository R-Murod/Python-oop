# inheritance - наследования
# Наследование в ооп


class Geom:
    name = 'Geom'

    def set_coords(self, x1, x2, y1, y2):  # мы можем вынести одинаковые функции в базовые
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        # self.draw()  # работает, но для самого класса Geom выдаёт ошибку, потому что такого функции не существует

    def draw(self):
        print("Draw line")


class Line(Geom):  # Geom - базовый или родительский класс, Line - подкласс или дочерний класс
    name = "line"  # name - переопределяется в дочерним классе, слева стоит стрелочка

    def draw(self):  # точно такой же переопределение и в методах и свойствах
        print("Draw line")


class Rect(Geom):
    def draw(self):
        print("Draw rectangle")


# class Rect(Geom):  # если draw() не найдется в классе то, то проверяется из родительского класса
#     pass


g = Geom()
g.set_coords(1, 1, 2, 2)
r = Rect()
l = Line()
r.set_coords(1, 1, 2, 2)
l.set_coords(1, 1, 2, 2)
print(l.name)  # обращается к атрибуту name, если в классе нету то, ищет в базовым классе
print(r.name)
