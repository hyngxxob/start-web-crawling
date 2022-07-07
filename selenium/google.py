from selenium import webdriver
from attr import Attribute
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
from urllib.request import Request, urlopen

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.send_keys("대한민국")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try :
            driver.find_element(By.CSS_SELECTOR, "input.mye4qd").click()
        except :
            break
    last_height = new_height

images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1
for image in images :
    try :
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img").get_attribute("src")
        print(imgUrl)

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent','Chrome/103.0.5060.114')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, f"./img/{str(count)}.jpg")
        count = count + 1
    except :
        pass

driver.close()