import requests
from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
import time

# driver = webdriver.Chrome()

years = list(range(1991, 2022))

player_stats_url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"

# for year in years:
#     url = player_stats_url.format(year)
#     driver.get(url)
#     driver.execute_script("window.scrollTo(1,10000)")
#     time.sleep(2)
#     html = driver.page_source

#     with open("player/{}.html".format(year), "w+", encoding="utf-8") as f:
#         f.write(html)
# driver.close()

dfs = []

for year in years:
    with open("player/{}.html".format(year)) as f:
        page = f.read()
        
    soup = BeautifulSoup(page, 'html.parser')
    soup.find('tr', class_="thead").decompose()
    player_table = soup.find_all(id="per_game_stats")[0]
    player_df = pd.read_html(str(player_table))[0]
    player_df["Year"] = year  
    dfs.append(player_df)

print(dfs)
   