import pandas as pd
import altair as alt
import altair_saver



# function for overall negativity over time
def neg_chart(df,  time_unit):
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
def pos_chart(df,  time_unit):
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
def neu_chart(df,  time_unit):
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
def com_chart(df,  time_unit):
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
def charts(df,  time_unit):
    neg = neg_chart(df,  time_unit)
    pos = pos_chart(df,  time_unit)
    neu = neu_chart(df,  time_unit)
    com = com_chart(df,  time_unit)

    overall = neg & pos & neu & com

    return overall
    
uk = pd.read_csv('data/ukrainekyiv.csv')
ru = pd.read_csv('data/russiakyiv.csv')

uk_overall = charts(uk, 'monthdate')
ru_overall = charts(ru, 'monthdate')

complete = uk_overall | ru_overall

complete.save('visualizations/kyiv.html')