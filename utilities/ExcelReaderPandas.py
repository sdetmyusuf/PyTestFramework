import pandas as pd

# # Load the Excel file — make sure the file is in your working directory
# file_path = 'your_file.xlsx'  # Replace with the actual file name or path
# sheet = 'Sheet1'  # Replace with your sheet name, or remove this line to use the default sheet

class ExcelReaderPandas:
    def __init__(self, file_path, sheetName):
        self.file_path = file_path
        self.sheetName = sheetName

    def readExcelUsingPandas (self, file_path, sheetName):
        try:
            # Read the Excel sheet
            df = pd.read_excel(file_path, sheetName)
            #
            # # Show the first 5 rows
            # print("Top 5 rows:")
            # print(df.head())
            # for value in df['username']:
            #     print(value)
            # print("----------------")
            # print(df['username'][0])
            # print(type(df['username'][0]))
            #
            # # Show basic info about the DataFrame
            # print("\nData summary:")
            # print(df.info())
            return df
        except FileNotFoundError:
            print("File not found. Please check the path.")
        except ValueError:
            print("Sheet name might be incorrect.")
        except Exception as e:
            print(f"Something went wrong: {e}")


objerp = ExcelReaderPandas("C://Users//Mohd Yusuf//PycharmProjects//PYTestFramework//ExcelFiles//LoginData.xlsx", "LoginData")
excelFileRead = objerp.readExcelUsingPandas ("C://Users//Mohd Yusuf//PycharmProjects//PYTestFramework//ExcelFiles//LoginData.xlsx", "LoginData")
print(excelFileRead['username'][0])
print(type(excelFileRead['username'].count()))