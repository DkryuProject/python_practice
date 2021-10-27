from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get("https://finance.naver.com/marketindex/worldExchangeList.naver?key=exchange&page=1")
soup = BeautifulSoup(html.text, "html.parser")

tbody = soup.select_one("div.tbl_area > table > tbody")
trs = tbody.select("tr")

for tr in trs:
    name = tr.select("td")[0].text
    symbol = tr.select("td")[1].text
    exchange = tr.select("td")[2].text
    pprint(name+" "+symbol+" "+exchange)
