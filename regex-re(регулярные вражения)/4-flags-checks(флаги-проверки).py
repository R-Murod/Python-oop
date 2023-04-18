# flags - флаги
# checks - проверка


import re

text = "подоходный налог, доход"
match = re.findall(r"прибыль|обретение|доход", text)  # доход в подоходный
match1 = re.findall(r"\bприбыль\b|\bобретение\b|\bдоход\b", text)  # если хотим найти отдельный доход то \bдоход\b, и каждому
match2 = re.findall(r"\b(прибыль|обретение|доход)\b", text)  # сохраняющуюся группировка
match3 = re.findall(r"\b(?:прибыль|обретение|доход)\b", text)  # не сохраняющуюся группировка
print(match)
print(match1)
print(match2)
print(match3)