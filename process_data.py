import assign_sentiments
import process_html
import csv
import pandas as pd
import enrich

# NOTE!!! This file is set to only process SAMPLE.HTML!

# retrieve dates and translated messages from the html
# then assign sentiment to each
# return a list of 3-tuples: (date, translated-message, sentiment-score)
def process_data(source):
    dates, messages = process_html.process(source)
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

    enrich.enrich(df)

    # export to csv
    csv_name = str(df['datetime'][0][:10]) + '.csv'
    df.to_csv(csv_name)


process_data('sample.html')
