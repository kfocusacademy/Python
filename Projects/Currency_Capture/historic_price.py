import requests
import csv
from datetime import datetime, timedelta

# Your API key
api_key = "2a29857fefb69de1f6c090a0e097cad4"

# Date range
end_date = datetime.today()
start_date = end_date - timedelta(days=0)
start = start_date.strftime("%Y-%m-%d")
end = end_date.strftime("%Y-%m-%d")

# Correct API endpoint
url = f"https://api.exchangerate.host/timeframe?start_date={start}&end_date={end}&base=USD&symbols=INR&access_key={api_key}"

response = requests.get(url)
data = response.json()
print(data)
# Check for success
if data.get("success"):
    with open("usd_inr_last_year.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "USD to INR"])
        for date, rates in sorted(data["rates"].items()):
            writer.writerow([date, rates["INR"]])
    print("✅ Data saved to usd_inr_last_year.csv")
else:
    print("❌ API error:", data.get("error", "Unknown issue"))
