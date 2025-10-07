# Собственный модуль lib.py
#  в виде 4-х функций


def summ(a: int, b: int) -> int:
    """
    Возвращает сумму
    :param a:
    :param b:
    :return:
    """
    return a + b


def diff(a: int, b: int) -> int:
    """
    Возвращает разность
    :param a:
    :param b:
    :return:
    """
    return a - b


def mul(a: int, b: int) -> int:
    """
    Возвращает произведение
    :param a:
    :param b:
    :return:
    """
    return a * b


def div(a: int, b: int) -> int:
    """
    Возвращает частное от двух чмсел
    :param a:
    :param b:
    :return:
    """
    if b != 0:
        return a / b


if __name__ == '__ main__':  # если этот файл исполняемый

    print('Запускайте файл "такой-то", в котором эта библиотека вызывается')
    print(__name__)
