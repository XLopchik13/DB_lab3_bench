from time import perf_counter
from cfg import *
import psycopg2
import pandas
from sqlalchemy import create_engine


df = pandas.read_csv("tiny_data.csv")
df["tpep_pickup_datetime"] = pandas.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pandas.to_datetime(df["tpep_dropoff_datetime"])


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
    print("Psycopg2:  ", format(res[0], '.3f'), format(res[1], '.3f'), format(res[2], '.3f'), format(res[3], '.3f'), sep='     ')
