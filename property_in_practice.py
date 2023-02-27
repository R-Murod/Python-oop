# Задача на свойства, property in practice
# verify - проверять
from string import ascii_letters


class Person:
    S_RUS = 'йцукенгшщзхъфывапролджэюбьтимсчяё-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(
            fio)  # что бы это метод отработал, если не возникнет ни одного исключение то программа пойдет дальше, для проверки корректность данных
        self.verify_old(
            old)  # что бы это метод отработал, если не возникнет ни одного исключение то программа пойдет дальше
        self.verify_ps(
            ps)  # что бы это метод отработал, если не возникнет ни одного исключение то программа пойдет дальше
        self.verify_weight(
            weight)  # что бы это метод отработал, если не возникнет ни одного исключение то программа пойдет дальше

        self.__fio = fio.split()  # private
        self.__old = old
        self.__password = ps
        self.__weight = weight

        # вместо всех этих проверок, мы можем так прописать
        # self.verify_fio(
        #     fio) # что бы это метод отработал, если не возникнет ни одного исключение то программа пойдет дальше, для проверки корректность данных

        # self.__fio = fio.split()  # private
        # self.old = old # что бы тут сработал сеттер
        # self.password = ps
        # self.weight = weight

    @classmethod  # декоратор класс метод, уровня класса
    def verify_fio(cls, fio):  # cls - ссылка на класс
        if type(fio) != str:
            raise TypeError("Фио должно быть строкой")  # raise - исключение
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат Фио")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER  # ascii_letters - это набор латинских букв малых и больших
        # S_RUS - набор русских букв, S_RUS_UPPER - а это русских за главных букв
        for s in f:
            if len(s) < 1:
                raise TypeError("В Фио должен быть хотя бы один символ")
            if len(s.strip(
                    letters)) != 0:  # если в фио содержить только разрешенные символы, то strip всех удалить и длина должна быть равно 0
                raise TypeError("В Фио можно использовать только буквенные символы и дефис")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом в диапазоне от 14 до 120")

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Возраст должен быть вещественным числом от 20 и выше")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")
        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должна быть числами")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)  # для проверки, прежде чем присваивать новое значение
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, ps):
        self.verify_ps(ps)
        self.__password = ps


# p = Person('Рахметов2 Мурод Эркинович', 21, '1234 567890', 80.0) # error
# p = Person('РахметовМурод Эркинович', 21, '1234 567890', 80.0) # error
p = Person('Рахметов Мурод Эркинович', 21, '1234 567890', 80.0)  # тут всё правильно
print(p.__dict__)
# присваиваем коррестное значение
p.old = 40
p.password = '1234 987654'
p.weight = 70.0
print(p.__dict__)
