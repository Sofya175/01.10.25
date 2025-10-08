# Основные понятия в ООП
# Специальные методы
# __init__ - создание объекта
# __name__ - возвращает имя объекта(экземпляра) или модуля
# __sizeof__() - размер объекта в байтах
# __class__ - имя класса объекта
# __str__ - строковое представление объекта
# __repr__ - представление сложного объекта

# Всё есть объект - манипуляции с объектами
# a, b = 3, 4
#
# c = a + b  # "под капотом" -> a.__add__(b)
# c = a / b  # "под капотом" -> a.__div__(b)
# c = str(a) # "под капотом" -> a.__str__()

class A:
    def __init__(self, a=0):
        self.a = a

    # Переопределяем (override)
    # преобразование в строку
    def __str__(self):
        return f'<Объект класса A со значением a = {self.a}>'

    # Представление (representation) сложного объекта
    def __repr__(self):
        return f'<Объект класса A со значением a = {self.a}>'

    def __add__(self, other):
        return A(self.a + other.a)


class B:
    def __init__(self, b=0):
        self.b = b

    # Переопределяем (override)
    # преобразование в строку
    def __str__(self):
        return f'<Объект класса B со значением b = {self.b}>'

    # Представление (representation) сложного объекта
    def __repr__(self):
        return f'<Объект класса B со значением b = {self.b}>'

    def __sub__(self, other):
        return B(self.b - other.b)


a1 = A(10)
a2 = A(15)
c = a1 + a2

b1 = B(15)
b2 = B(10)

d = b1 - b2

print(c)
print(d)

# ----------------------------- oop5 cо спецметодами
# Student, Employee, Person
class Student:
    def __init__(self, u=''):
        self.university = u


class Employee:
    def __init__(self, c=''):
        self.company = c


class Person:
    def __init__(self, n=''):
        self.name = n


s = Student('Техноложка')
e = Employee('Авангард')
p = Person('Дима')

print(p.__class__.__name__)
print(p.__sizeof__())  # определяется размер файла в байтах

persons = [s, e, p]

for person in persons:
    # if person is Student:  # is идентичность, а не равенство
    # для кортежа: if person is Student or persons is Pupl:
    if isinstance(person, Student):  # можно классы подавать кортежем, н-р (Student, Pupl), isinstance - инстанция
        print(person.university)
    elif isinstance(person, Employee):
        print(person.company)
    else:
        print(person.name)
