from time import perf_counter
from cfg import *
from sqlalchemy import create_engine, text


def test():
    res = []
    engine = create_engine(path)
    conn = engine.connect()
    for i in range(count):
        total = 0
        for j in range(attempts):
            start = perf_counter()
            conn.execute(text(queries[i].replace('''STRFTIME('%Y', "tpep_pickup_datetime")''', '''EXTRACT(year FROM "tpep_pickup_datetime")''')))
            finish = perf_counter()
            total += finish - start
        res.append(total / attempts)
    conn.close()
    engine.dispose()
    print("SQLAlchemy:", format(res[0], '.3f'), format(res[1], '.3f'), format(res[2], '.3f'), format(res[3], '.3f'), sep='     ')
