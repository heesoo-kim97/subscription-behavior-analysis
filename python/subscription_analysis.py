import pandas as pd

# Load datasets
client_details = pd.read_csv("data/client_details.csv")

subscription_records = pd.read_csv(
    "data/subscription_records.csv",
    parse_dates=["start_date", "end_date"]
)

economic_indicators = pd.read_csv(
    "data/economic_indicators.csv",
    parse_dates=["start_date", "end_date"]
)

# Inspect datasets
print("CLIENT DETAILS")
print(client_details.head())
print(client_details.shape)

print("\nSUBSCRIPTION RECORDS")
print(subscription_records.head())
print(subscription_records.shape)

print("\nECONOMIC INDICATORS")
print(economic_indicators.head())
print(economic_indicators.shape)