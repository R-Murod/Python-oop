# множественное наследование - multiple inheritance
# Миксины(mxins) - примеси - реализуют как раз множественные наследования
# MRO - Method Resolution Order - Порядок разрешения метода
# __mro__ - список классов, который обходится при поиске того или иного атрибута

class Goods:
    def __init__(self, name, weight, price):
        super().__init__()  # для того что бы вызвать init в MixinLog, тут можно задать вопрос, как super() обращается к второму init в MixinLog
        print("init Goods")  # тут поможет нам MRO, NoteBook -> Goods -> MixinLog -> object
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")

    # def print_info(self):  # в случае когда у нас две одинаковые методы
    #     print("print_info из MixinLog")


class NoteBook(Goods, MixinLog):  # тут идет по порядку
    pass
    # def print_info(self):  # в случае когда у нас две одинаковые методы, если в Goods нету то такого переопределение не нужны
    #     MixinLog.print_info(self)


n = NoteBook("Acer", 1.5, 30000)
n.print_info()
n.save_sell_log()
print(NoteBook.__mro__)