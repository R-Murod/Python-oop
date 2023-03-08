# Date - 08/02/2023
# Инициализатор и финализатор
# Магические методы - __название__
# __init__(self) - инициализатор объекта класса, вызывается сразу после создания экземпляр класса
# __del__(self) - финализатор класса, перед его удалением
# pt = Point() - pt ссылается на Point()
# pt = 0 - можем присвоить 0
# перед удалением экземпляра вызывается __del__

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print("call dell " + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt = Point()
print(pt.__dict__)