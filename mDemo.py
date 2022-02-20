from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# create
driver = webdriver.Chrome('./driver/chromedriver')
# ----- Alert Page TEST -----
driver.get("https://pro.jd.com/mall/active/3Sex5cB1TSBKKappQomcqyVno8iW/index.html?utm_medium=cpc&utm_source=google&utm_campaign=AmericaBrandC013&gclid=CjwKCAiAx8KQBhAGEiwAD3EiP8_YBUt7TVCyPJBlRrsFog2CXIoqFGRCT-ddphTmKJehhzXhCoS8xBoCTsQQAvD_BwE")
navbtn = driver.find_element(By.XPATH, '//*[@class="dt cw-icon"]')
ActionChains(driver).move_to_element(navbtn).perform()
sth = driver.find_element(By.ID, '//a[@role="menuitem" and text()="京东通信"]')
ActionChains(drive).move_to_element(sth).click().perform()


