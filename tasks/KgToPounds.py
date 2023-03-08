# Task 3
# kg to pounds - кг в фунты
# Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм, а с помощью метода to_pounds() они переводятся в фунты.
# Чтобы закрыть доступ к переменной “kg” она реализовала методы set_kg() - для задания нового значения килограммов, get_kg()  - для вывода текущего значения кг.
# Из-за этого возникло неудобство: нам нужно теперь использовать эти 2 метода для задания и вывода значений.
# Помогите ей переделать класс с использованием функции property() и свойств-декораторов. Код приведен ниже.

class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg  # private

    def to_pounds(self):
        if isinstance(self.__kg, (int, float)):  # проверяем
            return self.__kg * 2.205
        else:
            raise ValueError("Килограммы задаются только числами")  # генератор исключение

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):  # проверяем
            self.__kg = new_kg
        else:
            raise ValueError("Килограммы задаются только числами")  # генератор исключение

    def get_kg(self):
        return self.__kg


# kg = KgToPounds("str")
# kg.set_kg(5)
# print(kg.to_pounds())


# Есть другая решения с помощью свойство property()

class KgToPounds2:
    def __init__(self, kg):
        self.__kg = kg

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError("Килограммы задаются только числами")

    def to_pounds(self):
        return self.__kg * 2.205


kg = KgToPounds2(5)
kg.kg = 10  # задали новое значение
print(kg.to_pounds())

