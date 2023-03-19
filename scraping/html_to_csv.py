import enrichment.assign_sentiments as assign_sentiments
import csv
import pandas as pd
from bs4 import BeautifulSoup

######################################################################################
# HTML Processing Helpers
######################################################################################
# helper function to retrieve messages from html

def retrieve_messages(split_text):
    #print(split_text)
    messages = []
    dates = []

    for i in range(len(split_text)):
        #extract dates
        if 'date\"' in split_text[i]:
            date = split_text[i:i+5]
            dates.append(date)

        #extract translated message
        if split_text[i] == 'TRANSLATION':
            message = []
            j = 1
            while split_text[i + j] != '/>ORIGINAL' and split_text[i + j] != 'ORIGINAL':
                message.append(split_text[i + j])
                j += 1
            messages.append(message)

    return dates, messages


# helper function to clean messages
def clean_messages(messages):

    removal_list = ['/>', '<br', 'TRANSLATION', ':', 'SUBSCRIBE']

    message_out = []

    for message in messages:
        for word in message:
            if word in removal_list:
                message.remove(word)
        message_out.append((" ".join(message)).replace('/>', '').replace('<br', '').replace('Kiev', 'Kyiv'))

    return message_out

# helper function to clean dates
def clean_dates(dates):
    clean_dates = []
    
    # if old scrape method worked then use old clean method
    for date in dates:
        # clean time
        date[0] = date[0][13:]
        # clean year
        date[-1] = date[-1][:4]
        clean_dates.append(pd.to_datetime(" ".join(date)).strftime('%Y-%m-%d %X'))

    
    return clean_dates


# function to process html file into a list of messages. Each message is itself a list of words. 
# A message is an original telegram post in English.
def process_html(filename):
    # open and read in the html file
    file = open(filename, 'r')
    contents = file.read()
    soup = BeautifulSoup(contents, 'lxml')

    # try to get dates from html
    clean_dates = []
    dates = soup.find_all(class_='date')
    for date in dates:
        clean_dates.append(date.text)

    # try to get messages from html
    clean_messages = []
    messages = soup.find_all(class_='text')
    for message in messages:
        clean_messages.append(message.text)

    # if that doesn't work, go the long way
    if clean_messages == [] or dates == []:
        # convert html into text
        text = soup.text
        split_text = text.split()

        # retrieve messages from the text
        dates, messages = retrieve_messages(split_text)

        # clean the messages and dates
        clean_messages = clean_messages(messages)
        clean_dates = clean_dates(dates)

    return clean_dates, clean_messages

######################################################################################
# Enrichment Helpers
######################################################################################
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

#######################################################################################
# turn HTML into a CSV
#######################################################################################

# retrieve dates and translated messages from the html
# then assign sentiment to each
# return a list of 3-tuples: (date, translated-message, sentiment-score)
def html_to_csv(file):
    dates, messages = process_html(file)
    sentiments = assign_sentiments.assign(messages)
    # create dataframe
    # split sentiments into separate columns {'neg': 0.153, 'neu': 0.847, 'pos': 0.0, 'compound': -0.4404}
    neg = []
    neu = []
    pos = []
    compound = []
    for sentiment in sentiments:
        neg.append(sentiment['neg'])
        neu.append(sentiment['neu'])
        pos.append(sentiment['pos'])
        compound.append(sentiment['compound'])

    d = {'datetime': dates, 'message': messages, 'negativity': neg, 'neutrality': neu, 'positivity': pos, 'compound': compound}
    df = pd.DataFrame(data=d)

    enrich(df)

    # export to csv
    csv_name = '../sentimental-data/csv/' + file[25:-5] + '.csv'
    df.to_csv(csv_name)
