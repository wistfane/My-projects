import requests
import json

api_request = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=6&convert=USD&CMC_PRO_API_KEY=c07fd38f-24c9-4485-bed8-6e15a7f57f4f')
api = json.loads(api_request.content)
print('----------------')
print('----------------')

coins = [
      {
        'symbol': 'BTC',
        'amount_owned': 2,
        'price_per_coin': 14200
       },
       {
        'symbol': 'ETH',
         'amount_owned': 35,
         'price_per_coin': 220
       },
       {
         'symbol':'XRP',
         'amount_owned': 1200,
         'price_per_coin': 0.14
       }
    ]

total_pl = 0

for i in range(0, 6):
    for coin in coins:
        if (api['data'][i]['symbol']) == coin['symbol']:
            total_paid = coin['amount_owned'] * coin['price_per_coin']
            current_value = coin['amount_owned'] * api['data'][i]['quote']['USD']['price']
            pl_per_coin = api['data'][i]['quote']['USD']['price'] - coin['price_per_coin']
            total_pl_coin = pl_per_coin * coin['amount_owned']

            total_pl = total_pl + total_pl_coin

            print(api['data'][i]['name'] + '-' + api['data'][i]['symbol'])
            print('Price - ${0:.2f}'.format(api['data'][i]['quote']['USD']['price']))
            print('Number_of_coin:', coin['amount_owned'])
            print('Total amount paid:', '${0:.2f}'.format(total_paid))
            print('Current Value:', '${0:.2f}'.format(current_value))
            print('P/L per coin', '${0:.2f}'.format(pl_per_coin))
            print('Total P/L per coin', '${0:.2f}'.format(total_pl_coin))
            print('----------------')
            print('Total P/L for Portfolio:', '${0:.2f}'.format(total_pl))