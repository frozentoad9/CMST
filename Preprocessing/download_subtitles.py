#getting list of all directories
import os
path = "/home/frozentoad9/CMASR"
dir_list = os.listdir(path)
dir_list.sort()


import urllib.request


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/home/frozentoad9/Downloads/chromedriver"

driver = webdriver.Chrome(PATH)
driver.get('https://dotsub.com/view/')
driver.find_element_by_class_name("dropdown-toggle").click()
driver.find_element_by_id("username").send_keys("frozentoad9")
driver.find_element_by_id("password").send_keys("ad760940") 
driver.find_element_by_id("signIn").click()
time.sleep(5)  
main = driver.find_element_by_id("subtitleFileDownload")
links = main.find_elements_by_tag_name('a')
languages = []
 for link in links:
    direc = "/home/frozentoad9/Documents/"+link.text+".srt"
    urllib.request.urlretrieve(link.get_attribute('href'), direc) 


# =============================================================================
# driver.get('https://dotsub.com/view/2ec3ed00-e307-4e93-a300-4ced8a258a58')
# =============================================================================
