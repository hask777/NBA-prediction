import requests
from bs4 import BeautifulSoup
import pandas as pd

years = list(range(1991, 2022))
# print(years)

url_start = "https://www.basketball-reference.com/awards/awards_{}.html"

# for year in years:
#     url = url_start.format(year)
#     data = requests.get(url)

#     with open("mvp/{}.html".format(year), "w+", encoding="utf-8") as f:
#         f.write(data.text)

    # print("File create")

with open("mvp/1991.html") as f:
    page = f.read()

# print(page)

soup = BeautifulSoup(page, "html.parser")
soup.find('tr', class_="over_header").decompose()
# table = soup.find('table', id="mvp")
mvp_table = soup.find_all(id='mvp')
mvp_1991 = pd.read_html(str(mvp_table))[0]

for year in years:
    with open("mvp/{}.html".format(year)) as f:
        page = f.read()
    soup = BeautifulSoup(page, "html.parser")
    soup.find('tr', class_="over_header").decompose()
    mvp_table = soup.find_all(id='mvp')

    print(mvp_table)
