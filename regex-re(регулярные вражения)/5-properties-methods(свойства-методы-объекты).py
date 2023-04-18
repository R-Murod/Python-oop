# properties - свойства
# methods - методы
# Methods: re.search, re.findall and re.finditer
# pattern - регулярное выражение
# string - анализируемая строка
# flags - один или несколько флагов
# re.search(pattern, string, flags)
# re.finditer(pattern, string, flags)
# re.findall(pattern, string, flags)


import re
# method search - будет выделять только первый аттрибут, второй будет игнорирован
# method finditer - будет перебирать все аттрибуты текста
# method findall - если нам нужен на выходе получить просто список найденных вхождении

text = "<font color=#CC0000 bg=#ffffff>"
match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6}\b)",  text)
print(match)
for match1 in re.finditer(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6}\b)",  text):
    print(match1)
match2 = re.findall(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6}\b)",  text)
print(match2)
