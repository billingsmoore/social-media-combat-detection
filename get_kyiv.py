import pandas as pd

def get_kyiv(country):

    # open csv as dataframe
    filename = 'data/' + country + '.csv'
    df = pd.read_csv(filename)

    # select out only the kyiv rows
    df = df.loc[df['oblast'] == 'Kyiv']

    # output to fresh kyiv csv
    df.to_csv('data/' + country + 'kyiv.csv')

get_kyiv('ukraine')
get_kyiv('russia')
