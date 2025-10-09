# Файлы и запись словаря
# Домашнее задание
# Есть словарь, который нужно сохранить
# в файл и потом уметь его оттуда прочитать

d = {
    'стол': 'table',
    'стул': 'chair'
}

f = open('./files/info.txt', 'at+', encoding='utf8')  # файловый объект
f.seek(0)

for k, v in d.items():
    # f = open('./files/info.txt', 'at+', encoding='utf8')
    print(f'{k} : {v}', file=f)
    lines = f.readlines()
    lines = list(map(lambda x: x.strip(), lines))
#f = open('./files/info.txt', 'rt', encoding='utf-8')

    #while line := f.readline().strip():
    print(lines)

f.close()
