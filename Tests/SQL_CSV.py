import sys

import pyodbc
import pandas as pd

import numpy as np

cnxn_str = ("Driver={SQL Server};"
            "Server=MU00195249\ZEISSSQL;"
            "Database=InProcess;"
            "Trusted_Connection=yes;"
            "UID=sa;"
            "PWD=ZeissSql2015!;")

cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()
spectrum = '''SELECT ProductName, 
       ResultName,
	   Wavelengths,
	   [Values],
	   [Timestamp]
FROM InProcess.dbo.VSpectra'''


data = pd.read_sql(spectrum, cnxn)


df = data.ResultName.str.split(";", expand=True,)
df.rename(columns={0:'ResultName'}, inplace=True)
df_transpone = df.transpose()


wavelength = data.Wavelengths.str.split(";", expand=True,)
wavelength_transpone = wavelength.transpose()
dataframe = pd.DataFrame(wavelength_transpone, columns=['wavelength'])

values = data.Values.str.split(";", expand=True,)
values_transpone = values.transpose()


index = df[df['ResultName']=='Transmission'].index.values

wavelength_index = wavelength_transpone.iloc[:, index]
values_index = values_transpone.iloc[:, index]

result = pd.concat([wavelength_index, values_index], axis=1, join="inner")
#print(df_transpone.columns['Absorption'])


print(result)