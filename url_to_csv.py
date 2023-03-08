import get_html
import html_to_csv

for i in range(2,6):
    url = 'https://ukraine.osintukraine.com/2023-01_' + str(i) + '.html'
    filename = '2023-1_' + str(i) + '.html'
    get_html.get_html(url, filename)
    html_to_csv.html_to_csv(filename)
