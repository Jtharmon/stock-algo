import alpaca_trade_api as tradeapi
import time

# Replace with your Alpaca API credentials
API_KEY = "PKKBCZZC6EFBNV5LIBN4"
API_SECRET = "74q52MtaJpNXeyq43cqYrtFbhfxowLWriqgzfp2J"
BASE_URL = "https://paper-api.alpaca.markets/v2"

# Initialize API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version="v2")

# Function to fetch live stock price
def get_live_price(ticker):
    barset = api.get_latest_bar(ticker)
    return barset.c

# Example: Fetch AAPL stock price in real-time
ticker = "AAPL"

while True:
    price = get_live_price(ticker)
    print(f"Live {ticker} Price: ${price:.2f}")
    time.sleep(1)  # Fetch price every second
