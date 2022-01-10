import os
path = "/home/frozentoad9/CMASR"
dir_list = os.listdir(path)
dir_list.sort()



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

table = driver.find_element_by_tag_name("table")
main = table.find_elements_by_link_text('YouTube Video')
youtube_links = []
for link in main:
    youtube_links.append(link.get_attribute("href"))
    
print(len(youtube_links))
import urllib
PATH = "/home/frozentoad9/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

for i in range(1080):
    driver.get("https://ytmp3.cc/youtube-to-mp3/")
    driver.find_element_by_id("input").send_keys(youtube_links[i])
    driver.find_element_by_id("submit").click()
    try:
        main = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Download"))
                )
        link = main.get_attribute('href')
        print(link)
        try:
            direc = "/home/frozentoad9/Downloads/"+dir_list[i]+".mp3"
            urllib.request.urlretrieve(link, direc)
        except:
            print('not done ', i)
    except:
        continue













