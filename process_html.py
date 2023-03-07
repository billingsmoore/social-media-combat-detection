from bs4 import BeautifulSoup

# import html

file = open('sample.html', 'r')

contents = file.read()

soup = BeautifulSoup(contents, 'lxml')

text = soup.text

split_text = text.split()

# retrieve messages from html

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


# clean messages
removal_list = ['/>', '<br', 'TRANSLATION', ':', 'SUBSCRIBE']

for message in messages:
    for word in message:
        if word in removal_list:
            message.remove(word)

print(messages[:5])
