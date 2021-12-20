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

p1=driver.find_element(By.ID,"datepicker").send_keys("12/31/2021")

time.sleep(5)
driver.quit()