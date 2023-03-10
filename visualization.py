import pandas as pd
import altair as alt

# need to refactor for more general archiving of visualizations
# right now it saves everything into test_viz

filename = 'test_csv/merged.csv'


# function for overall negativity over time
def overall_neg_chart(df):
    # Create a scatterplot of the negativity scores over time
    scatterplot = alt.Chart(df).mark_point().encode(
        x=alt.Color('datetime', timeUnit=time_unit),
        y='negativity',
        tooltip='message',
        color =alt.Color('oblast', legend=alt.Legend(title="Negative Sentiments")),
    )

    # Create a line graph of the daily means
    linegraph = alt.Chart(df).mark_line().encode(
        x=alt.Color('datetime', timeUnit=time_unit),
        y='mean(negativity)',
        color=alt.value('red'),
    )

    # Combine the scatterplot and line graph into a layered chart
    chart = (scatterplot + linegraph)

    # Display the chart
    #chart.save(path + 'neg_time.html')
    return chart
    

# function to make overall positivity over time chart
def overall_pos_chart(df):
    # Create a scatterplot of the scores over time
    scatterplot = alt.Chart(df).mark_point().encode(
        x=alt.Color('datetime', timeUnit=time_unit),
        y='positivity',
        tooltip='message',
        color =alt.Color('oblast', legend=alt.Legend(title="Positive Sentiments")),
    )

    # Create a line graph of the daily means
    linegraph = alt.Chart(df).mark_line().encode(
        x=alt.Color('datetime', timeUnit=time_unit),
        y='mean(positivity)',
        color=alt.value('red'),
    )

    # Combine the scatterplot and line graph into a layered chart
    chart = (scatterplot + linegraph)

    # Display the chart
    #chart.save(path + 'pos_time.html')
    return chart
    

# function to make overall neutrality  over time chart
def overall_neu_chart(df):
    # Create a scatterplot of the scores over time
    scatterplot = alt.Chart(df).mark_point().encode(
        x=alt.Color('datetime', timeUnit=time_unit),
        y='neutrality',
        tooltip='message',
        color =alt.Color('oblast', legend=alt.Legend(title="Neutral Sentiments")),
    )

    # Create a line graph of the daily means
    linegraph = alt.Chart(df).mark_line().encode(
        x=alt.Color('datetime', timeUnit=time_unit),
        y='mean(neutrality)',
        color=alt.value('red'),
    )

    # Combine the scatterplot and line graph into a layered chart
    chart = (scatterplot + linegraph)

    # Display the chart
    #chart.save(path + 'neu_time.html')
    return chart
    

# function to make overall compound over time chart
def overall_com_chart(df):
    # Create a scatterplot of the negativity scores over time
    scatterplot = alt.Chart(df).mark_point().encode(
        x=alt.Color('datetime', timeUnit=time_unit),
        y='compound',
        tooltip='message',
        color =alt.Color('oblast', legend=alt.Legend(title="Compound Sentiments")),
    )

    # Create a line graph of the rolling daily means
    linegraph = alt.Chart(df).mark_line().encode(
        x=alt.Color('datetime', timeUnit=time_unit),
        y='mean(compound)',
        color=alt.value('red'),
    )

    # Combine the scatterplot and line graph into a layered chart
    chart = (scatterplot + linegraph)

    # Display the chart
    #chart.save(path + 'com_time.html')
    return chart
    

# function to make all the overall charts
def overall_charts(df):
    neg = overall_neg_chart(df)
    pos = overall_pos_chart(df)
    neu = overall_neu_chart(df)
    com = overall_com_chart(df)

    overall = neg & pos & neu & com
    overall.save('test_viz/overall.html')

overall_charts(df)