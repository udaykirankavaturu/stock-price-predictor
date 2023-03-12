import pickle
import pandas_datareader.data as web
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import yfinance as yf

# Define the stock symbol and the start and end dates for the historical data
symbol = 'AAPL'
start = pd.to_datetime('2010-01-01')
end = pd.to_datetime('2023-03-10')

# Read the historical stock data from Yahoo Finance using pandas-datareader
data = yf.download(symbol, start, end)
print('reading completed')
print(data)

# Create the input features (X) and output variable (y)
X = data[['Open', 'High', 'Low', 'Volume']]
y = data['Close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create the linear regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)


# Use the model to make predictions on the testing data
predictions = model.predict(X_test)

# Print the model's score (R-squared value) on the testing data
score = model.score(X_test, y_test)
print("Model score: %.2f" % score)

# Save the model to a file using pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
