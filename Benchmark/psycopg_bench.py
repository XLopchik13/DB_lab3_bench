from time import perf_counter
from cfg import *
import psycopg2
import pandas
from sqlalchemy import create_engine


df = pandas.read_csv("tiny_data.csv")
df["tpep_pickup_datetime"] = pandas.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pandas.to_datetime(df["tpep_dropoff_datetime"])
my_db = {"dbname": "postgres", "user": "postgres", "password": "your pass", "host": "localhost", "port": 5432}  # write your db info here
path = "postgresql://postgres:petrov2004@localhost:5432/postgres"


def test():
    res = []
    eng = create_engine(path)
    connection = psycopg2.connect(**my_db)
    df.to_sql("trips", eng, if_exists="replace")
    cursor = connection.cursor()
    for i in range(count):
        total = 0
        for j in range(attempts):
            start = perf_counter()
            cursor.execute(queries[i].replace('''STRFTIME('%Y', "tpep_pickup_datetime")''', '''EXTRACT(year FROM "tpep_pickup_datetime")'''))
            finish = perf_counter()
            total += finish - start
        res.append(total / attempts)
    cursor.close()
    connection.close()
    eng.dispose()
    print(res)
    return res
