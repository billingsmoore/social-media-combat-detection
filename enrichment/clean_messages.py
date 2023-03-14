import pandas as pd

filename = None

df = pd.read_csv(filename)

def clean_messages(row):
    message = row['message']
    # TODO
