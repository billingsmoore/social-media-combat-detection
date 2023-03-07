# this assigns sentiments to each message

#load in the lists
def load_lists():
    # open positives list
    with open("positive-words.txt", "r") as pos:
        pos_words = pos.read().split()

    # open negatives list
    with open("negative-words.txt", "r") as neg:
        neg_words = neg.read().split()

    return pos_words, neg_words

# assign sentiments to messages
def assign(messages):

    pos_words, neg_words = load_lists()
    sentiments = []

    for message in messages:
        sentiment = 0
        for word in message:
            if word in pos_words:
                sentiment += 1
            elif word in neg_words:
                sentiment -= 1
        sentiments.append(sentiment)
    
    return sentiments