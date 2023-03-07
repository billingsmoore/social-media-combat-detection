import requests
import process_html

# not currently working
# need to contact site owner, may allow much, much easier scraping if i ask nicely

url = 'https://ukraine.osintukraine.com/2023-01.html#2023-01-01'
response = requests.get(url)

try:
    html_content = response.content

    with open('page.html', 'wb') as f:
        f.write(html_content)

    print(f'{url} download successful')

except:
    print(f'{url} failed to download!!!')

messages = process_html.process('page.html')

print(messages[:5])