import pandas_datareader.data as web
import pandas as pd
import yfinance as yf
import pickle
from pandas_datareader import data as pdr
from datetime import date
from datetime import timedelta
import certifi

certifi.where()
yf.pdr_override()

# Load the saved model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the stock symbol and the start and end dates for the historical data
symbol = 'SBIN.NS'
today = date.today()
yesterday = today - timedelta(days=1)

# Use the model to make a prediction for the next day's stock price
new_data = pdr.get_data_yahoo(symbol, start=yesterday, end=today)
print(new_data)

if len(new_data):
    X_new = new_data[['Open', 'High', 'Low', 'Volume']]
    y_new = model.predict(X_new)
    print("Predicted stock price for next market day: %.2f" % y_new)
else:
    print(f'no data found for {symbol}')

# URL = 'https://www1.nseindia.com/content/indices/ind_nifty50list.csv'
# df = pd.read_csv(URL, index_col='Company Name')
# print(df)
