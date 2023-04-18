# Методы для поиска вхождений
# pattern - регулярное выражение
# string - анализируемая строка
# flags - один или несколько флагов
# repl - строка или функция для замены найденного выражения
# count - максимальное число замен(если не указано, то неограниченно)
# re.match(pattern, string, flags)
# re.split(pattern, string, flags)
# re.sub(pattern, repl, string, count, flags)
# re.subn(pattern, repl, string, count, flags)
# re.compile(pattern, flags)


import re

text = "+7(123)456-78-90"
text1 = "sdhcnsdjcn; csdjcnjdc; jsdncsdm>"
text2 = """ Москва
Казань
Тверь
Самара
Уфа"""  # <option>Уфа</option> либо если хотим <option value='5'>Уфа</option> - тогда примем функцию к этому value

count = 0


def replFind(m):
    global count
    count += 1
    return f"<option value='{count}'>{m.group(1)}</option>\n"


match = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)  # re.match - ищет совпадений начиная с самого начало строки
match1 = re.split(r"[\n;,]+", text1)  # re.split - разбивает строки по указанному
match2 = re.sub(r"\s*(\w+)\s*", r"<option>\1</option>\n", text2)  # re.sub -
match3 = re.sub(r"\s*(\w+)\s*", replFind, text2)  # re.sub -
match4, total = re.subn(r"\s*(\w+)\s*", r"<option>\1</option>\n", text2)  # re.subn - посчитает количество замен
match5 = re.compile(r"\s*(\w+)\s*")  # re.compile - сначала компилируется потом можем использовать
list, total1 = match5.subn(r"<option>\1</option>\n", text2)
list2 = match5.sub(replFind, text2)
print(match)
print(match1)
print(match2)
print(match3)
print(match4, total)
print(list, total1, list2, sep="\n")
