# Введение в Data Classes part 2
# Data classes - классы данных

from dataclasses import dataclass, field, InitVar


class Vector3D:
    def __init__(self, x: int, y: int, z: int, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5 if calc_len else 0


@dataclass
class V3D:
    x: int = field(repr=False)  # исключаем x
    y: int
    z: int = field(compare=False)  # исключаем в сравнение
    calc_len: InitVar[bool] = True  # те параметры которые исп InitVar, того мы должны передать в __post_init__
    length: float = field(init=False, compare=False, default=0)  # init - говорить не следует добавить length как параметр

    def __post_init__(self, calc_len: bool):  # с этим методом мы можем воспользоваться всеми атрибутами
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3, False)
v2 = V3D(1, 2, 3)
print(v)
print(v == v2)  # use compare