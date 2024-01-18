import os
import yfinance as yf
from datetime import datetime

# List of stock symbols
stock_symbols = [
    "AAPL", "ABBV", "ABT", "ACN", "ADBE", "AMD", "AMZN", "ASML", "AVGO",
    "AZN", "BABA", "BAC", "BRK-A", "CMCSA", "COST", "CRM", "CSCO", "CVX",
    "GOOGL", "HD", "INTC", "JNJ", "JPM", "KO", "LIN", "LLY", "MA", "MCD",
    "META", "MRK", "MSFT", "NFLX", "NVDA", "NVO", "NVS", "ORCL", "PDD",
    "PEP", "PG", "SAP", "SNY", "TM", "TMO", "TMUS", "TSLA", "TSM", "UNH",
    "V", "WMT", "XOM"
]


# Directory for storing CSV files
directory = "Stock_Data"
os.makedirs(directory, exist_ok=True)

# Download data for the past 5 years until January 1, 2024
end_date = "2024-01-01"
start_date = "2019-01-01"

for symbol in stock_symbols:
    # Fetch historical data
    data = yf.download(symbol, start=start_date, end=end_date)

    # Save data to a CSV file
    file_path = os.path.join(directory, f"{symbol}.csv")
    data.to_csv(file_path)

    print(f"Data for {symbol} saved to {file_path}")
