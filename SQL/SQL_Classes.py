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

result_name = data.ResultName.str.split(";", expand=True, )
product_name = data.ProductName.str.split(";", expand=True, )

wavelengths = data.Wavelengths.str.split(";", expand=True, )
values = data.Values.str.split(";", expand=True, )


class InProcessData:

    def __init__(self, product, result, column):
        self.product = product
        self.result = result
        self.column = column

    def get_data(self):
        transposed_data = self.column.transpose()
        result_name.rename(columns={0: 'ResultName'}, inplace=True)
        product_name.rename(columns={0: 'ProductName'}, inplace=True)
        result_index = result_name[result_name['ResultName'] == self.result].index.values
        product_index = product_name[product_name['ProductName'] == self.product].index.values
        data_index = list(set(product_index).intersection(result_index))
        recent_data_index = max(data_index)  # to get newest data with desired ProductName and ResultName
        data = transposed_data.iloc[:, recent_data_index]
        return data





def joining_data(table):
    results = pd.concat(table, axis=1, join="inner")
    print(results)


example1 = InProcessData('test', 'Transmission', values).get_data()

print(example1)

# transmission_wavelength = InProcessData('Transmission', wavelengths).get_data()
# transmission_values = InProcessData('Transmission', values).get_data()
#
# table_example = [transmission_wavelength, transmission_values]
#
#
# joining_data(table_example)
#
