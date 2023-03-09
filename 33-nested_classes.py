# nested classes - вложенные классы
# Это нужна нам для описания модели во фреймворке - Django

class Women:
    title = 'объект класса для поля title'
    photo = 'объект класса для поля photo'
    ordering = 'объект класса для поля ordering'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + '@' + psw)  # если мы хотим обращаться к Мету()

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access


w = Women('root', '12345')
print(w.ordering)
print(w.Meta.ordering)
print(w.__dict__)  # пустой словарь, потому что мы не определили __init__, тут нету никаких локальных свойств, если __init__ есть то можем
print(w.meta.__dict__)  # пустой словарь, потому что мы не определили __init__
