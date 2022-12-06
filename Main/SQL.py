import pyodbc
import pandas as pd


def fire_results(product, result):
    cnxn_str = ("Driver={SQL Server};"
                "Server=MU00195249\ZEISSSQL;"
                "Database=InProcess;"
                "Trusted_Connection=yes;"
                "UID=sa;"
                "PWD=ZeissSql2015!;")
    cnxn = pyodbc.connect(cnxn_str)

    spectrum = '''SELECT * FROM InProcess.dbo.VSpectra'''
    data = pd.read_sql(spectrum, cnxn)

    result_name = data.ResultName.str.split(";", expand=True, )
    product_name = data.ProductName.str.split(";", expand=True, )

    wavelengths = data.Wavelengths.str.split(";", expand=True, )
    values = data.Values.str.split(";", expand=True, )

    class InProcessData:

        def __init__(self, product_class, result_class, column):
            self.product = product_class
            self.result = result_class
            self.column = column

        def get_data(self):
            transposed_data = self.column.transpose()
            result_name.rename(columns={0: 'ResultName'}, inplace=True)
            product_name.rename(columns={0: 'ProductName'}, inplace=True)
            result_index = result_name[result_name['ResultName'] == self.result].index.values
            product_index = product_name[product_name['ProductName'] == self.product].index.values
            data_index = list(set(product_index).intersection(result_index))
            recent_data_index = max(data_index)  # to get newest data with desired ProductName and ResultName
            transposed_data = transposed_data.iloc[:, recent_data_index]
            return transposed_data

    def joining_data(product_table, result_table):
        value_column = InProcessData(product_table, result_table, values).get_data()
        wavelength_column = InProcessData(product_table, result_table, wavelengths).get_data()
        table = [wavelength_column, value_column]
        results = pd.concat(table, axis=1, join="inner")
        print(results)
    return joining_data(product, result)

    cnxn.close()

#fire_results('test', 'Transmission')



