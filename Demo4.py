import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("http://www.bing.com")

driver.find_element_by_id("sb_form_q").send_keys("James Hunter")
driver.find_element_by_class_name()
driver.find_element_by_css_selector()
driver.find_element_by_link_text()
driver.find_element_by_partial_link_text()
driver.find_element_by_tag_name()
driver.find_element_by_xpath("//label[@for='sb_form_go']").click()
# to enter a value: sendkeys, click operation: click

time.sleep(5)  #which will wait for 5 seconds
driver.quit()  #which will termante the browser and release