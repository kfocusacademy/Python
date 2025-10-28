import requests

api_key = "2a29857fefb69de1f6c090a0e097cad4"
# Where USD is the base currency you want to use
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD" 

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)