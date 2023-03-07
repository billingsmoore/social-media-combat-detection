from bs4 import BeautifulSoup



# helper function to retrieve messages from html

def retrieve_messages(split_text):

    messages = []

    for i in range(len(split_text)):
        if split_text[i] == 'TRANSLATION':
            message = []
            message.append(split_text[i])
            j = 1
            while split_text[i + j] != '/>ORIGINAL':
                message.append(split_text[i + j])
                j += 1
            messages.append(message)

    return messages


# helper function to clean messages
def clean_messages(messages):

    removal_list = ['/>', '<br', 'TRANSLATION', ':', 'SUBSCRIBE']

    message_out = []

    for message in messages:
        for word in message:
            if word in removal_list:
                message.remove(word)
        message_out.append(" ".join(message))

    return message_out


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
    messages = retrieve_messages(split_text)

    # clean the messages
    messages = clean_messages(messages)

    return messages
