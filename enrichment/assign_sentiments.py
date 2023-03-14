import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# this assigns sentiments to each message

# assign sentiments to messages
def assign(messages):
    sentiments = []
    sia = SentimentIntensityAnalyzer()
    for message in messages:
        sentiment = sia.polarity_scores(message)
        sentiments.append(sentiment)
    return sentiments
