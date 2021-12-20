import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("http://www.bing.com")
driver.get("https://www.bing.com/account/general?ru=")

driver.find_element_by_id("enAS").click()

...
"click is a command that will toggle the status of the checkbox" \
"but my requirement is I dont want to toggle it. Based on the status of checked I need to update it" \
"if my checkbox is in checked mode: then simply print a message that is already checked"
"if it is not checked mode then check it and print a message that successfully"
...

time.sleep(5)  #which will wait for 5 seconds
driver.quit()  #which will termante the browser and release