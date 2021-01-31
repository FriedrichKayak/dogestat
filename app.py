
import requests

response = requests.get("https://chain.so/api/v2/get_price/DOGE/USD")

if response.status_code == 200:
    content = response.json()
    print(f"Dogecoin price: {content['data']['prices'][0]['price']}")
else:
    print(f"Dogecoin price: Unavailable")