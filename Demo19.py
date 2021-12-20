import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")
time.sleep(3)

fr=driver.find_element(By.CLASS_NAME,"demo-frame")
# How to switch frames is down below

driver.switch_to.frame(fr)

src=driver.find_element(By.XPATH,"//div[@class='ui-widget-content ui-draggable ui-draggable-handle']")
dest=driver.find_element(By.XPATH,"//div[@class='ui-widget-header ui-droppable']")

ActionChains(driver).drag_and_drop(src,dest).perform()

time.sleep(8)
driver.quit()