import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
# below command will maximize window
driver.maximize_window()
driver.get("http://www.bing.com")

# p1=driver.find_elements_by_tag_name("a")
p1=driver.find_elements(By.TAG_NAME,"a")
print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)
        p1[element].send_keys(Keys.TAB)
    # print(p1[element].text)




time.sleep(5)
driver.quit()