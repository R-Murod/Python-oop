# Магические методы __getitem__(), __setitem__(), __delitem__()
# __getitem__(self, item) - получение значения по ключу item
# __setitem__(self, key, value) - запись значения value по ключи key
# __delitem__(self, key) - удаление элемента по ключу key


class Student:
    def __init__(self, name, marks):  # каждый экземпляр класса содержить имя и список оценок
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):  # через квадратные скобки возвращает значение, в данном случае из s1[2] - 2 идет к item
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):  # через квадратные скобки возвращает значение, в данном случае из s1[2] = 4 - 2 = key, value = 4
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)  # расширяем список до нужного индекса, extend() - добавляет в конец списка

        self.marks[key] = value  # key - принимает только целочисленные значение

    def __delitem__(self, key):  # вызывается когда происходить удаление того или иного объекта
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        del self.marks[key]


s1 = Student("Murod", [5, 5, 3, 2, 5])
# print(s1.marks[2]) # вводить нам значение из списка marks
# print(s1[2])
# print(s1[20]) # Неверный индекс
# s1[10] = 4  # Ошибка, класс Student не поддержит операцию присвоение
del s1[2]
print(s1.marks)