# Web-приложение

# GET - запрос (аналог READ)
# GET запрос
# https://static-maps.yandex.ru/1.x/?ll=30.325498,59.918305&spn=0.0025,0.0025&l=map&pt=30.325498,59.918305,pm2dgl
# POST  - аналог CREATE
# PUT - аналог UPDATE

# Flask - минимализм с возможностью расширения
# устанавливаем pip install flask
# pip freeze
# Django - все включено (не используем)

from flask import Flask, url_for
import sqlite3

app = Flask(__name__)  # name - модуль Питона 55_web1


@app.route('/')  # декоратор для функции index()
@app.route('/home')
def index():
    return """Я ваше первое приложение.
    <br> Подробнее <a href="/about">здесь</a>
    <br> А вот <a href="/countdown">тут</a> обратный отсчет"""


@app.route('/about')  # декоратор
def about():
    return """Эта страница с более подробной информацией.
    <br>А <a href="/genres"> вот тут </a> про жанры.
    <br>А <a href="/flag"> вот тут </a> будет флаг.
    <br> Подробнее <a href="/home">назад</a>"""


@app.route('/countdown')
def cdown():
    lst = [str(x) for x in reversed(range(11))]
    lst.append('Поехали!')
    return '<br>'.join(lst)  # join - соединение строк из списка


@app.route('/genres')
def genres():
    temp = []
    con = sqlite3.connect('db/books_bd.sqlite')
    cur = con.cursor()
    res = cur.execute("SELECT * FROM genres").fetchall()
    cur.close()
    con.close()
    for _, name in res:
        temp.append(name)
    temp = list(map(lambda x: '<li>' + x + '</li>', temp))
    res = '<br>'.join(temp)
    result = f"""
    <!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{url_for('static', filename="css/styles.css")}">
    <title>Жанры</title>
</head>
<body>
<h1>А вот и жанры:</h1>
<ul>
{res}
</ul>
</body>
</html>"""
    return result


@app.route('/flag')
def flag():
    # return """<img src=\"static/images/flag.jpg\"
    #         height="40" width"60"
    #         alt=\"Нету флага\">"""
    # ИЛИ через: url_for - соединяет директорию с файлом
    return f"""<img src="{url_for('static', filename='images/flag.jpg')}"
            height="40" width"60"
            alt=\"Нету флага\">"""

# <name> - строка
# <num:int> - целое
# <num:float> - дес. дробь
@app.route('/greet/', defaults={'name': None})
@app.route('/greet/<name>')
def greeting(name=None):
    if name is None:
        return '<h1>Не с кем здороваться!!!</h1>'
    return f"""
    <!DOCTYPE html>
<html lang="ru">
<head>
<!--    как будет отображаться на странице-->
    <meta charset="UTF-8">
    <meta name="description" content="Описание страницы сайта.">
    <link rel="stylesheet" href="{url_for('static', filename='css/styles.css')}">
    <title>Приветствуем тебя, {name}</title>
</head>
<body>
<h1>{name.capitalize()}, мы приветствуем тебя</h1>
</body>
</html>
    """


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)  # host или локальный хост, 5000 - классический порт для приложения flask
