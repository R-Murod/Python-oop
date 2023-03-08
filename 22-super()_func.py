# Расширение - extended
# переопределение - overriding

# Example: Расширение - extended
# class Geom:
#     name = "Geom"
#
#
# class Line(Geom):
#     def draw(self):
#         print("Draw line")

# Example: переопределение - overriding
# class Geom:
#     name = "Geom"
#     def draw(self):
# #       print("Draw line")
#
#
# class Line(Geom):
#     def draw(self):
#         print("Draw line")

class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f'инициализатор Geom for {self.__class__}')  # для проверки из какого дочернего класса был вызван
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):

    def draw(self):
        print("Draw line")


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        # Geom.__init__(self, x1, y1, x2, y2)  # для отображения вызова __init__ в Geom
        super().__init__(x1, y1, x2, y2)  # делегирование - для отображения вызова __init__ в Geom, super() - для обращение к базовой классу, self - не потребуется
        print("инициализатор Rect")
        self.fill = fill

    def draw(self):
        print("Draw rect")


# после () - вызывается метод __call__ - который по очередью вызывает, then method __new__ - для создания экземпляра класса, потом метод __init__
l = Line(0, 0, 10, 20)
r = Rect(0, 0, 10, 20)
