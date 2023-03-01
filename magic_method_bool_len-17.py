# Функция bool() и магические методы
# __len__() - вызывается функцией bool(), если не определен магический метод __bool__()
# __bool__() - вызывается в приоритетном порядке функцией bool()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        print("__bool__")
        return self.x == self.y


p = Point(3, 3)
# print(len(p))  # вызывается метод __len__
# print(bool(p))  # возвращает True, если значение равны
# В основном эти методы мы используем в условиях, пример:
if p:
    print("объект p дает True")
else:
    print("объект p дает False")
