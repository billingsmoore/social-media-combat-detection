import pandas as pd

df = pd.read_csv('../sentimental-data/merged-data/russia-only-2-before.csv')

fights = df[df['fighting'] == 1]

no_fights = df[df['fighting'] == 0]

print(fights.head())
print(no_fights.head())