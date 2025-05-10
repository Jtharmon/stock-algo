import yfinance as yf
import pandas as pd

def fetch_data(ticker='AAPL', start='2020-01-01', end='2023-12-31'):
    print(f"📥 Downloading data for {ticker}...")
    data = yf.download(ticker, start=start, end=end)
    data.to_csv('data/raw_data.csv')
    print("✅ Data saved to data/raw_data.csv")