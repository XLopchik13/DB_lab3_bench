import sqlite_bench
import pandas_bench
import duck_bench
import alchemy_bench
import psycopg_bench


print("Module/Query: ", "Query_1 |", "Query_2 |", "Query_3 |", "Query_4")
sqlite_bench.test()
pandas_bench.test()
duck_bench.test()
alchemy_bench.test()
psycopg_bench.test()
