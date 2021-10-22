from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=날씨")
#pprint(html.text)

bs = BeautifulSoup(html.text, 'html.parser')
pprint(bs.prettify())



