import requests
from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
import time

# parsing the site data
years = list(range(1991, 2022))
# team_stats_url = "https://www.basketball-reference.com/leagues/NBA_{}_standings.html"

# for year in years:
#     url = team_stats_url.format(year)
#     data = requests.get(url)
#     with open("team/{}.html".format(year), "w+", encoding="utf-8") as f:
#         f.write(data.text)

# extract table's data

dfs = []
for year in years:
    with open('team/2021.html') as f:
        page =  f.read()

    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find(id="divs_standings_E")
    soup.find('thead').decompose()
    team_table = soup.find(id="divs_standings_E")
    team = pd.read_html(str(team_table))[0]
    team["Year"] = year  
    team["Team"] = team["Eastern Conference"]
    del team["Eastern Conference"]
    dfs.append(team)

    soup = BeautifulSoup(page, 'html.parser')
    soup.find('thead').decompose()
    team_table = soup.find(id="divs_standings_W")
    team = pd.read_html(str(team_table))[0]
    team["Year"] = year  
    team["Team"] = team["Western Conference"]
    del team["Western Conference"]
    dfs.append(team)

teams = pd.concat(dfs)

# print(teams)
teams.to_csv("teams.csv")