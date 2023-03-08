import get_html
import html_to_csv

# key info
year = '2022'
month = '04'
date = year + '-' + month
last_page_num = 20

# get the first page
url = 'https://ukraine.osintukraine.com/' + date + '.html'
filename = '2023-1'
filename = get_html.get_html(url, filename)
html_to_csv.html_to_csv(filename)

for i in range(2,last_page_num):
    url = 'https://ukraine.osintukraine.com/'+ date + '_' + str(i) + '.html'
    filename = '2023-1_' + str(i)
    filename = get_html.get_html(url, filename)
    html_to_csv.html_to_csv(filename)
