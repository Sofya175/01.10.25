# Исключения - это не ошибка
# Исключения возникает run-time,
#   т.е. во время работы программы
#   исключительная ситуация


# 1. NameError - имя не определено
a = 3
try:
    print(b)
except NameError:
    print('Переменная b не была определена')

# 2. Деление на ноль
b = 0
try:
    print(a / b)
except ZeroDivisionError:
    print('На ноль делить нельзя')

# 3.Некорректный индекс
s = 'Python'
try:
    print(s[8])
except IndexError:
    print('Некорректный индекс')

# 4. Отсутствие файла для чтения
fname = 'non-ex'
try:
    f = open(fname)
except FileNotFoundError:
    print(f'Файла с именем {fname} не существует')

# 5. Некорректная операция с типами
x = 4
y = '5'
try:
    print(x+y)
except TypeError:
    print('Нельзя выполнять операции с данными разного типа')

# 6. Ошибка преобразования
z = '4F'
try:
     print(int(z))
except ValueError:
     print('Некоректное приведение типа')

# 7. Не знаем какое исключение
try:
    a = 3 / 0
except Exception as exp:
    print(exp.__class__.__name__)