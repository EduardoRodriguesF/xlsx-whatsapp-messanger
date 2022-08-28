import json
import pandas
from os.path import abspath, join
from utils.phone_number import sanitize_phone, is_phone_valid

def get_sheets_data():
    sheets_path = join('data', 'data.xlsx')

    excel_data = pandas.read_excel(sheets_path)
    
    json_str = excel_data.to_json(orient='records')

    result = json.loads(json_str)

    return result

def for_each_valid_phone(callback):
    print('Converting .xlsx file into JSON')
    list = get_sheets_data()

    print('Done! Iterating through phones')

    for item in list:
        raw_phone = item.get('bot_phone') or item.get('Telefone') or ''

        phone = sanitize_phone(raw_phone)

        if not is_phone_valid(phone):
            print('Unable to resolve:', phone, 'from', raw_phone)
            continue

        callback(phone)
