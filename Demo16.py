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

# I observe that dates are starting with tagname as a
# so we can use linkText command to perform click operations
# usually if anything is starting with tagname a if you want to perform click operation on that
# we can use linkText

driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
driver.find_element(By.LINK_TEXT,"29").click()

time.sleep(5)
driver.quit()