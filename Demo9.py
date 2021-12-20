import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("http://www.bing.com")
driver.get("https://www.bing.com/account/general?ru=")

dd=driver.find_element_by_id("rpp")

#dd means its a dropdown information itself

s=Select(dd)

# s.select_by_index(2)

# s.select_by_value("50")

# s.select_by_visible_text("Auto")

p1=s.options

#options: which will capture all the values in the dropdown and it will store in a variable when we use a print
#Statement it is printing all the web elements but my requirement I want is to print text from all the objects

for element in p1:
    p2=element.get_attribute("value")
    print(p2)

# print(p1)

...
"If we want to select 1st value in the dd then we need to give index as 0" \
"if we want to select 2nd value from the dd then we select 1"
...

time.sleep(5)  #which will wait for 5 seconds
driver.quit()  #which will termante the browser and release