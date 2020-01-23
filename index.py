import requests
import json

r = requests.get('https://api.coinbase.com/v2/currencies').json()

print("Get a list of all available cryptocurrencies and display it :")

for asset in r["data"]:
    print(asset["id"])

print("Create a function to display the ’ask’ or ‘bid’ price of an asset. Direction and asset name as parameters")


r = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell').json()

print(r)


print("Get order book for an asset")

r = requests.get('https://api-public.sandbox.pro.coinbase.com/products/BTC-USD/book').json()

print(r)


print("Create a function to read agregated trading data (candles) def refreshDataCandle(pair = 'BTCUSD',duration = '5m’)")

r = requests.get('https://api-public.sandbox.pro.coinbase.com/products/BTC-USD/candles?granularity=300').json()

print(r)


print("Create a function to extract all available trade data")

r = requests.get('https://api-public.sandbox.pro.coinbase.com/products/BTC-USD/trades').json()

print(r)


print("Create an order def createOrder (api_key, secret_key, direction, price, amount, pair = 'BTCUSD_d', orderType = 'LimitOrder’)")

payload = {'size': '0.01', 'price': '0.100', "side": "buy", "product_id": "BTC-USD", "type": "limit"}
r = requests.post("https://api-public.sandbox.pro.coinbase.com/orders", data=payload).json()

id = r["id"]

print(r)

print("Cancel an order def cancelOrder (api_key, secret_key, uuid)")

r = requests.get("https://api-public.sandbox.pro.coinbase.com/orders/" + id).json()

print(r)
