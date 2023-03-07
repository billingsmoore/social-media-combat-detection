from bs4 import BeautifulSoup

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
            while split_text[i + j] != '/>ORIGINAL':
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
        message_out.append(message)

    return message_out

# helper function to clean dates
def clean_dates(dates):
    for date in dates:
        # clean time
        date[0] = date[0][13:]
        # clean year
        date[-1] = date[-1][:4]
    
    return dates


# function to process html file into a list of messages. Each message is itself a list of words. 
# A message is an original telegram post in English.
def process(filename):

    # open and read in the html file
    file = open(filename, 'r')
    contents = file.read()
    soup = BeautifulSoup(contents, 'lxml')

    # convert html into text
    text = soup.text
    split_text = text.split()

    # retrieve messages from the text
    dates, messages = retrieve_messages(split_text)

    # clean the messages
    messages = clean_messages(messages)
    dates = clean_dates(dates)

    return dates, messages
