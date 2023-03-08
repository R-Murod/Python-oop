# Решаем задачи
# ingredient - добавка
# Task 1
# Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».
class Soda:
    def __init__(self, ingredient):
        if isinstance(ingredient, str):  # для проверки является ли оно строка
            self.ingredient = ingredient
        else:  # если нет, то нечего не сделаем
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print(f"Газировка и {self.ingredient}")
        else:
            print("Обычная газировка")


s = Soda("sugar")
s1 = Soda(5)
s.show_my_drink()
s1.show_my_drink()
