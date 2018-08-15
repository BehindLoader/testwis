import requests

def get_valute(valute):
    r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    return r.json()['Valute'].get(valute)