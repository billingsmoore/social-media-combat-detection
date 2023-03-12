import pandas as pd

def get_kharkiv(country):

    # open csv as dataframe
    filename = '../sentimental-data/merged-data/' + country + '.csv'
    df = pd.read_csv(filename)

    # select out only the kyiv rows
    df = df.loc[df['oblast'] == 'Kharkiv']

    # output to fresh kyiv csv
    df.to_csv('../sentimental-data/' + country + 'kharkiv.csv')

get_kharkiv('ukraine')
get_kharkiv('russia')
