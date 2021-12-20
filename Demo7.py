import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("http://www.bing.com")
driver.get("https://www.bing.com/account/general?ru=")

driver.find_element_by_id("adlt_set_strict").click()
p1=driver.find_element_by_id("adlt_set_strict").is_selected()
print(p1)

#is_selected commnad to know the statis of the checkbox
#is true, if it is not selected then it will return false.

time.sleep(5)
driver.quit()