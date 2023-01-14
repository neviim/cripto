import json
import requests

key = "https://api.binance.com/api/v3/ticker/price?symbol="

currencies = ["BTCUSDT", "ETHUSDT", "LTCUSDT"]
j = 0

# running loop to print all crypto prices
for i in currencies:

	# completing API for request
	url = key+currencies[j]
	data = requests.get(url)
	data = data.json()
	j = j+1
	print(f"{data['symbol']} price: {data['price']}")

