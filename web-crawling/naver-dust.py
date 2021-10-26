from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B0%80%EC%82%B0%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hUOx%2Fwp0JXVssDrECeKssssstss-011077")
#pprint(html.text)

bs = BeautifulSoup(html.text, 'html.parser')
title = bs.select_one("h2.title")
temperature = bs.select_one("div.temperature_text > strong")
weather = bs.select_one("span.weather")

pprint("title: "+title.get_text())
pprint("temperature: "+temperature.get_text())
pprint("weather: "+weather.get_text())



