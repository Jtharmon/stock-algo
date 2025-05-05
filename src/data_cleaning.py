import pandas as pd

def clean_data():
    df = pd.read_csv('data/raw_data.csv', index_col=0, parse_dates=True)

    # Define all possible numeric columns, but only use ones that exist in the file
    possible_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    numeric_columns = [col for col in possible_columns if col in df.columns]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df.dropna(inplace=True)

    if 'Close' in df.columns:
        df['Return'] = df['Close'].pct_change()
        df.dropna(inplace=True)

    df.to_csv('data/cleaned_data.csv')
    print("✅ Cleaned data saved to data/cleaned_data.csv")
    print("Columns in raw data:", df.columns.tolist())

