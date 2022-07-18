# Date : 2022.07.18
# Data Crawling prototype test

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import re


TARGET_URL = "https://smartstore.naver.com/floomingplants"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

driver = webdriver.Chrome("./diver/chromedriver.exe")
option = Options()
option.add_argument("user-agent="+USER_AGENT)
driver.get(TARGET_URL)
print("request URL successed!")


