import numpy as np
import pandas as pd

from coin_toss_sim import simulate_coin_toss
from histogram import plot_overlaid_histograms
from record_reader import get_nba_wins

GAMES_IN_SEASON = 82

def plot_wins_hist():
    wins_dict = get_nba_wins("nba_data.csv")

    nba_hist = []
    coin_hist = []

    for team, season_wins in wins_dict.items():
        coin_hist += [sum(simulate_coin_toss(GAMES_IN_SEASON)) for _ in range(len(season_wins))]
        nba_hist += season_wins

    plot_overlaid_histograms(coin_hist, nba_hist, 'Histogram of Wins', 'Wins', 'Frequency', 'histogram_of_wins.html')

if __name__ == '__main__':
    plot_wins_hist()
