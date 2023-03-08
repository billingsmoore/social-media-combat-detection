from bs4 import BeautifulSoup

filename = '2023-1_2.html'

file = open(filename, 'r')
contents = file.read()
soup = BeautifulSoup(contents, 'lxml')

text = soup.text
split_text = text.split()

dates = soup.find_all(class_='date')
clean_dates = []
for date in dates:
    clean_dates.append(date.text)


print(clean_dates)