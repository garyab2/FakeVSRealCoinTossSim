import numpy as np

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *


def plot_overlaid_line_graphs(x, coin_hist, nba_hist, team, title, xaxis, yaxis, filename):
    coin_trace = go.Scatter(x=x, name='Coins',y=coin_hist)
    nba_trace = go.Scatter(x=x, name=team,y=nba_hist)

    data = [coin_trace,  nba_trace]

    layout = go.Layout(
        title=title,
        xaxis=dict(title=xaxis),
        yaxis=dict(title=yaxis),
        barmode='overlay')

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename=filename)
