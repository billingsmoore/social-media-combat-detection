import pandas as pd

# load in ukraine
uk = pd.read_csv('../sentimental-data/merged-data/ukraine.csv')

uk = uk.drop(uk.oblast == '' or uk.oblast == 'n/a')

uk = uk.drop(columns=['Unnamed: 0', 'message', 'city'])

uk_daily_means = uk.groupby(pd.to_datetime(uk['datetime']).dt.date)[['negativity', 'neutrality', 'positivity', 'compound']].mean()


# load in russia
ru = pd.read_csv('../sentimental-data/kharkiv/russiakharkiv.csv')

ru = ru.drop(ru.oblast == '' or ru.oblast == 'n/a')

ru = ru.drop(columns=['Unnamed: 0', 'message', 'city'])

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

# export results

daily_means['fighting'] = daily_means.apply(add_battles, axis=1)

print(daily_means.head())

daily_means.to_csv('complete_data.csv')