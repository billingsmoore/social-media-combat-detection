import pandas as pd
import os

my_path = '../sentimental-data/russia/csv'

my_filename = 'russia'

def merge_csv(path, filename):
    
    df_files = []
    
    for f in os.listdir(path):
        df_temp = pd.read_csv(path + '/' + f)
        df_files.append(df_temp)
    
    df = pd.concat(df_files)
    
    df['datetime'] = pd.to_datetime(df['datetime'])

    df.to_csv('../sentimental-data/merged-data/' + filename + '.csv')

merge_csv(my_path, my_filename)