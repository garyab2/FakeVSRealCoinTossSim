import pandas as pd

def get_nba_wins(csv_filename):
    names = [
        'Celtics', 'Hawks',  'Nets', 'Hornets', 'Bulls', 'Cavaliers', 'Mavericks', 'Nuggets',
        'Pistons','Warriors','Rockets','Pacers','Clippers','Lakers','Grizzlies','Heat',
        'Bucks','Timberwolves','Pelicans','Knicks','Thunder','Magic','76ers','Suns',
        'Trail','Kings','Spurs','Raptors','Jazz','Wizards'
    ]

    df = pd.read_csv(csv_filename)
    df['Year'] = df['Year'].apply(lambda y: int(y[:4]) +1)
    df = df[(df['Year'] < 2017) & (df['Year'] > 1980)]

    df = df.reset_index(drop=True)
    df.reindex(list(range(len(df))))

    j = 0
    wins = {n : [] for n in names}
    for i, n in enumerate(names):
        while j < len(df) and df['Team'][j] != names[(i + 1) % len(names)]:
            wins[n].append(int(df['Record'][j].split('-')[0]))
            j += 1

    return wins

if __name__ == '__main__':
    print(get_nba_wins("nba_data.csv"))