# Файлы и работа с ними
# Построчное чтение

f = open('./files/info.txt', 'rt', encoding='utf-8') # файловый объект (r - чтение, t - текстовый (по умолчанию)
#f = open('./files/info.txt', 'at+', encoding='utf8')  # файловый объект

f.seek(0) # если открыт как at+, то нужно сместиться в начало

lines = f.readlines()

# Через map
# lines = list(map(lambda x: x.strip(), lines))

# Через списочное выражение
lines = [x.strip() for x in lines]

for line in lines:
    if line:
        print(line)

# print(lines)
#----------------
#line1 = f.readline().strip()
#line2 = f.readline().strip()
#line3 = f.readline().strip()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
#
# print(line1, line2, line3)
# print(line1)
# print(line2)
# print(line3)
#print('Привет, мир!', end='...', file=f)
#-----------------

# Оптимальный способ (если нет пустых строк до конца файла)
# while line := f.readline().strip():
#     print(line)

f.close()


"""
Плохая практика:
line = None

while True:
    line = f.readline().strip()
    if line:
        print(line)
    else:
        break
"""