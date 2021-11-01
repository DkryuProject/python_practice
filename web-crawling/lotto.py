from bs4 import BeautifulSoup
from pprint import pprint
from tqdm import tqdm
from pymongo import MongoClient
import requests

st_num = 1 # 시작회차
ed_num = 987 # 종료회차

#MongoDB 세팅
client = MongoClient('localhost', 27017)

db = client["test"]
collections = db["lotto"]

for i in tqdm(range(st_num, ed_num)):
    html = requests.get("https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="+str(i))
    soup = BeautifulSoup(html.text, "html.parser")

    #회차
    no = soup.select_one("div.win_result > h4 > strong")
    #추첨일
    date = soup.select_one("div.ein_result > p")
    #당첨번호
    lotto_numbers = soup.select("div.num.win > p > span")
    #보너스 번호
    lotto_bonus = soup.select_one("div.num.bonus > p > span")

    lotto_dict = {"no": no.get_text()}

    for index, no in enumerate(lotto_numbers):
        lotto_dict.update({"num"+str(index+1): no.get_text()}) 

    lotto_dict["bonus"] = lotto_bonus.get_text()

    #pprint(lotto_dict)
    #DB 저장
    collections.insert_one(lotto_dict)

