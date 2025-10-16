# Исключения  и конструкция их обработки
from sys import excepthook

# try:
#     пробуем провети операцию
# except ИмяИсключения:
#     если исключение было, то обработчик
# else: # если исключения не было (не обязательно)
#     тогда отдельный блок кода
# finally: # блок кода, который выполниться
#     в любом случае

# Пример 1
# try:
#     f = open('file.txt')
#     # print(f)
#     # какие-то действия
# except FileNotFoundError:
#     print('Файл не найден')
# else:
#     f.close()
#
# # Пример 2
# try:
#     namber = int(input('Введите число: '))
# except ValueError as exp:
#     print('Это не число, a', exp.args[0].split()[-1])
#
# # 3. Несколько исключений
# a = [0, 1, 2, 3]
# try:
#     index = int(input('Введите индекс: '))
#     result = 5 /a[index] + '2'
# except ZeroDivisionError:
#     print('Попытка деления на 0')
# except IndexError:
#     print('Такого индекса нет')
# except ValueError:
#     print('Индекс должен быть целым числом')
# else:
#     print('Удачно угадали индекс')
#     print('И получили результат -', result)
# finally:
#     try:
#         print('А индекс вводился такой: ', index)
#     except NameError:
#         print('Не смогли назначить индекс')

# Пример 4
# try:
#     age = int(input('Введите возраст человека: '))
#     if age < 0:
#         raise ValueError('Возраст не может быть отрицательным.')
#
# except ValueError as exp:
#     if exp.args[0].startswith('invalid'):
#         print('Надо вводить целое число, в не ', exp.args[0].split()[-1])
#     else:
#         print(exp)
# except Exception as e:
#     print('Непредвиденная ситуация: ', e)
# else:
#     print('Введен возраст: ', age)

# Пример 5
# class Exceple:
#     pass
#
# exceple = Exceple()
#
# try:
#     print(exceple.info())
# except Exception as e:
#     print('Непредвиденная ситуация: ', e)


# Пример 6
# try:
#     password = input('Введите пароль: ')
#     assert len(password) > 8
# except AssertionError: # используют чаще в целях тестирования и отладки
#     print('Пароль слишком короткий.')
# else:
#     print('Успешный ввод.')

# Пример тестирования функции

def validate_email(email):
    assert '@' in email, 'E-mail должен содержать символ @'
    assert email.endswith(('.ru', '.org', '.com')), 'Домен для E-mail не указан'
    return True
# Сам тест
try:
    validate_email('test@example.com')
    validate_email('test#example.com')
    validate_email('test@example')
except AssertionError as e:
    print('Не прошел проверку: {e}', e)

# try:
#     a = 3 / 0
# except Exception as exp:
#     print(exp.__class__.__name__)
