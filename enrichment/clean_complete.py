import pandas as pd

df = pd.read_csv('../sentimental-data/merged-data/complete.csv')

df = df.dropna()

def get_fighting(row):
    if row['uk_fighting'] != 0 or row['ru_fighting'] != 0:
        return 1
    else:
        return 0
    
def get_2before(row):
    if row['uk_2before'] != 0 or row['ru_2before'] != 0:
        return 1
    else:
        return 0
    
df['fighting'] = df.apply(get_fighting, axis=1)
df['2before'] = df.apply(get_2before, axis = 1)

df = df.drop(columns=['Unnamed: 0', 'uk_fighting', 'ru_fighting', 'uk_2before', 'ru_2before'])

df.to_csv('../sentimental-data/merged-data/clean_complete.csv')