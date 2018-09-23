from bs4 import BeautifulSoup
import requests

acceptable = [' W ', ' L ']

page_link = "http://www.landofbasketball.com/results_by_team/2017_2018_bulls.htm"
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

rows = page_content.findAll("td", {"class": "a-center"})

record = []

for row in rows:
    text = row.text
    if text in acceptable:
        record.append(text == acceptable[0])

print(record)