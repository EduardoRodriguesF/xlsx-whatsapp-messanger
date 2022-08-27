import json
import pandas
from os.path import abspath

def get_sheets_data():
    sheets_path = abspath('data/data.xlsx')

    excel_data = pandas.read_excel(sheets_path)
    
    json_str = excel_data.to_json(orient='records')

    result = json.loads(json_str)

    return result
