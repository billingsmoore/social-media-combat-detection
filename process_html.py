from bs4 import BeautifulSoup
#import json 

file = open('sample.html', 'r')

contents = file.read()

soup = BeautifulSoup(contents, 'lxml')

text = soup.text

split_text = text.split()

messages = []


for i in range(len(split_text)):
    if split_text[i] == 'TRANSLATION':
        message = []
        print('message found: ')
        message.append(split_text[i])
        j = 1
        while split_text[i + j] != '/>ORIGINAL':
            #print(split_text[i + j])
            message.append(split_text[i + j])
            j += 1
        messages.append(message)
        #print(message)

for message in messages:
    message.join(' ')

print(messages)
