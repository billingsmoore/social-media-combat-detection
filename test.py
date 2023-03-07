import process_html as process_html
import assign_sentiments


filename = 'html_management/sample.html'

test_messages = [['This', 'is', 'a', 'day'],
                 ['This', 'is', 'a', 'terrible', 'day'],
                 ['This', 'is', 'a', 'hopeful', 'day'],
                 ['This', 'is', 'a', 'terrible', 'yet', 'hopeful', 'day']]


# test process_html on filename
dates, messages = process_html.process(filename)
print(dates[:5])
print(dates[-5:])
#print(messages[:5])

# test analysis on test_messages
#sentiments = assign_sentiments.assign(test_messages)

# test analysis on sample.html
#messages = process_html.process(filename)
#sentiments = assign_sentiments.assign(messages)

#print(sentiments)