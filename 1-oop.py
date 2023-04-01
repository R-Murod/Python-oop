# Классы и объекты
# person = Point() - создаём экземпляр класса
# getattr(obj, name) - возвращает значение атрибута объекта
# hasattr(obj, name) - проверяет на наличие атрибута name в obj
# setattr(obj, name, value) - задает значение атрибута (если атрибута не существует, то он создается)
# delattr(obj, name) - удаляет атрибута с именем name

# del Point.name - for example, удаляем атрибут name из класса Point

# Инкапсуляция - через разрешенные методы(н.п у авто - руль, тормоз, газ), а так же public, private and protected
# Наследование - общие свойство(DRY), ex фигуры координаты, цвет, размеры
# Полиморфизм - разное поведение одного и того же метода в разных классах(изменяем методы)

# __doc__ - содержит строку с описанием класса -- """ Example """
# __dict__ - содежит набор содержит набор атрибутов экземпляра класса
class Point:
    def set_person(self, name, age):
        self.name = name
        self.age = age

    def get_person(self):
        return self.name, self.age


person = Point()
person.set_person("Murod", 21)
print(person.name)
print(type(person))
print(setattr(Point, 'prop', 1))
