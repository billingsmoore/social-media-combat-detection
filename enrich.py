import pandas as pd

# this script will enrich the data extracted from the html
# start by opening the csv from data processing
filename = '2023-01-01.csv'
df = pd.read_csv(filename)
df.columns = ['datetime', 'message', 'sentiments']
# try finding location from the text of the messages

# load location lists
with open("locations/cities.txt", "r") as pos:
    cities = pos.read().split()

with open('locations/oblasts.txt', 'r') as pos:
    oblasts = pos.read().split()

#iterate over rows in the dataframe and append location as two columns: city, oblast
city_results = []
oblast_results = []
for index, row in df.iterrows():
    words = row['message'].split()
    city = 'n/a'
    oblast = 'n/a'
    for word in words:
        if word in cities:
            city = word
        if word in oblasts:
            oblast = word
    city_results.append(city)
    oblast_results.append(oblast)

# add location to dataframe
df['city'] = city_results
df['oblast'] = oblast_results

# export the enriched data to csv
csv_name = 'enriched_'+ filename
df.to_csv(csv_name)
