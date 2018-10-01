import numpy as np

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *

def plot_single_comparison_walks(x, coin_walk, nba_walk, label, title, yaxis, filename):
    coin_trace = go.Scatter(x=x, name='Coins', y=coin_walk)
    nba_trace = go.Scatter(x=x, name=label, y=nba_walk)

    data = [coin_trace, nba_trace]
    layout = dict(
        title=title,
        yaxis=dict(title=yaxis),
        barmode='overlay')
    fig = go.Figure(data=data, layout=layout)

    plotly.offline.plot(fig, filename=filename)


def get_overlaid_line_graphs(x, ys, labels):
    return [go.Scatter(x=x, name=labels[i], y=ys[i]) for i in range(len(ys))]


def plot_sub_line_graphs(traces1, traces2, title, yaxis, filename):
    layout = dict(
        title=title,
        yaxis=dict(title=yaxis),
        barmode='overlay')

    fig = plotly.tools.make_subplots(rows=1, cols=2, shared_yaxes=True)

    [fig.append_trace(trace1, 1, 1) for trace1 in traces1]
    [fig.append_trace(trace2, 1, 2) for trace2 in traces2]
    fig['layout'].update(**layout)

    plotly.offline.plot(fig, filename=filename)