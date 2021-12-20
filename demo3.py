import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("http://www.bing.com")

# to get xpath  //tagname[@property type='property value']

driver.find_element_by_id("sb_form_q").send_keys("James Hunter")
driver.find_element_by_xpath("//label[@for='sb_form_go']").click()

# in the last session we created 1 scenario it launched another browser, we are not writing any  commands to close
# the browser, usually our system will allocate some memory : if we are not terminating the browser means we will
#     encounter and speed of our machine will reduce
#  it will close the browser and will release the memory which is allocated

time.sleep(5)  #which will wait for 5 seconds
driver.quit()  #which will termante the browser and release