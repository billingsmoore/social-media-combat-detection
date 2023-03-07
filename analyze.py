# this is where the real analysis will happen

import process_html

messages = process_html.process('sample.html')

print(messages[:5])