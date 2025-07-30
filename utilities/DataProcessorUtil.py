from utilities.ExcelReaderPandas import readExcelUsingPandas

class DataProcessor:
    def __init__(self, file_path, sheet_name):
        self.data = readExcelUsingPandas(file_path, sheet_name)

    def show_data(self):
        print(self.data.head())