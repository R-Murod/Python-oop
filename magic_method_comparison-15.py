# Методы сравнения
# __eq__() - для равенства (==)
# __ne__() - для неравенства (!=)
# __lt__() - для оператора меньше (<)
# __le__() - для оператора меньше или равно (<=)
# __gt__() - для оператора больше (>)
# __ge__() - для оператора больше или равно (>=)

# Formula
# c1 != c2, not(c1 == c2)
# c1 > c2, c2 < c1
# c1 >= c2, c2 <= c1

class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")

        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):  # что бы не было дублирование кода в магических методах
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):  # для сравнения (==)
        sc = self.__verify_data(other)
        return self.seconds == sc  # self = c1, sc = количество секунд у правого операнда

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc  # self = c1, sc = количество секунд у правого операнда

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc  # self = c1, sc = количество секунд у правого операнда


c1 = Clock(1000)
c2 = Clock(2000)
print(c1 == c2)  # тут сравнивается только адреса этих экземпляров, if we use magic method __eq__, then output will True or False
print(c1 != c2)  # работает!!!, хотя мы не определили метода __ne__, мы можем использовать этот метод, но по умолчанию интерпретатор питон сам решить
print(c1 < c2)  # тут сравнивается только адреса этих экземпляров, if we use magic method __lt__, then output will True or False
print(c1 > c2)  # работает!!!, для проверки определим метод, но по умолчанию интерпретатор питон сам решить