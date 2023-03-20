import pandas as pd

# define battle lists

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

chernihiv_battles = [['24 February 2022 ', '4 April 2022']]

dnipropetrovsk_battles = [['27 February 2022', '11 May 2022']]

poltava_battles = [['27 February 2022','11 May 2022']]

# donetsk has had an ongoing battle since feb 21, 2022
donetsk_battles = [['21 February 2022', '13 March 2023']]

kherson_battles = [['24 February 2022 ', '2 March 2022'],
                   ['27 May 2022', '16 June 2022'],
                   ['29 August 2022', '11 November 2022']]

mykolaiv_battles = [['29 August 2022', '11 November 2022'],
                    ['26 February 2022', '8 April 2022'],
                    ['2 March 2022', '3 March 2022'],
                    ['9 March 2022', '13 March 2022']]

odesa_battles = [['24 February 2022', '25 February 2022 ']]

sumy_battles = [['24 February 2022', '17 March 2022'],
                ['24 February 2022', '4 April 2022'],
                ['24 February 2022', '25 February 2022'],
                ['24 February 2022', '26 March 2022'],
                ['24 February 2022', '4 April 2022'],
                ['24 February 2022', '26 March 2022'],
                ['26 February 2022', '4 April 2022']]

zaporizhzhia_battles = [['25 February 2022', '1 March 2022'],
                        ['28 February 2022', '4 March 2022'],
                        ['5 March 2022', '13 March 2023']]

# luhansk has had an ongoing battle since may 5, 2022
luhansk_battles = [['15 March 2022', '12 May 2022'],
                   ['5 May 2022', '13 March 2023'],
                   ['18 March 2022', '7 May 2022'],
                   ['18 April 2022', '19 April 2022'],
                   ['5 May 2022', '13 May 2022'],
                   ['6 May 2022', '25 June 2022'],
                   ['10 May 2022', '21 June 2022'],
                   ['25 June 2022', '3 July 2022'],
                   ['2 October 2022', '13 March 2023']]

# put battle lists into dictionary for lookup
battle_dict = {'Kyiv': kyiv_battles,
               'Luhansk': luhansk_battles,
               'Chernihiv': chernihiv_battles,
               'Dnipro-petrovsk': dnipropetrovsk_battles,
               'Donetsk': donetsk_battles,
               'Kharkiv': kharkiv_battles,
               'Kherson': kherson_battles,
               'Mykolaiv': mykolaiv_battles,
               'Odesa': odesa_battles,
               'Sumy': sumy_battles,
               'Zaporizhzhia': zaporizhzhia_battles}


def add_battles(row):
    global battle_dict
    try:
        oblast = row['oblast']
        battles = battle_dict[oblast]
        date = pd.to_datetime(row['datetime'])
        for i in range(len(battles)):
            start = pd.to_datetime(battles[i][0])
            end = pd.to_datetime(battles[i][1])
            if date >= start and date <= end:
                return 1
        return 0
    except:
        return 2
    
def add_battles_before(row):
    global battle_dict
    try:
        oblast = row['oblast']
        battles = battle_dict[oblast]
        date = pd.to_datetime(row['datetime'])
        for i in range(len(battles)):
            start = pd.to_datetime(battles[i][0])-pd.Timedelta(days=2)
            end = pd.to_datetime(battles[i][0])
            if date >= start and date <= end:
                return 1
        return 0
    except:
        return 2
    
df = pd.read_csv('../sentimental-data/merged-data/ukraine.csv')

df['fighting'] = df.apply(add_battles, axis=1)

df = df[df['fighting'] != 2]

df['2before'] = df.apply(add_battles_before, axis=1)

df = df[df['2before'] != 2]

df = df.drop(columns=['city'])

df.to_csv('../sentimental-data/merged-data/ukraine_with_battles.csv')


