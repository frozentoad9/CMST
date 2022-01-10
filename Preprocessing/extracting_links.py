from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/home/frozentoad9/Downloads/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://vanimedia.org/wiki/Table:_Clips_to_subtitle")

#extracting Dotsub Links

table = driver.find_element_by_tag_name("table")
main = table.find_elements_by_link_text('Dotsub Video')
dotsub_links = []
for link in main:
    dotsub_links.append(link.get_attribute("href"))

print('Total Links : {}'.format(len(dotsub_links)))
print(dotsub_links)


#extracting youtube links

table = driver.find_element_by_tag_name("table")
main = table.find_elements_by_link_text('YouTube Video')
youtube_links = []
for link in main:
    youtube_links.append(link.get_attribute("href"))

print('Total Links : {}'.format(len(youtube_links)))
print(youtube_links)
























