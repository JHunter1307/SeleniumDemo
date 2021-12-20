import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.emirates.com/in/english/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='onetrust-accept-btn-handler']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[@data-link='MANAGE']").click()

obj=driver.find_element(By.XPATH,"//a[@data-link='MANAGE:Before you fly']")

ActionChains(driver).move_to_element(obj).perform()
# Move to element is a command which will move cursor to a specified object

# //*[@id="submenu-1-1"]/div/div[2]/div[1]/ul/li[1]/a/span/i

# data-link='MANAGE:Before you fly'

time.sleep(5)
driver.quit()