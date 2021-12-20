import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Firefox(executable_path="drivers/geckodriver.exe")

driver.get('http://seleniumhq.org/')
driver.maximize_window()

driver.implicitly_wait(30)

time.sleep(5)
driver.quit()