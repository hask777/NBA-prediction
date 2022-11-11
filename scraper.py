import requests

years = list(range(1991, 2022))
# print(years)

url_start = "https://www.basketball-reference.com/awards/awards_{}.html"

for year in years:
    url = url_start.format(year)
    data = requests.get(url)

    with open("mvp/{}.html".format(year), "w+", encoding="utf-8") as f:
        f.write(data.text)

    print("File create")
