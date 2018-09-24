import urllib.request
from bs4 import BeautifulSoup

base = 'http://www.landofbasketball.com/'
base_list_url = base + 'nba_teams_year_by_year.htm'

teams_page = urllib.request.urlopen(base_list_url)
teams = BeautifulSoup(teams_page.read(), 'html.parser')

lists = teams.find_all('div', class_='rd-100-50 clearfix')

team_base = []

for l in lists:
    for link in l.find_all('a'):
        team_base.append(link.get('href'))

acceptable = [' W ', ' L ']

def parse_season(season_link):
    page_response = urllib.request.urlopen(base + season_link)
    page_content = BeautifulSoup(page_response.read(), "html.parser")
    rows = page_content.findAll("td", {"class": "a-center"})
    record = []
    for row in rows:
        text = row.text
        if text in acceptable:
            record.append(text == acceptable[0])
    return record

team_results = {}
for team in team_base:
    team_url = base + team
    page = urllib.request.urlopen(team_url)
    data = BeautifulSoup(page.read(), 'html.parser')
    season_list = []
    season_map = {}
    for link in data.find_all('a'):
        url = link.get('href')
        if url is not None and 'results_by_team' in url and '2019' not in url and 'playoff' not in url:
            season_list.append(url[2:])
    for season_url in season_list:
        season_map[season_url] = parse_season(season_url)
    team_results[team] = season_map

for team, seasons in team_results.items():
    for season, record in seasons.items():
        print(team[14:].split('.')[0] + ',' + season[17:21] + ',"' + str(record) + '"')
