import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https//login.salesforce.com/")
driver.maximize_window()
#the next 3 lines will eneter name, password and click on login button
driver.find_element_by_id("username").send_keys("chaitusarma99@gmail.com")
driver.find_element_by_id("password").send_keys("NewPass@123")
driver.find_element_by_id("Login").click()
time.sleep(35)


time.sleep(8)
driver.quit()