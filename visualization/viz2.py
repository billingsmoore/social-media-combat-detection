import pandas as pd
import altair as alt
import seaborn
from statsmodels.api import OLS

df = pd.read_csv('../sentimental-data/kharkiv/kharkiv_complete_data.csv')

seaborn.scatterplot(df, x='datetime', y='uk_compound', hue='fighting').get_figure().savefig('uk.png')

seaborn.scatterplot(df, x='datetime', y='ru_compound', hue='fighting').get_figure().savefig('ru.png')

df2 = df[['uk_compound', 'ru_compound', 'fighting']]

seaborn.heatmap(df2.corr()).get_figure().savefig('heatmap.png')

seaborn.pairplot(df2).savefig('pairplot.png')