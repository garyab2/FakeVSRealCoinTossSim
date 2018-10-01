import ast
import numpy as np
import pandas as pd

from coin_toss_sim import simulate_coin_toss
from line_graph import plot_overlaid_line_graphs

TEAM = 'washington_wizards' # snake case
DISPLAY_NAME = 'Washington Wizards'
YEAR = 2017

def create_random_walk(record):
    walk = [0]
    for i in record:
        diff = 1 if int(i) == 1 else -1
        walk.append(walk[-1] + diff)
    return walk

def plot_random_walk():
    scores_df = pd.read_csv('scrape_data.csv')
    team = scores_df[(scores_df['Team'] == TEAM) & (scores_df['Year'] == YEAR)].iloc[0]
    record = ast.literal_eval(team['Record'])

    x = list(range(0, len(record) + 1))

    coin_sim = simulate_coin_toss(len(record))

    plot_overlaid_line_graphs(x, create_random_walk(coin_sim), create_random_walk(record), DISPLAY_NAME, 'Random Walks', 'Step', 'Distance', 'random_walk.html')

if __name__ == '__main__':
    plot_random_walk()
