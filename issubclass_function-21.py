# Line -> Geom -> object
class Geom:
    pass


class Line(Geom):
    pass


g = Geom()
l = Line()
print(issubclass(Line, object))  # проверка наследование, проверка к экземпляру не работает
print(isinstance(l, Geom))  # проверка к экземпляру


# Для проверки расширение функции

class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


v = Vector([1, 2, 3])
print(v)
