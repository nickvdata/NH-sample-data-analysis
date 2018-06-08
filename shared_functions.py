# plot_bar to plot bar chartdef

def plot_bar(x_value, y_value):
    df_grouped_bar = df.groupby([x_value], as_index = False).sum()
    df_grouped_bar.sort_values(x_value)
    data  = [go.Bar(
            x=df_grouped_bar[x_value],
            y=df_grouped_bar[y_value]
    )]
    plotly.offline.iplot(data)


#plot_box to plot a box chart

def plot_box(y_value,x_value):
    df.sort_values(x_value)

    trace0 = go.Box(
        y=df[y_value],
        x=df[x_value],
         boxpoints = 'suspectedoutliers',
        name = y_value
    )

    data1 = [trace0]
    layout1 = go.Layout(
        yaxis=dict(
            title=y_value,
            zeroline=True,
            range = [range_1,range_2]
        ),
        boxmode='group'
    )

    fig1 = go.Figure(data=data1, layout=layout1)
    plotly.offline.iplot(fig1)

# plot_bubble to plot a bubble chart

def plot_bubble(variable, x_value, y_value, z_value):
    df_grouped_bubble = df.groupby([variable], as_index = False).sum()
    df_grouped_bubble.sort_values(variable)
    df_grouped_bubble.iplot(kind='bubble', x=x_value, y=y_value, size=z_value, text=variable, categories = variable,
             xTitle=x_value, yTitle=y_value, title = x_value+' vs '+y_value+' with bubble size indicating '+z_value)
