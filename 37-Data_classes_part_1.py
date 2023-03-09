# Введение в Data Classes
# Data classes - классы данных

from dataclasses import dataclass, field
from pprint import pprint


class Thing:  # это класс мы можем написать с помощью dataclass
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f"Thing: {self.__dict__}"


@dataclass  # декоратор dataclass, автоматически вставляется метод __repr__, сокращает код
class ThingData:  # Thing and ThingData практически одно и то же
    name: str
    weight: int = 0
    price: float = 0
    # dims: list = []  # мы не можем присвоить значение к изменяемым переменным, решение к этому задачу указан ниже
    dims: list = field(default_factory=list)  # при __init__ создается dims: [], у всех экземпляра будет своё значение
    # если в Thing __init__ будем создать list, потом будем добавлять значение оно там и сохраняется

    # view in __init__
    # def __init__(self, name: str, price: float = 0, weight: int = 0):
    #     self.name = name
    #     self.weight = weight
    #     self.price = price

    # def __eq__(self, other):  # по умолчанию проверяется все параметры ThingData, мы можем вручную писать
    #     return self.weight == other.weight


# t = Thing("Thing", 54, 1200)
td = ThingData("ThingData", 54, 1200)
td.dims.append(10)  # для проверки dims: list
print(td)
td_2 = ThingData("ThingData", 54, 1200)  # для проверки dims: list
print(td_2)
# print(t)
# print(td)
# pprint(ThingData.__dict__)  # выводить какие методы принадлежать к ThingData
# td_2 = ThingData("ThingData", 54, 1200)  # в ThingData __eq__ проверяется по параметрам
# td_3 = ThingData("ThingData", 55, 1200)
# print(td_2 == td_3)
