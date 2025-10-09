# Основные понятия в ООП
# Полиморфизм (polymorphism - продолжение)
# Свойство кода работать с разными типами данных
# Функция isinstance(объект, класс) -> True или False
# Добавить необходимые поля, вывод об объекте, геттеры, сеттеры

# Student, Employee, Person
class Student:
    def __init__(self, u='', g=1000, n=''):
        self._university = u
        self._group = g
        self._surname = n

    def about_student(self):
        print(f'Студент:\n Наименование университета - "{self._university}",'
              f'\n номер группы - {self._group},'
              f'\n фамилия студента - {self._surname}.')

    # Setter (сеттер)
    def set_group(self, new_group):
        if 1000 < new_group < 6000:
            self._group = new_group
        else:
            print('Не верный номер группы')

    def set_surname(self, new_surname):
        if len(new_surname) > 3:
            self._surname = new_surname

    # Getter (геттеры)
    def get_university(self):
        return self._university

    def get_group(self):
        return self._group

    def get_surname(self):
        return self._surname


class Employee:
    def __init__(self, c='', j='', s1=''):
        self._company = c
        self._job = j
        self._surname = s1

    def about_employee(self):
        print(f'Сотрудник:\n Наименование организации - "{self._company}",'
              f'\n должность - {self._job},'
              f'\n фамилия - {self._surname}.')

    # Setter (сеттер)
    def set_surname(self, new_surname):
        if len(new_surname) > 3:
            self._surname = new_surname

    # Getter (геттеры)
    def get_company(self):
        return self._company

    def get_job(self):
        return self._job

    def get_surname(self):
        return self._surname


class Person:
    def __init__(self, n='', s2='', a=0):
        self._name = n
        self._surname = s2
        self._age = a

    def about_person(self):
        print(f'Персона:\n Имя - {self._name},'
              f'\n фамилия - {self._surname},'
              f'\n возраст - {self._age}.')

    # Setter (сеттер)
    def set_age(self, new_age):
        if 0 < new_age <= 125:
            self._age = new_age
        else:
            print('Недопустимое значение для возраста')

    def set_surname(self, new_surname):
        if len(new_surname) > 3:
            self._name = new_surname

    # Getter (геттеры)
    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_age(self):
        return self._age


s = Student('Техноложка', 1510, 'Петров')
# s.about_student()
e = Employee('Авангард', 'Инженер', 'Иванов')
# e.about_employee()
p = Person('Дима', 'Федоров', 15)
# p.about_person()

persons = [s, e, p]

for person in persons:
    if isinstance(person, Student):
        print(person.about_student())
    elif isinstance(person, Employee):
        print(person.about_employee())
    else:
        print(person.about_person())

# for person in persons:
#     if isinstance(person, Student):
#         print(person.__class__)
#     elif isinstance(person, Employee):
#         print(person.__class__)
#     else:
#         print(person.__class__)

# for person in persons:
#     if isinstance(person, Student):
#         print(person.university)
#     elif isinstance(person, Employee):
#         print(person.company)
#     else:
#         print(person.name)