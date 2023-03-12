import pandas as pd

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

kharkiv_battles = [['24 February 2022 ', '14 May 2022 '],
                   ['3 March 2022', '1 April 2022'],
                   ['11 April 2022', '11 June 2022'],
                   ['5 August 2022', '6 September 2022 '],
                   ['6 September 2022', '8 September 2022 '],
                   ['7 September 2022 ', '8 September 2022'],
                   ['8 September 2022 ', '16 September 2022'],
                   ['6 September 2022', '2 October 2022']]

uk = pd.read_csv('../sentimental-data/kharkiv/ukrainekharkiv.csv')

uk = uk.drop(columns=['Unnamed: 0.2', 'Unnamed: 0.1', 'Unnamed: 0', 'message', 'city', 'oblast'])

uk_daily_means = uk.groupby(pd.to_datetime(uk['datetime']).dt.date)[['negativity', 'neutrality', 'positivity', 'compound']].mean()


# load in russia
ru = pd.read_csv('../sentimental-data/kharkiv/russiakharkiv.csv')

ru = ru.drop(columns=['Unnamed: 0.2', 'Unnamed: 0.1', 'Unnamed: 0', 'message', 'city', 'oblast'])

ru_daily_means = ru.groupby(pd.to_datetime(ru['datetime']).dt.date)[['negativity', 'neutrality', 'positivity', 'compound']].mean()


uk_daily_means.rename(columns = {'negativity' : 'uk_negativity',
                                 'neutrality': 'uk_neutrality',
                                 'positivity' : 'uk_positivity',
                                 'compound' : 'uk_compound'}, inplace=True)

ru_daily_means.rename(columns = {'negativity' : 'ru_negativity',
                                 'neutrality': 'ru_neutrality',
                                 'positivity' : 'ru_positivity',
                                 'compound' : 'ru_compound'}, inplace=True)

daily_means = uk_daily_means.join(ru_daily_means, on='datetime')




def add_battles(row):

    date = pd.to_datetime(row.name)
    for i in range(len(kharkiv_battles)):
        start = pd.to_datetime(kharkiv_battles[i][0]) 
        end = pd.to_datetime(kharkiv_battles[i][1])
        if date >= start and date <= end:
            return 'True'
    return 'False'

daily_means['fighting'] = daily_means.apply(add_battles, axis=1)

print(daily_means.head())

daily_means.to_csv('kharkiv_complete_data.csv')