import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("http://www.bing.com")

# p1=driver.find_elements_by_tag_name("a")
p1=driver.find_elements(By.TAG_NAME,"a")
# we are using FindElements and the output will be a collection of multiple objects
# we can use a for loop to print all the values

# this will rotate the for loop on all the values present in p1
# initial it will start from 0 index from element onwards
# len(list): total number of values in the list
# isSelected
# is displayed also : which will check whether the object is displayed in the borwser or not

print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)
    # print(p1[element].text)




time.sleep(5)
driver.quit()