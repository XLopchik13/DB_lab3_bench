# Бенчмарк "4 QUERIES"

## Оглавление

- [Оглавление](#оглавление)
- [Введение](#введение)
- [1 Запросы](#1-запросы)
- [2 Используемые библиотеки](#2-используемые-библиотеки)
  - [2.1 Sqlite3](#21-sqlite3)
  - [2.2 Pandas](#22-pandas) 
  - [2.3 Duckdb](#23-duckdb)
  - [2.4 SQLAlchemy](#24-sqlalchemy)
  - [2.5 Psycopg2](#25-psycopg2)
- [3 Инструкция по запуску](#3-инструкция-по-запуску)
- [4 Итоги запусков](#4-итоги-запусков)
- [Вывод](#Вывод)

***
## Введение
В данной лабораторной работе проводится тестирование и сравнение 5 python-библиотек 
для работы с данными. Тестирование включает в себя 4 запроса к базе данных. Итоги
сравнения будут представлены в виде таблиц и графиков. 

В бенчмарке будут участвовать:
* [SQLite3](https://docs.python.org/3/library/sqlite3.html) (встроенная в Python библиотека)
* [Pandas](https://pandas.pydata.org/docs/)
* [Duckdb](https://duckdb.org/docs/)
* [SQLalchemy](https://docs.sqlalchemy.org/en/20/)
* [Psycopg2](https://www.psycopg.org/docs/)

## 1 Запросы
```SQL
SELECT "VendorID", COUNT(*) 
FROM "trips" GROUP BY 1;
```
1. Этот запрос выполняет подсчёт кол-ва записей в таблице `trips` для каждого уникального значения столбца `VendorID` и группирует результаты по `VendorID`.

```SQL
SELECT "passenger_count", AVG("total_amount") 
FROM "trips" GROUP BY 1;
```
2. Этот запрос выполняет вычисление среднего значения стоимости поездки для каждого значения числа пассажиров в таблице `trips`.

```SQL
SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), COUNT(*)
FROM "trips" GROUP BY 1, 2;
```
3. Этот запрос извлекает информацию из таблицы `trips` о кол-ве пассажиров и годе по времени взятия такси, и подсчитывает кол-во записей, соответствующих каждому уникальному значению комбинации этих данных.

```SQL
SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*),
FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;
```
4. Этот запрос получает информацию из таблицы `trips` о кол-ве пассажиров, годе по времени взятия такси, округлённой дистанции поездки и подсчитывает кол-во записей для каждой комбинации этих данных. Итоговый результат сортируются по году взятия такси в порядке возрастания, а кол-во записей в каждой группе упорядочивается по убыванию.

## 2 Используемые библиотеки
### 2.1 Sqlite3
SQLite3 — встроенный модуль Python для работы с легковесной и простой
в использовании реляционная базы данных SQLite. 
Однако эта СУБД обладает довольно низкой производительностью.

**Использование:**

Для работы с модулем нам достаточно знать, что он работает файлами .db и
поддерживает стандартные для SQL операции. Основные шаги:
- Соединиться с файлом .db
- Создать курсор
- Выполнить SQL запрос
- Закрыть курсор и разорвать соединение с БД
```Python
import sqlite3

conn = sqlite3.connect(".db") # database name
...
cursor = conn.cursor()
cursor.execute(" ") # your SQL-query
...
cursor.close()
conn.close()
```

### 2.2 Pandas
Pandas - обширная библиотека для работы с **различными базами данных**, обладающая разнообразным
функционалом. Работа с данными в Pandas строится поверх другой 
Python-библиотеки - NumPy.

**Использование:**

Пример использование библиотеки при работе с SQLite:
```Python
import pandas
from sqlalchemy import create_engine

engine = create_engine("sqlite:///database.db") # database name 
...
pandas.read_sql(" ", con=engine) # your SQL-query
...
engine.dispose()
```

### 2.3 Duckdb
Duckdb - библиотека для работы с одноименной СУБД, поддерживающая SQL. 
База данных DuckDB отлично подходит для аналитических целей, 
так как предназначена для сложных запросов и большого объема данных, что
достигается за счёт векторизации выполнения запросов.

**Использование:**
```Python
import duckdb

duckdb.install_extension("sqlite")
conn = duckdb.connect(".db") # database name 
cursor = conn.cursor()
...
cursor.execute(" ") # your SQL-query
...
cursor.close()
conn.close()
```

### 2.4 SQLAlchemy
SQLAlchemy - это ORM для различных баз данных (MySQL, PostgreSQL, SQLite, 
Oracle и т.д.), что позволяет работать с базой данных, как с объектом языка
программирования со своими методами и атрибутами.

**Использование:**
```Python
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///mydatabase.db")
conn = engine.connect()
...
conn.execute(text(" ")) # your SQL-query
...
conn.close()
engine.dispose()
```

### 2.5 Psycopg2
Psycopg2 - фактически эта библиотека - это адаптер для Python,
позволяющий работать с базой данных PostgreSQL (мощная, открытая 
объектно-реляционная база данных, для работы с которой требуется
отдельный сервер). Основные преимущества - это потокобезопасность 
и возможность нескольких потоков работать с одним подключением. 

**Использование:**

- Соединиться с БД
- Создать курсор
- Выполнить SQL запрос
- Закрыть курсор и разорвать соединение с БД

```Python
import psycopg2
import pandas
from sqlalchemy import create_engine

my_db = {"dbname": " ", 
         "user": " ", 
         "password": " ", 
         "host": " ", 
         "port": int}  # your db info 
path = "postgresql://postgres:password@host:port/dbname" 

eng = create_engine(path)
connection = psycopg2.connect(**my_db)
cursor = connection.cursor()
...
cursor.execute(" ") # your SQL-query
...
cursor.close()
connection.close()
eng.dispose()
```

## 3 Инструкция по запуску
- Скачать файлы с данными [отсюда](https://drive.google.com/drive/folders/1usY-4CxLIz_8izBB9uAbg-JQEKSkPMg6)
- Поместить файлы в папку Benchmark 
- Отредактировать файл cfg.py
- Запустить main.py

## 4 Итоги запусков
_Во время тестирования использовалось два файла [отсюда](https://drive.google.com/drive/folders/1usY-4CxLIz_8izBB9uAbg-JQEKSkPMg6)._

- #### Итоги тестирования на данных размером ~200МБ:

| Module/Query | Query_1  | Query_2 | Query_3  | Query_4|
|--------------|----------|--------|----------|--------|
| SQLite3      | 0.647    | 1.241  | 2.193    | 4.254  |
| Pandas       | 0.824    | 1.827  | 3.030    | 4.245 |
| DuckDB       | 0.194    | 0.206   | 0.215    | 0.230  |
| SQLAlchemy   | 0.648   | 1.236  | 2.211    | 4.253  |
| Psycopg2     | 0.360    | 0.307  | 0.426    | 1.308  |


![](Benchmark/200mb.png)

- #### Итоги тестирования на данных размером ~2ГБ:

| Module/Query | Query_1 | Query_2 | Query_3  | Query_4 |
|--------------|---------|--------|----------|--------|
| SQLite3      | 9.525   | 11.454 | 20.666   | 46.478 |
| Pandas       | 7.789   | 19.856 | 33.739   | 46.356 |
| DuckDB       | 1.091   | 1.159  | 1.235    | 1.338  |
| SQLAlchemy   | 5.859   | 11.448 | 20.539   |  46.379|


![](Benchmark/2gb.png)

## Вывод 

В процессе тестирования 5 библиотек для работы с базами данных было выявлено, что:

- Наилучшую производительность на каждом датасете показала библиотека DuckDB. 
Это обусловлено тем, что данная библиотека специализируется на аналитических запросах
и оптимизирована под большие данные.
- На первом датасете второй по производительности оказалась Pcycopg2, однако на
втором датасете в следствие безумного потребления оперативной памяти и долгой
обработке данных, библиотека в статистике не участвует. Однако субд PostgreSQL
обладает гибкой настраиваемостью и возможно, что при должной оптимизации 
Psycopg2 также покажет хороший результат и на втором датасете.
- Оставшиеся три библиотеки (SQLite3, Pandas, SQLAlchemy) на каждом датасете 
показали приблизительно равную производительность, но в большинстве случаев самой
медленной оказалась библиотека Pandas в связке с субд SQLite. Однако такая низкая
скорость SQLite компенсируется её компактностью и простотой использования.
