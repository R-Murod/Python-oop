# Свойство property - что бы каждому атрибуту не писать геттеры и сеттеры

# property - свойство
# as - в виде


class Person:
    def __init__(self, name, old):
        self.__name = name # as private
        self.__old = old # что бы обращаться к таким закрытым данных, нужна геттеры и сеттеры

    # def get_old(self):
    #     return self.__old
    #
    # def set_old(self, old):
    #     self.__old = old

    @property # ставится перед геттером
    def old(self):
        return self.__old

    @old.setter
    def old(self, old): # the name of methods must match, when we use decorators
        self.__old = old

    @old.deleter # оно вызывается когда происходить удаление определенного свойства
    def old(self):
        del self.__old

    # old = property(get_old, set_old) # приоритет выше чем другого атрибут(переменные) класса
    # old = property()
    # old = old.setter(set_old)
    # old = old.getter(get_old)


p = Person("Murod", 21)
# print(p.get_old())
# p.set_old(35)
# print(p.get_old())
# print(p.old)
# p.__dict__['old'] = 'old in object p' # вручную писали, это для переменных
# p.old = 35
# print(p.old)

del p.old
# print(p.old) # не будет работать потому что, оно удалено
p.old = 5 # но мы можем присвоить новое значение
print(p.old)
print(p.__dict__) # можем посмотреть что там

