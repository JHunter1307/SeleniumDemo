import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://jqueryui.com/draggable/")
time.sleep(5)
fr=driver.find_element(By.CLASS_NAME,"demo-frame")
# How to switch frames is down below
driver.switch_to.frame(fr)
# driver.switch_to.frame(0)
obj=driver.find_element(By.ID,"draggable")

# ActionChains.drag_and_drop_by_offset(obj,50,50).perform()   NEED TO HAVE SPECIFIED DRIVER
# untill we import the package we cant see all the supported methods
# so lets import the proper package and then see the various methods in that
# perform(): which is used to perform that operation on the browser
ActionChains(driver).drag_and_drop_by_offset(obj,50,50).perform()

time.sleep(8)
driver.quit()