# my_module.py
# Расчет факториала
х = input('Введите число для расчета факториала: ')

def factorial(x):
    # i = 0
    for i in range(x):
        x = x * (x - 1)
        print(f'Факториал =, {x}')
    return f"Факториал =, {x}"


#PI = 3.1415

# def greet(name):
#     return f"Привет, {name}!"
# PI = 3.1415
