
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# create
driver = webdriver.Chrome('./driver/chromedriver')
# ----- Alert Page TEST -----
driver.get(r'file:///Users/isabelding/PycharmProjects/WebDemo/alert.html')

driver.find_element(By.TAG_NAME, 'button').click()
# switch alert
alert = driver.switch_to.alert
print(alert.text)

alert.accept()
