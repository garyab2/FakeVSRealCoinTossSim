import ast
import numpy as np
import pandas as pd

from coin_toss_sim import simulate_coin_toss
from histogram import plot_overlaid_histograms

def get_longest_streak(sim):
    max_streak = 0
    curr_streak = 0
    for result in sim:
        curr_streak = curr_streak + int(result) if int(result) == 1 else 0
        max_streak = max(max_streak, curr_streak)
    return max_streak

def plot_longest_streak_hist():
    scores_df = pd.read_csv('scrape_data.csv')

    nba_hist = []
    coin_hist = []

    for i, row in scores_df.iterrows():
        record = ast.literal_eval(row['Record'])
        coin_sim = simulate_coin_toss(len(record))

        nba_hist.append(get_longest_streak(record))
        coin_hist.append(get_longest_streak(coin_sim))

    plot_overlaid_histograms(coin_hist, nba_hist, 'Histogram of Win Streaks', 'Streaks', 'Frequency', 'histogram_of_streaks.html')

if __name__ == '__main__':
    plot_longest_streak_hist()
