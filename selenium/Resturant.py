from selenium import webdriver
from attr import Attribute
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
from urllib.request import Request, urlopen

driver = webdriver.Chrome()
driver.get("https://www.diningcode.com/list?query=")
elem = driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div[1]/input")
elem.send_keys("상수역")
elem.send_keys(Keys.RETURN)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[3]/div/button").click()
time.sleep(2)

resturants = driver.find_elements(By.CLASS_NAME, "Info")
for rest in resturants :
    name = driver.find_element(By.CLASS_NAME, "InfoHeader")
    print(name)

# 새로 생성된 탭으로 전환
# driver.switch_to.window(driver.window_handles[-1])
# time.sleep(5)
# driver.close()
while(True) :
    pass