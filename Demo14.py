import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")

fr=driver.find_element(By.CLASS_NAME,"demo-frame")
# How to switch frames is down below
driver.switch_to.frame(fr)
# driver.switch_to.frame(0)

p1=driver.find_element(By.ID,"datepicker").click()

# This allows the focus to be on the main html part of the page again
driver.switch_to.default_content()

time.sleep(5)
driver.quit()