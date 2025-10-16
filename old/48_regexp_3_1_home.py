# Регулярные выражения (regular expression)
# Найти все email-адреса в строке

import re

text = "Свяжитесь с нами: support@mail.com, help@domain.org или info@example.net"
# pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
pattern = r'[\w\+]+@[\w\]+\.[\w\+]{1,}'
result = re.findall(pattern, text)
print(result)  # ['3', '15', '200']

email = "user@example.com"
pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
if re.match(pattern, email):
    print("Email корректный")
else:
    print("Неверный email")


result = re.split(r'[,;]', 'яблоко,банан;груша')
# ['яблоко', 'банан', 'груша']
# result = re.findall(pattern, text)
print(result)