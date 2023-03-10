import pandas as pd

df = pd.read_csv('data/ukrainekyiv.csv')

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

def enrich_with_battles(df):
    global kyiv_battles
    for index, row in df.iterrows():
        for battle in kyiv_battles:
            # TODO
            #if row['datetime'] 