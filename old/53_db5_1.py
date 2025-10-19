# Базы данных
# SQL - Structured Query Language
# Структурированный язык запоса
#CRUD - Create Read Update Delete
# % - набор любых символов от None до ...
# _ - один любой символ

# ЧТЕНИЕ

# SELECT * - выборка
# FROM books
# WHERE year BETWEEN 1967 AND 1970; - с 1967 до 1978
# WHERE year = (1967, 1970, 1987); - конкретные года
#------------------
# WHERE year IN (1967, 1970, 1987)
# ORDER BY year;
# ORDER BY year, title DESC; - сортировка в обратном порядке
#------------------
# SELECT title, year
#   FROM books
#  WHERE title LIKE '_еч%'
#------------------
# SELECT author, title, year
#   FROM books
#  WHERE author LIKE '_е%'
#------------------
# Вложенный запрос
# SELECT author,
#        title,
#        year
#   FROM books
#  WHERE genre_id = (
#                        SELECT id
#                          FROM genres
#                         WHERE name = 'Роман'
#                    );
# можно добавить ограничение вывода
# ORDER BY title
# LIMIT 5;
#------------------

# Объединение вывода из 2-х таблиц (Псевдонимы)
# SELECT b.*
# FROM books b
# JOIN genres g ON b.genre_id = g.id
# WHERE g.name LIKE 'Науч%'
#------------------
# SELECT b.title AS Книга,
#        b.author AS Автор,
#        g.name AS ЖАНР
#   FROM books b
#        JOIN
#        genres g ON b.genre_id = g.id
#  WHERE g.name LIKE 'Науч%';
#------------------

# SELECT g.name,
#        COUNT( * ) AS Количество
#   FROM books b
#        JOIN
#        genres g ON b.genre_id = g.id
#  GROUP BY g.name;
#------------------

# Вывод повторов
# SELECT title,
#        author,
#        COUNT( * )  AS count
#   FROM books
#  GROUP BY title,
#           author
# HAVING count > 1;

# ЗАПИСАТЬ, УДАЛИТЬ
# INSERT INTO books(title,author,genre_id, year)
# VALUES('Унесенные ветром','Маргарет Митчелл', 3, 1939);
#
# INSERT INTO books(title,author,genre_id, year)
# VALUES('Убийство в восточном экспрессе','Маргатта Кристи', 2, 1963),
# ('Великий Гэтсби','Френсис Скотт Фицжеральд', 3, 1967);
#
# UPDATE books
#    SET author = 'Агата Мэри Кларисса Миллер'
#  WHERE author = 'Агата Кристи';
#
# DELETE FROM books
#       WHERE id = 112;

