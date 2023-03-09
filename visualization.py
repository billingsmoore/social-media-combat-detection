import pandas as pd
import altair as alt

# need to refactor for more general archiving of visualizations
# right now it saves everything into test_viz

filename = '../sentimental-data/merged-data/ukraine.csv'

my_path = '../sentimental-data/merged-data/'

df = pd.read_csv(filename)

# function for overall negativity over time
def overall_neg_chart(df, path):
    # Create a scatterplot of the negativity scores over time
    scatterplot = alt.Chart(df).mark_point().encode(
        x=alt.Color('datetime', timeUnit='month'),
        y='negativity',
        tooltip='message',
        color =alt.Color('oblast', legend=alt.Legend(title="Negative Sentiments")),
    )

    # Create a line graph of the daily means
    linegraph = alt.Chart(df).mark_line().encode(
        x=alt.Color('datetime', timeUnit='month'),
        y='mean(negativity)',
        color=alt.value('red'),
    )

    # Combine the scatterplot and line graph into a layered chart
    chart = (scatterplot + linegraph)

    # Display the chart
    chart.save(path + 'neg_time.html')
    return chart
    

# function to make overall positivity over time chart
def overall_pos_chart(df, path):
    # Create a scatterplot of the scores over time
    scatterplot = alt.Chart(df).mark_point().encode(
        x=alt.Color('datetime', timeUnit='month'),
        y='positivity',
        tooltip='message',
        color =alt.Color('oblast', legend=alt.Legend(title="Positive Sentiments")),
    )

    # Create a line graph of the daily means
    linegraph = alt.Chart(df).mark_line().encode(
        x=alt.Color('datetime', timeUnit='month'),
        y='mean(positivity)',
        color=alt.value('red'),
    )

    # Combine the scatterplot and line graph into a layered chart
    chart = (scatterplot + linegraph)

    # Display the chart
    chart.save(path + 'pos_time.html')
    return chart
    

# function to make overall neutrality  over time chart
def overall_neu_chart(df, path):
    # Create a scatterplot of the scores over time
    scatterplot = alt.Chart(df).mark_point().encode(
        x=alt.Color('datetime', timeUnit='month'),
        y='neutrality',
        tooltip='message',
        color =alt.Color('oblast', legend=alt.Legend(title="Neutral Sentiments")),
    )

    # Create a line graph of the daily means
    linegraph = alt.Chart(df).mark_line().encode(
        x=alt.Color('datetime', timeUnit='month'),
        y='mean(neutrality)',
        color=alt.value('red'),
    )

    # Combine the scatterplot and line graph into a layered chart
    chart = (scatterplot + linegraph)

    # Display the chart
    chart.save(path + 'neu_time.html')
    return chart
    

# function to make overall compound over time chart
def overall_com_chart(df, path):
    # Create a scatterplot of the negativity scores over time
    scatterplot = alt.Chart(df).mark_point().encode(
        x=alt.Color('datetime', timeUnit='month'),
        y='compound',
        tooltip='message',
        color =alt.Color('oblast', legend=alt.Legend(title="Compound Sentiments")),
    )

    # Create a line graph of the rolling daily means
    linegraph = alt.Chart(df).mark_line().encode(
        x=alt.Color('datetime', timeUnit='month'),
        y='mean(compound)',
        color=alt.value('red'),
    )

    # Combine the scatterplot and line graph into a layered chart
    chart = (scatterplot + linegraph)

    # Display the chart
    chart.save(path + 'com_time.html')
    return chart
    

# function to make all the overall charts
def overall_charts(df, path):
    neg = overall_neg_chart(df, path)
    pos = overall_pos_chart(df, path)
    neu = overall_neu_chart(df, path)
    com = overall_com_chart(df, path)

    overall = neg & pos & neu & com
    overall.save(path + 'overall-monthly.html')

overall_charts(df, my_path)