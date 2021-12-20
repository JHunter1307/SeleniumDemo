import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("http://www.bing.com")
driver.get("https://www.bing.com/account/general?ru=")

p1=driver.find_element_by_id("enAS").is_selected()
print(p1)
#is selected() true or false : if is checked moe then it will return else it will return false

if p1:
    print("already checked")
else:
    driver.find_element_by_id("enAS").click()
    print("successfully checked it")

time.sleep(5)
driver.quit()