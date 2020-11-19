from tkinter import *
import requests
import json

pycrypto = Tk()
pycrypto.title('My Crypto Port')
pycrypto.iconbitmap(r'C:\Users\Boris\Desktop\favicon.ico')


def font_color(amount):
    if amount >= 0:
      return 'green'
    else:
      return 'red'

def my_portfolio():
    api_request = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=6&convert=USD&CMC_PRO_API_KEY=c07fd38f-24c9-4485-bed8-6e15a7f57f4f')
    api = json.loads(api_request.content)

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
    coin_row = 1
    total_current_value = 0

    for i in range(0,6):
          for coin in coins:
            if (api['data'][i]['symbol']) == coin['symbol']:
              total_paid = coin['amount_owned'] * coin['price_per_coin']
              current_value = coin['amount_owned'] * api['data'][i]['quote']['USD']['price']
              pl_per_coin = api['data'][i]['quote']['USD']['price'] - coin['price_per_coin']
              total_pl_coin = pl_per_coin * coin['amount_owned']

              total_pl = total_pl + total_pl_coin
              total_current_value = total_current_value + current_value

              #print(api['data'][i]['name']+ '-' + api['data'][i]['symbol'])
              #print('Price - ${0:.2f}'.format(api['data'][i]['quote']['USD']['price']))
              #print('Number_of_coin:', coin['amount_owned'])
              #print('Total amount paid:', '${0:.2f}'.format(total_paid))
              #print('Current Value:', '${0:.2f}'.format(current_value))
              #print('P/L per coin', '${0:.2f}'.format(pl_per_coin))
              #print('Total P/L per coin', '${0:.2f}'.format(total_pl_coin))
              #print('----------------')

              name = Label(pycrypto, text=api['data'][i]['symbol'], bg='white', fg='black', font='Calibri 12 ', padx='5', pady='5', borderwidth=2, relief='groove')
              name.grid(row=coin_row, column=0, sticky=N + S + E + W)

              price = Label(pycrypto, text='${0:.2f}'.format(api['data'][i]['quote']['USD']['price']), bg='white', fg='black', font='Calibri 12 ', padx='5', pady='5', borderwidth=2, relief='groove')
              price.grid(row=coin_row, column=1, sticky=N + S + E + W)

              num_coins = Label(pycrypto, text=coin['amount_owned'], bg='white', fg='black', font='Calibri 12 ', padx='5', pady='5', borderwidth=2, relief='groove')
              num_coins.grid(row=coin_row, column=2, sticky=N + S + E + W)

              amount_paid = Label(pycrypto, text='${0:.2f}'.format(total_paid), bg='white', fg='black', font='Calibri 12 ', padx='5', pady='5', borderwidth=2, relief='groove')
              amount_paid.grid(row=coin_row, column=3, sticky=N + S + E + W)

              current_val = Label(pycrypto, text='${0:.2f}'.format(current_value), bg='white', fg='black', font='Calibri 12 ', padx='5', pady='5', borderwidth=2, relief='groove')
              current_val.grid(row=coin_row, column=4, sticky=N + S + E + W)

              pl_coin = Label(pycrypto, text='${0:.2f}'.format(pl_per_coin), bg='white', fg=font_color(float('{0:.2f}'.format(pl_per_coin))), font='Calibri 12 ', padx='5', pady='5', borderwidth=2, relief='groove')
              pl_coin.grid(row=coin_row, column=5, sticky=N + S + E + W)

              totalpl = Label(pycrypto, text='${0:.2f}'.format(total_pl_coin), bg='white', fg=font_color(float('{0:.2f}'.format(total_pl_coin))), font='Calibri 12 ', padx='5', pady='5', borderwidth=2, relief='groove')
              totalpl.grid(row=coin_row, column=6, sticky=N + S + E + W)

              coin_row = coin_row + 1

    totalcv = Label(pycrypto, text='${0:.2f}'.format(total_current_value), bg='white', fg='black', font='Calibri 12 ',padx='5', pady='5', borderwidth=2, relief='groove')
    totalcv.grid(row=coin_row, column=4, sticky=N + S + E + W)

    totalpl = Label(pycrypto, text='${0:.2f}'.format(total_pl), bg='white', fg=font_color(float('{0:.2f}'.format(total_pl))), font='Calibri 12 ', padx='5',pady='5', borderwidth=2, relief='groove')
    totalpl.grid(row=coin_row, column=6, sticky=N + S + E + W)

    api= ''

    update = Button(pycrypto, text='Update', bg='white', fg='black',  font='Calibri 12 ', padx='5', pady='5',borderwidth=2, relief='groove')
    update.grid(row=coin_row + 1 , column=6, sticky=N + S + E + W)

    #print('Total P/L for Portfolio:', '${0:.2f}'.format(total_pl))


name = Label(pycrypto, text='Coin Name', bg='#142E54', fg='white', font='Calibri 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(pycrypto, text='Price', bg='#142E54', fg='white', font='Calibri 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
price.grid(row=0, column=1, sticky=N+S+E+W)

num_coins = Label(pycrypto, text='Coins Owned', bg='#142E54', fg='white', font='Calibri 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
num_coins.grid(row=0, column=2, sticky=N+S+E+W)

amount_paid = Label(pycrypto, text='Total Amount Paid', bg='#142E54', fg='white', font='Calibri 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
amount_paid.grid(row=0, column=3, sticky=N+S+E+W)

current_val = Label(pycrypto, text='Current Value', bg='#142E54', fg='white', font='Calibri 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
current_val.grid(row=0, column=4, sticky=N+S+E+W)

pl_coin = Label(pycrypto, text='P/L per coin', bg='#142E54', fg='white', font='Calibri 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
pl_coin.grid(row=0, column=5, sticky=N+S+E+W)

totalpl = Label(pycrypto, text='Total P/L with coin', bg='#142E54', fg='white', font='Calibri 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
totalpl.grid(row=0, column=6, sticky=N+S+E+W)

my_portfolio()

pycrypto.mainloop()
print('Program complete')


