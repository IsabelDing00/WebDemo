
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# create
driver = webdriver.Chrome('./driver/chromedriver')
# -----12306 Ticket TEST -----
driver.get('https://www.12306.com')

time.sleep(5)
driver.execute_script('document.querySelector(\'[id="train-date"]\').value="2021-05-02"')
