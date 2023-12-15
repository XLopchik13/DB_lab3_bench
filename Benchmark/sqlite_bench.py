from time import perf_counter
import pandas
from cfg import *
import sqlite3
from pandas import read_csv

df = read_csv(file)
df["tpep_pickup_datetime"] = pandas.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pandas.to_datetime(df["tpep_dropoff_datetime"])


def test():
    res = []
    conn = sqlite3.connect("mydatabase.db")
    df.to_sql("trips", conn, if_exists="replace")
    cursor = conn.cursor()
    for i in range(count):
        total = 0
        for j in range(attempts):
            start = perf_counter()
            cursor.execute(queries[i])
            finish = perf_counter()
            total += finish - start
        res.append(total / attempts)
    cursor.close()
    conn.close()
    print("SQLite3:   ", format(res[0], '.3f'), format(res[1], '.3f'), format(res[2], '.3f'), format(res[3], '.3f'), sep='     ')
