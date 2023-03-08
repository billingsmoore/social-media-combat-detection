from selenium import webdriver

def get_html(url, filename):
    # Use Chrome as the browser
    browser = webdriver.Chrome()

    # Navigate to the URL
    browser.get(url)
    browser.implicitly_wait(100)
    # Get the source HTML of the page
    source = browser.page_source

    # Close the browser
    browser.quit()

    # Save source file
    with open(filename, 'w') as f:
            f.write(source)

