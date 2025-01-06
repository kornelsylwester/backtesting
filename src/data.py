import pandas as pd


file = '/Users/kornelsylwester/Desktop/backtesting/src/candles XRP-USD start 2024-12-31 20:54:58.433022.csv'
df = pd.read_csv(file)


# df['start'] = pd.to_numeric(df['start'])
# print(df[df['start'] == 1735680240])

# filtered = df.iloc[0:20000]

market_data = df

