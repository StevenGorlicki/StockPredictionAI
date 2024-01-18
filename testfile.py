import yfinance as yf

# Fetch historical data for a stock (e.g., Apple Inc.)
data = yf.download('AAPL', start='2020-01-01', end='2021-01-25')
print(data.head())