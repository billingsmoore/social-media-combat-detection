import pandas as pd

oblast_list = ['Chekasy', 
    'Chernihiv',  
    'Chernivtsi',  
    'Dnipro-petrovsk',  
    'Donetsk',  
    'Ivano-Frankivsk',  
    'Kharkiv',   
    'Kherson',  
    'Khmelnytskyi',  
    'Kyiv',  
    'Kirovohrad',  
    'Luhansk',  
    'Lviv',  
    'Mykolaiv',  
    'Odessa',  
    'Poltava',  
    'Rivne', 
    'Sumy ', 
    'Ternopil', 
    'Vinnytsia', 
    'Volyn', 
    'Zakarpattia', 
    'Zaporizhzhia', 
    'Zhytomyr', 
    'Crimea', 
    'Sevastopol']

russian = pd.read_csv('../sentimental-data/merged-data/russia_with_battles.csv')

ukrainian = pd.read_csv('../sentimental-data/merged-data/ukraine_with_battles.csv')

out = pd.DataFrame(columns=['uk_negativity','uk_neutrality','uk_positivity','uk_compound','uk_fighting','uk_2before',
                            'ru_negativity','ru_neutrality','ru_positivity','ru_compound','ru_fighting','ru_2before'])

for oblast in oblast_list:
    uk = ukrainian.loc[ukrainian['oblast'] == oblast]
    ru = russian.loc[ukrainian['oblast'] == oblast]

    uk_daily_means = uk.groupby(pd.to_datetime(uk['datetime']).dt.date)[['negativity', 'neutrality', 'positivity', 'compound', 'fighting', '2before']].mean()
    ru_daily_means = ru.groupby(pd.to_datetime(ru['datetime']).dt.date)[['negativity', 'neutrality', 'positivity', 'compound', 'fighting', '2before']].mean()

    uk_daily_means.rename(columns = {'negativity' : 'uk_negativity',
                                    'neutrality': 'uk_neutrality',
                                    'positivity' : 'uk_positivity',
                                    'compound' : 'uk_compound',
                                    'fighting': 'uk_fighting',
                                    '2before': 'uk_2before'}, inplace=True)

    ru_daily_means.rename(columns = {'negativity' : 'ru_negativity',
                                    'neutrality': 'ru_neutrality',
                                    'positivity' : 'ru_positivity',
                                    'compound' : 'ru_compound',
                                    'fighting': 'ru_fighting',
                                    '2before': 'ru_2before'}, inplace=True)

    daily_means = uk_daily_means.join(ru_daily_means, on='datetime')

    out = pd.concat([out, daily_means])
# export results
out.to_csv('../sentimental-data/merged-data/complete.csv')

