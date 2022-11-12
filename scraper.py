import requests
from bs4 import BeautifulSoup
import pandas as pd

years = list(range(1991, 2022))

url_start = "https://www.basketball-reference.com/awards/awards_{}.html"

soup = BeautifulSoup(page, "html.parser")
soup.find('tr', class_="over_header").decompose()
# table = soup.find('table', id="mvp")
mvp_table = soup.find_all(id='mvp')
mvp_1991 = pd.read_html(str(mvp_table))[0]

dfs = []
for year in years:
    with open("mvp/{}.html".format(year)) as f:
        page = f.read()
    soup = BeautifulSoup(page, "html.parser")
    soup.find('tr', class_="over_header").decompose()
    mvp_table = soup.find_all(id='mvp')
    mvp = pd.read_html(str(mvp_table))[0]
    mvp["year"] = year
    dfs.append(mvp)

mvps = pd.concat(dfs)
mvps.to_csv("mvps.csv")
# print(mvps)
