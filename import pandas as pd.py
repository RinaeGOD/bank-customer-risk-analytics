import pandas as pd

# Load data
customers = pd.read_csv('data/customers.csv')
transactions = pd.read_csv('data/transactions.csv')
loans = pd.read_csv('data/loans.csv')

# Convert date
transactions['Date'] = pd.to_datetime(transactions['Date'])

# Remove duplicates
customers.drop_duplicates(inplace=True)
transactions.drop_duplicates(inplace=True)
loans.drop_duplicates(inplace=True)

# Handle missing values
customers.fillna(method='ffill', inplace=True)

print("Data cleaned successfully")