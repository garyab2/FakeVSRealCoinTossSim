import ast
import numpy as np
import pandas as pd

from coin_toss_sim import simulate_coin_toss
from line_graph import get_overlaid_line_graphs, plot_sub_line_graphs

TEAM = 'chicago_bulls' # snake case
YEAR = 2016
DISPLAY_NAME = 'Chicago Bulls'

def create_random_walk(record):
    walk = [0]
    for i in record:
        diff = 1 if int(i) == 1 else -1
        walk.append(walk[-1] + diff)
    return walk

def plot_random_walk():
    scores_df = pd.read_csv('scrape_data.csv')
    sub_df = scores_df[scores_df['Team'] == TEAM]

    random_walks = []
    years = []
    for i, row in sub_df.iterrows():
        record = ast.literal_eval(row['Record'])
        random_walks.append(create_random_walk(record))
        years.append(row.Year)

    coin_walks = [create_random_walk(simulate_coin_toss(len(record))) for _ in random_walks]
    x = list(range(0, len(record) + 1))

    nba_traces = get_overlaid_line_graphs(x, random_walks, years)
    coin_traces = get_overlaid_line_graphs(x, coin_walks, years)
    
    plot_sub_line_graphs(nba_traces, coin_traces, 'The Random Walks of The {} and Coin Tossing'.format(DISPLAY_NAME), 'Distance', 'multiple_walk.html')

if __name__ == '__main__':
    plot_random_walk()
