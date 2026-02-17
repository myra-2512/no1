import sqlite3

database = 'database(1).sqlite'

conn=sqlite3.connect(database)
print("Opened database successfully")   

import pandas as pd

tables=pd.read_sql("""SELECT * FROM sqlite_master
WHERE type='table';""", conn )

print(tables)

match=pd.read_sql("""SELECT * FROM Match;""", conn )

match.info()