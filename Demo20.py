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
obj=driver.find_element(By.ID,"draggable")


# below command will capture the height and width of the object
s=obj.size
# below command will capture x and y corridnates of the object
l=obj.location

# obj.get_attribute("property")
print(obj.get_attribute("class"))


print(s)
print(l)

time.sleep(8)
driver.quit()