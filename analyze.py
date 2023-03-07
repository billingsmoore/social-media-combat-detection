import pandas as pd
import altair as alt

df = pd.read_csv('2023-01-01.csv')
df.columns = ['datetime', 'message', 'sentiment']

chart = alt.Chart(df).mark_point().encode(
    x='datetime',
    y='sentiment'
).save('chart.html')

