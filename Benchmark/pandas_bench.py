from time import perf_counter
from cfg import *
from sqlalchemy import create_engine
import pandas


def test():
    res = []
    engine = create_engine("sqlite:///mydatabase.db")
    for i in range(count):
        total = 0
        for j in range(attempts):
            start = perf_counter()
            pandas.read_sql(queries[i], con=engine)
            finish = perf_counter()
            total += finish - start
        res.append(total / attempts)
    engine.dispose()
    print("Pandas:    ", format(res[0], '.3f'), format(res[1], '.3f'), format(res[2], '.3f'), format(res[3], '.3f'), sep='     ')
