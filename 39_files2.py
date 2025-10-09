# Файлы и работа с ними
# Запись

f = open('./files/info.txt', 'wt', encoding='utf-8') # файловый объект (w - запись с нуля, t - текстовый (по умолчанию)

num = f.write('Привет, Python!')

print(f'В файл было записано {num} байт')
print(f.readable())

f.close()

