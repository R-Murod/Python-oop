# character class - символьный класс
import re

text = "Карта map и объект bitmap - это разные вещи"
match = re.findall('map', text)
match1 = re.findall(r'\bmap\b', text)  # можно использовать в таком виде '\\bmap\\b' или r'\bmap\b' -
# r - исп. - ся перед определением шаблоны регулярных выражений
print(match)
print(match1)
# Специальные символы =   \.^$?+*{}[]()|

text2 = 'Еда, беду, -5 5 55 победа'
match2 = re.findall(r"[еЕ]д[ау]", text2)  # символьные классы
match3 = re.findall(r"[0123456789]", text2)  # символьные классы, если хотим найти 5, можно в таком виде r"[0-9]"
match4 = re.findall(r"[0123456789][0-9]", text2)  # символьные классы, если хотим найти 55, можно в таком виде r"[0-9]"
match5 = re.findall(r"[-0-9][0-9]", text2)  # символьные классы, если хотим найти -5, можно в таком виде r"[-0-9]", дефис или любую число от 0-9
match6 = re.findall(r"[^0-9]", text2)  # символьные классы, если хотим вывести все символы кроме числ
match7 = re.findall(r"[а-я]", text2)  # символьные классы, если хотим вывести все маленькие алфавиты
match8 = re.findall(r"[а-яА-Я]", text2)  # символьные классы, если хотим вывести все алфавиты
match9 = re.findall(r"[а-яА-Я0-9]", text2)  # символьные классы, если хотим вывести все алфавиты и цифры
match10 = re.findall(r"[\d]", text2)  # символьные классы, у всех символа есть своя значения можно по гуглить, еще существует re.ASCII
text3 = "0xf, 0xa, 0x5"
match11 = re.findall(r"0x[\da-fA-F]", text3) # символьные классы, существует стандартные наборы - \d, кроме .
print(match2)
print(match3)
print(match4)
print(match5)
print(match6)
print(match7)
print(match8)
print(match9)
print(match10)
print(match11)
