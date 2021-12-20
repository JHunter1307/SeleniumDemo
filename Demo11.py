import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("https://www.bing.com/account/general?ru=")

p1=driver.find_elements_by_tag_name("option")


print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)
    # print(p1[element].text)




time.sleep(5)
driver.quit()