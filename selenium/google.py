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
elem.send_keys("JMC")
elem.send_keys(Keys.RETURN)
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1
for image in images :
    image.click()
    time.sleep(2)
    imgUrl = driver.find_element(By.CSS_SELECTOR, "img.n3VNCb.KAlRDb").get_attribute("src")
    print(imgUrl)

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent','Chrome/103.0.5060.114')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(imgUrl, f"./img/{str(count)}.jpg")
    count = count + 1
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close() 