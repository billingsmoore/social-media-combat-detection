import pandas as pd
import altair as alt

filename = 'csv/2023-1_2.csv'

df = pd.read_csv(filename)

chart = alt.Chart(df).mark_point().encode(
    x=alt.X('datetime', timeUnit='hours'),
    y='negativity',
    color =alt.Color('oblast', legend=alt.Legend(title="Negative Sentiment in Ukrainian Telegram Messages")),
    tooltip = 'message',
).save('negativity.html')