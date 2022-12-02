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
spectrum = '''SELECT * FROM InProcess.dbo.VSpectra'''
data = pd.read_sql(spectrum, cnxn)

result_name = data.ResultName.str.split(";", expand=True,)
wavelengths = data.Wavelengths.str.split(";", expand=True,)
values = data.Values.str.split(";", expand=True,)
product_name = data.ProductName.str.split(";", expand=True,)


class InProcessData:

    def __init__(self, measurement_name, column_name):
        self.measurement_name = measurement_name
        self.column_name = column_name

    def get_data(self):
        transposed_data = self.column_name.transpose()
        result_name.rename(columns={0: 'ResultName'}, inplace=True)
        index = result_name[result_name['ResultName'] == self.measurement_name].index.values
        data = transposed_data.iloc[:, index]
        return data

def joining_data(table):
    results = pd.concat(table, axis=1, join="inner")
    print(results)


transmission_wavelength = InProcessData('Transmission', wavelengths).get_data()
transmission_values = InProcessData('Transmission', values).get_data()

table_example = [transmission_wavelength, transmission_values]


joining_data(table_example)
