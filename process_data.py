import assign_sentiments
import process_html



def process_data(source):
    data = []
    dates, messages = process_html.process(source)
    sentiments = assign_sentiments.assign(messages)
    for i in range(len(dates)):
        date = " ".join(dates[i])
        message = " ".join(messages[i])
        data.append((date, message, sentiments[i]))

    return data

dat = process_data('sample.html')

print(dat[:5])