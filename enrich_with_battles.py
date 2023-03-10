import pandas as pd

df = pd.read_csv('../sentimental-data/kyiv/ukrainekyiv.csv')

kyiv_battles = [['24 February 2022 ', '25 February 2022 '],
                ['24 February 2022 ', '24 February 2022 '],
                ['25 February 2022 ', '27 February 2022 '],
                ['25 February 2022 ', '1 April 2022'],
                ['26 February 2022', '26 February 2022'], 
                ['27 February 2022', '31 March 2022'],
                ['27 February 2022', '28 March 2022'],
                ['27 February 2022', '25 March 2022'],
                ['5 March 2022', '21 March 2022'],
                ['9 March 2022', '1 April 2022 '],
                ['18 March 2022', '27 March 2022'],
                ['25 February 2022 ', '31 March 2022']]

for battle in kyiv_battles:
    for date in battle:
        date = pd.to_datetime(date)

def enrich_with_battles(row):
    kyiv_battles = [['24 February 2022 ', '25 February 2022 '],
                ['24 February 2022 ', '24 February 2022 '],
                ['25 February 2022 ', '27 February 2022 '],
                ['25 February 2022 ', '1 April 2022'],
                ['26 February 2022', '26 February 2022'], 
                ['27 February 2022', '31 March 2022'],
                ['27 February 2022', '28 March 2022'],
                ['27 February 2022', '25 March 2022'],
                ['5 March 2022', '21 March 2022'],
                ['9 March 2022', '1 April 2022 '],
                ['18 March 2022', '27 March 2022'],
                ['25 February 2022 ', '31 March 2022']]
    for battle in kyiv_battles:
        if row['datetime'] >= battle[0] and row['datetime'] <= battle[1]:
            return True
    return False

df['fighting'] = df.apply(enrich_with_battles, axis=1)

print(df.head())