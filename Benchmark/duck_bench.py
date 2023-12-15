from time import perf_counter
from cfg import *
import duckdb


def test():
    res = []
    duckdb.install_extension("sqlite")
    conn = duckdb.connect("mydatabase.db")
    cursor = conn.cursor()
    for i in range(count):
        total = 0
        for j in range(attempts):
            start = perf_counter()
            cursor.execute(queries[i].replace('''STRFTIME('%Y', "tpep_pickup_datetime")''', '''EXTRACT(year FROM "tpep_pickup_datetime")'''))
            finish = perf_counter()
            total += finish - start
        res.append(total / attempts)
    cursor.close()
    conn.close()
    print("DuckDB:    ", format(res[0], '.3f'), format(res[1], '.3f'), format(res[2], '.3f'), format(res[3], '.3f'), sep='     ')

