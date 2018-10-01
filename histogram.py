import numpy as np

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *


def plot_overlaid_histograms(coin_hist, nba_hist, title, xaxis, yaxis, filename):
    coin_hist = go.Histogram(
        x=coin_hist,
        name='Coins',
        opacity=0.75
    )
    nba_hist = go.Histogram(
        x=nba_hist,
        name='NBA',
        opacity=0.75
    )

    data = [coin_hist, nba_hist]
    layout = go.Layout(
        title=title,
        xaxis=dict(title=xaxis),
        yaxis=dict(title=yaxis),
        barmode='overlay')
    fig = go.Figure(data=data, layout=layout)

    plotly.offline.plot(fig, filename=filename)
