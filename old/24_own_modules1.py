# Собственный модуль lib.py
#  в виде 4-х функций
# Подключаем модуль Lib

# import lib
# import lib import summ
from old.lib import summ, diff, mul, div


def main():
    a, b = 5, 3

    print(f'Сумма чисел: {a} + {b} = {summ(a, b)}')
    print(f'Разность чисел: {a} - {b} = {diff(a, b)}')
    print(f'Произведение чисел: {a} * {b} = {mul(a, b)}')
    print(f'Частное от чисел: {a} : {b} = {div(a, b):.1f}')


if __name__ == '__main__':  # если этот файл исполняемый
    main()
