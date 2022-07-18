# Date : 2022.07.18
# Data Crawling prototype test

from cgitb import html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import re


TARGET_URL = "https://smartstore.naver.com/floomingplants"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

# 주간 베스트
ul_class = "_3ba8S41U2S C6YnC57T6Q"
# 주간 베스트 리스트
li_class = "_3zhPg5BV4U _2hiE--seNK _3FxXcV5yvs"
# 주간 베스트 제목 텍스트 div
div_class = "_16P0LCXnI1"
# 주간 베스트 상품 제목
storng_class = "_1Zvv5Kme1t"

ul_pattern = re.compile(r"^_.+ .+")
li_pattern = re.compile(r"^_.+ _.+ _.+")
div_pattern = re.compile(r"^_.+")

option = Options()
option.add_argument('user-agent='+USER_AGENT)
option.add_argument('headless')
driver = webdriver.Chrome("./diver/chromedriver.exe", options=option)
driver.get(TARGET_URL)
sleep(1.5)
print("request URL successed!")


source = driver.page_source
print("get html success")
html = BeautifulSoup(source, "html.parser")

#crawler part

#title part
ul_list = html.find("ul", {'class':f'{ul_class}'})
product_list = ul_list.findAll("li")
title_list = [] 
for product in product_list:
    title = product.findAll("strong")
    title_list.append(title)
print(product_list)
print(title_list[0])
    




