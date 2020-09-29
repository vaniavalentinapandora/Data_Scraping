import requests

#json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {'usd': {'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 6.7176004246166e-05, 'date': 'Mon, 28 Sep 2020 12:00:01 GMT', 'inverseRate': 14886.267964607},
             'eur': {'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 5.7746635270912e-05, 'date': 'Mon, 28 Sep 2020 12:00:01 GMT', 'inverseRate': 17317.026270165}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])



