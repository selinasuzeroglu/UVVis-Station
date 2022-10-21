import pyodbc
import pandas as pd

cnxn_str = ("Driver={SQL Server};"
            "Server=MU00195249\ZEISSSQL;"
            "Database=InProcess;"
            "Trusted_Connection=yes;"
            "UID=sa;"
            "PWD=ZeissSql2015!;")

cnxn = pyodbc.connect(cnxn_str)

cursor = cnxn.cursor()

data = pd.read_sql(' SELECT * FROM result',cnxn)

print(data)
print(type(data))