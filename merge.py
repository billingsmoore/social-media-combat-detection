import pandas as pd
import os

my_path = 'test_csv'

my_filename = 'merged'

def merge_csv(path, filename):
    
    df_files = []
    
    for f in os.listdir(path):
        df_temp = pd.read_csv(path + '/' + f)
        df_files.append(df_temp)
    
    df = pd.concat(df_files)
    
    df['datetime'] = pd.to_datetime(df['datetime'])

    df.to_csv(path + '/' + filename + '.csv')

merge_csv(my_path, my_filename)