# grouping - группировка
# preservation - сохранение
# работаем с круглыми скобками


import re

text = "lat = 5, lon=7 a=5"
match = re.findall(r"\w+\s*=\s*\d+", text)  # выводить из текста слова которые соот требованию
match1 = re.findall(r"lat\s*=\s*\d+|lon\s*=\s*\d+", text)  # выводить из текста слова которые начинаются с lat or lon
match2 = re.findall(r"(?:lat|lon)\s*=\s*\d+", text)  # группировка, сокращенный вид match1, ?: - не сох группировка
match3 = re.findall(r"(lat|lon)\s*=\s*(\d+)", text)  # группировка, сокращенный вид match2, ?: - сох группировка со ключом
print(match)
print(match1)
print(match2)
print(match3)

text1 = "<p> Картинка <img src='bg.jpg'> в тексте </p>"
match4 = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']", text1)
match5 = re.findall(r"<img\s+[^>]*src=([\"'])(.+?)\1", text1)  # сох () - ка, \1 - обращается к первому сох () - ку
# но это не правильна, так как может встретиться еще один соз () - ка
match6 = re.findall(r"<(img)\s+[^>]*src=(?P<q>[\"'])(.+?)(?P=q)", text1)  # сох () - ка, (?P=q) - обращается к q
print(match4)
print(match5)
print(match6)