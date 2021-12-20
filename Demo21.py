import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://jqueryui.com/tooltip/")
time.sleep(3)

fr=driver.find_element(By.CLASS_NAME,"demo-frame")
# How to switch frames is down below

driver.switch_to.frame(fr)

obj=driver.find_element(By.ID,"age")

p1=obj.get_attribute("title")
print("tooltip message is : " + p1)



time.sleep(8)
driver.quit()