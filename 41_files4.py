# Файлы и работа с ними
# Построчная запись


f = open('./files/info.txt', 'rt', encoding='utf-8') # файловый объект (r - чтение, t - текстовый (по умолчанию)

f.seek(0) # если открыт как at+, то нужно сместиться в начало

# Оптимальный способ, если нет пустых строк до конца файла
while line := f.readline().strip():
    print(line)


lines = list(map(lamda x: x.strip(), lines))
lines = [x.strip() for x in lines]

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
f.close()
