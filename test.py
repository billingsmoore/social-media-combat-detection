import process_html
import assign_sentiments


filename = 'sample.html'

test_messages = [['This', 'is', 'a', 'day'],
                 ['This', 'is', 'a', 'terrible', 'day'],
                 ['This', 'is', 'a', 'hopeful', 'day'],
                 ['This', 'is', 'a', 'terrible', 'yet', 'hopeful', 'day']]


# test process_html on filename
#messages = process_html.process(filename)
#print(messages[:5])

# test analysis on test_messages
#sentiments = assign_sentiments.assign(test_messages)

# test analysis on sample.html
messages = process_html.process(filename)
sentiments = assign_sentiments.assign(messages)

print(sentiments)