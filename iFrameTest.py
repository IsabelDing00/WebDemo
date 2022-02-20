from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# create
driver = webdriver.Chrome('./driver/chromedriver')
# ----- alibaba cloud TEST -----
driver.get('https://account.alibabacloud.com/register/intl_register.htm?spm=a3c0i.239195.6791778070.43.7af912bd2Nbqb8&lang=en&oauth_callback=https%3A%2F%2Fus.alibabacloud.com%2F')

# find iframe
frame = driver.find_element(By.ID, 'alibaba-register-box')
# switch to iFrame
driver.switch_to.frame(frame)

# input email
driver.find_element(By.ID, 'email').send_keys('chongfanding@gmail.com')


time.sleep(3)
driver.quit()