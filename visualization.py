import pandas as pd
import altair as alt

filename = 'test_csv/2023-1_2.csv'

df = pd.read_csv(filename)

neg_time = alt.Chart(df).mark_point().encode(
    x=alt.X('datetime', timeUnit='hours'),
    y='negativity',
    color =alt.Color('oblast', legend=alt.Legend(title="Negative Sentiments")),
    tooltip = 'message',
)

neg_time = neg_time + neg_time.transform_regression('datetime', 'negativity').mark_line()

neg_time.save('test_viz/neg_time.html')

neg_oblast = alt.Chart(df).mark_point().encode(
    x='oblast',
    y='negativity',
    color =alt.Color('datetime', timeUnit='hours', legend=alt.Legend(title="Negative Sentiments")),
    tooltip = 'message',
).save('test_viz/neg_oblasts.html')

