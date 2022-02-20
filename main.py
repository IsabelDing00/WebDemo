
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# create
driver = webdriver.Chrome('./driver/chromedriver')
# -----Baidu TEST -----
driver.get('https://www.baidu.com')
# find element by id
# driver.find_element(By.ID, 'kw').send_keys('helloworld')

# find element by name
# driver.find_element(By.NAME, 'wd').send_keys('helloworld')

# find element by link text   or partial link text
# driver.find_element(By.LINK_TEXT, '地图').click()

# find element by CSS
driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('helloworld')

# -----Ctrip TEST -----
# driver.get('https://www.ctrip.com')
# # Xpath and print all elements
# elements = driver.find_elements(By.XPATH, '//*[@dcity="2"]')
# for e in elements:
#     print(e.text)



time.sleep(3)
driver.quit()
