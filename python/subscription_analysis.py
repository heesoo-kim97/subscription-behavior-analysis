import pandas as pd

client_details = pd.read_csv("data/client_details.csv")

subscription_records = pd.read_csv(
    "data/subscription_records.csv",
    parse_dates=["start_date", "end_date"]
)

economic_indicators = pd.read_csv(
    "data/economic_indicators.csv",
    parse_dates=["start_date", "end_date"]
)

economic_indicators = economic_indicators.drop(
    columns=["Unnamed: 0"]
)

subscription_records["subscription_days"] = (
    subscription_records["end_date"]
    - subscription_records["start_date"]
).dt.days


datasets = {
    "CLIENT DETAILS": client_details,
    "SUBSCRIPTION RECORDS": subscription_records,
    "ECONOMIC INDICATORS": economic_indicators
}

for name, df in datasets.items():
    print(f"\n{name}")
    print("-" * len(name))
    print("Shape:", df.shape)
    print("Columns:", list(df.columns))
    print("\nData types:")
    print(df.dtypes)


for name, df in datasets.items():
    print(f"\n{name}")
    print("Missing values:")
    print(df.isnull().sum())
    print("Duplicate rows:", df.duplicated().sum())
