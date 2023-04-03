import pandas as pd
import statsmodels.formula.api as smf
from contextlib import redirect_stdout


df = pd.read_csv('../sentimental-data/merged-data/clean_complete.csv')

# print(df.head())

df = df[['uk_compound','ru_compound', 'fighting']]

model = smf.ols('fighting ~ uk_compound + ru_compound', data=df).fit()

# print(model.summary())

with open('modelsummary.txt', 'w') as f:
    with redirect_stdout(f):
        model.summary()