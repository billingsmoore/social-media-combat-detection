import get_html
import html_to_csv

def scrape(start, end):
    for i in range(start, end + 1):
        # key info
        year = '2023'
        month = str(i)
        if len(month) < 2:
            month = '0' + month
        date = year + '-' + month
        last_page_num = 150

        # get the first page
        url = 'https://ukraine.osintukraine.com/' + date + '.html'
        filename = date + '_1'
        filename = get_html.get_html(url, filename)
        html_to_csv.html_to_csv(filename)

        for j in range(2,last_page_num):
            try:
                url = 'https://ukraine.osintukraine.com/'+ date + '_' + str(j) + '.html'
                filename = date + '_' + str(j)
                filename = get_html.get_html(url, filename)
                html_to_csv.html_to_csv(filename)
            except:
                break

scrape(1, 2)

print('Done!')