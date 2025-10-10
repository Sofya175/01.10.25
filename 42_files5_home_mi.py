# Файлы и запись словаря
# Домашнее задание
# Есть словарь, который нужно сохранить
# в файл и потом уметь его оттуда прочитать

d = {
    'стол': 'table',
    'стул': 'chair'
}

f = open('./files/info.txt', 'wt', encoding='utf-8')  # файловый объект

for k, v in d.items():
    print(f'{k} : {v}', file=f)

f = open('./files/info.txt', 'rt', encoding='utf-8')

while line := f.readline().strip():
    print(line)

f.close()
