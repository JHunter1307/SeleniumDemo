import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("http://www.bing.com")
driver.get("https://www.bing.com/account/general?ru=")

driver.find_element_by_id("rpp").send_keys("50")

time.sleep(5)  #which will wait for 5 seconds
driver.quit()  #which will termante the browser and release