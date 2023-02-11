# Date - 10/02/2023
# Magic method - магический метод
# __new__()  - вызывается перед созданием объекта класса
# super() - конструкция, ссылка на базовый класс


# class Point:
#     def __new__(cls, *args,
#                 **kwargs):  # magic method __new__ , cls - ссылается на текущий экземпляр класса, в данном сл. Point
#         print("call __new__ for " + str(cls))
#         return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):  # magic method __init__  , self - ссылается уже создаваемый экземпляр класса
#         print("call __init__ for " + str(self))
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# print(pt)


class DataBase:
    __instance = None  # будет ссылкой на экземпляр класса

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"connect with DB: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print(f"close connect with DB")

    def read(self):
        return "information from DB"

    def write(self, data):
        print(f"record in DB: {data}")


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)

print(id(db), id(db2)) # это говорить что при создании 2 го объекта он не был создан
