import pandas as pd
import altair as alt

df = pd.read_csv('2023-01-01.csv')

chart = alt.Chart(df).mark_point().encode(
    x='datetime',
    y='negativity',
    color =alt.Color('oblast', legend=alt.Legend(title="Negative Sentiment in Ukrainian Telegram Messages")),
    tooltip = 'message',
).save('chart.html')

