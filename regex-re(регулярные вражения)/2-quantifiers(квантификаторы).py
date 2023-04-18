# quantifiers - квантификаторы
# {m, n}
# m - минимальное число совпадений с выражением
# n - максимальное число совпадений с выражением


import re

text = "Google, Gooogle, Goooooogle"
match = re.findall(r"o{2,5}", text)  # r"o{2, 5} - квантификатор, мажорный "o" может повторяться от 2 до 5
match1 = re.findall(r"o{2,5}?", text)  # r"o{2, 5}? - квантификатор, минорный выводит по 2 "o"
match2 = re.findall(r"Go{2,}gle", text)  # r"o{2,} - квантификатор, выводит все "o" от 2 и больше
match3 = re.findall(r"Go{,4}gle", text)  # r"o{,4} - квантификатор, выводит все "o" не больше 4
print(match)
print(match1)
print(match2)
print(match3)

phone = "87531598624"
match4 = re.findall(r"8\d{10}", phone)  # проверка корректность телефон номера
print(match4)

text2 = "стеклянный, стекляный"
match5 = re.findall(r"стеклянн?ый", text2)  # это гласит что н можно выводить от 0 до 1
print(match5)

text3 = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
match6 = re.findall(r"\w+\s*=\s*[^;]+", text3)  # выводим все текста кроме ";"
print(match6)

text4 = "<p> Картинка <img src='bg.jpg'> в тексте </p>"
match7 = re.findall(r"<img.*>", text4)  # . - перебирает все символы, * - выводить все символы пока не встретиться ">"
# - выбирает наиболее длинный последовательность, <img src='bg.jpg'> в тексте </p>
match8 = re.findall(r"<img.*?>", text4)  # наиболее короткий последовательность <img src='bg.jpg'>
match9 = re.findall(r"<img[^>]*>", text4)  # второй вариант, наиболее короткий последовательность <img src='bg.jpg'>
match10 = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text4)  # attribute img должен содержать src
print(match7)
print(match8)
print(match9)
print(match10)