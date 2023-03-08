import pandas as pd
import altair as alt

df = pd.read_csv('2023-01-01.csv')

chart = alt.Chart(df).mark_point().encode(
    x=alt.X('datetime', timeUnit='hours'),
    y='negativity',
    color =alt.Color('oblast', legend=alt.Legend(title="Negative Sentiment in Ukrainian Telegram Messages")),
    tooltip = 'message',
).save('negativity.html')

chart = alt.Chart(df).mark_point().encode(
    x=alt.X('datetime', timeUnit='hours'),
    y='positivity',
    color =alt.Color('oblast', legend=alt.Legend(title="Positive Sentiment in Ukrainian Telegram Messages")),
    tooltip = 'message',
).save('positivity.html')

chart = alt.Chart(df).mark_point().encode(
    x=alt.X('datetime', timeUnit='hours'),
    y='compound',
    color =alt.Color('oblast', legend=alt.Legend(title="Compound Sentiment in Ukrainian Telegram Messages")),
    tooltip = 'message',
).save('compound.html')