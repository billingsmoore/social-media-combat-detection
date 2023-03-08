import pandas as pd

# this script will enrich the data extracted from the html

# dictionary of cities and oblast
locations = {
    'Kyiv': 'Kyiv',
    'Kharkiv': 'Kharkiv',
    'Odesa': 'Odesa',
    'Dnipro': 'Dnipro-petrovsk',
    'Donetsk': 'Donetsk',
    'Zaporizhzhia': 'Zaporizhzhia',
    'Lviv': 'Dnipro-petrovsk',
    'Kryvyi Rih': 'Dnipro-petrovsk',
    'Mykolaiv': 'Mykolaiv',
    'Sevastopol': 'Sevastopol',
    'Mariupol': 'Donetsk',
    'Luhansk': 'Luhansk',
    'Vinnytsia': 'Vinnytsia',
    'Makiivka': 'Donetsk',
    'Simferopol': 'Crimea',
    'Chernihiv': 'Chernihiv',
    'Kherson': 'Kherson',
    'Poltava': 'Poltava',
    'Khmelnytskyi': 'Khmelnytski',
    'Cherkasy': 'Cherkasy',
    'Chernivtsi': 'Chernivtsi',
    'Zhytomyr': 'Zhytomyr',
    'Sumy': 'Sumy',
    'Rivne': 'Rivne',
    'Horlivka': 'Donetsk',
    'Ivano-Frankivsk': 'Ivano-Frankivsk',
    'Kamianske': 'Dnipro-petrovsk',
    'Ternopil': 'Ternopil',
    'Lutsk': 'Volyn',
    'Bila Tserkva': 'Kyiv',
    'Kerch': 'Crimea',
    'Melitopol': 'Zaporizhzhia',
    'Kramatorsk': 'Donetsk',
    'Uzhhorod': 'Zakarpattia',
    'Brovary': 'Kyiv',
    'Yevpatoria': 'Crimea',
    'Berdiansk': 'Zaporizhzhia',
    'Nikopol': 'Dnipro-petrovsk',
    'Sloviansk': 'Donetsk',
    'Pavlohrad': 'Dnipro-petrovsk',
    'Konotop': 'Sumy',
    'Uman': 'Cherkasy',
    'Yalta': 'Crimea',
    'Berdychiv': 'Zhytomyr',
    'Stakhanov': 'Luhansk',
    'Shostka': 'Sumy',
    'Bakhmut': 'Donetsk',
    'Izmail': 'Odesa',
    'Novomosk': 'Dnipro-petrovsk',
    'Kolomyia': 'Ivano-Frankivsk',
    'Chornomorsk': 'Odesa',
    'Pryluky': 'Chernihiv',
    'Bilhorod-Dnistrovskyi': 'Odesa',
    'Okhtyrka': 'Sumy',
    'Izium': 'Kharkiv',
    'Varash': 'Rivne',
    'Netishyn': 'Khmelnytskyi',
    'Boyarka': 'Kyiv',
    'Obukhiv': 'Kyiv',
    'Hlukhiv': 'Sumy',
    'Mohyliv-Podilskyi': 'Vinnytsia',
    'Chortkiv': 'Ternopil',
    'Khust': 'Zakarpattia',
    'Balakliia': 'Kharkiv',
    'Lebedyn': 'Sumy',
    'Horodok': 'Khmelnytskyi',
    'Zhydachiv': 'Lviv',
    'Pochaiv': 'Ternopil',
    'Sviatohirsk': 'Donetsk',
}

def enrich(df):
    global locations
    cities = locations.keys()
    oblasts = locations.values()
    # iterate over rows in the dataframe and append location as two columns: city, oblast
    city_results = []
    oblast_results = []
    # try finding location from the text of the messages
    for index, row in df.iterrows():
        words = row['message'].split()
        city = 'n/a'
        oblast = 'n/a'
        for word in words:
            if word in cities:
                city = word
                oblast = locations[city]
            if oblast == 'n/a' and word in oblasts:
                oblast = word
        city_results.append(city)
        oblast_results.append(oblast)

    # add location to dataframe
    df['city'] = city_results
    df['oblast'] = oblast_results
    