import assign_sentiments
import process_html
import csv

# NOTE!!! This file is set to only process SAMPLE.HTML!

# retrieve dates and translated messages from the html
# then assign sentiment to each
# return a list of 3-tuples: (date, translated-message, sentiment-score)
def process_data(source):
    data = []
    dates, messages = process_html.process(source)
    sentiments = assign_sentiments.assign(messages)
    for i in range(len(dates)):
        #clean up the format of the data points
        date = dates[i]
        message = messages[i]
        data.append((date, message, sentiments[i]))
    return data

# output the data into a summary csv file for archiving
def archive_result(data):
    # open the file in the write mode
    csv_name = str(data[0][0][:10]) + '.csv'
    with open(csv_name, 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        for row in data:
            # write a row to the csv file
            writer.writerow(row)

dat = process_data('sample.html')

archive_result(dat)