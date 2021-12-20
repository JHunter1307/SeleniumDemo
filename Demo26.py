import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https//login.salesforce.com/")
driver.maximize_window()
#the next 3 lines will eneter name, password and click on login button
driver.find_element_by_id("username").send_keys("chaitusarma99@gmail.com")
driver.find_element_by_id("password").send_keys("NewPass@123")
driver.find_element_by_id("Login").click()
time.sleep(35)
#there is a reason for giving 35sec here which we will study

#the next 2 lines will click on create and then it will creat user
driver.find_element_by_xpath("//a[@tittle='Create Menu']").click()
driver.find_element_by_xpath("//span[@class='slds-align-middle']").click()
# I can use findElements to capture all the information with a forloop and print all the text and click on desired
# object as discussed in demo 25 example
# you can also use demo 24 example option which is identify the count 1st and write customized xpath which is
# (xpath)[count]
time.sleep(8)

first=driver.window_handles[0]
second=driver.window_handles[1]
# above 2 commands will capture both window information
# now we need to ask our webdriver to switch to 2nd window

driver.switch_to.window(second)
# switch to frame in the new window
frame2=driver.find_element(By.ID,"searchFrame")
driver.switch_to.frame(frame2)

# below command will enter a value in the new window
driver.find_element(By.ID,"1ksrch").send_keys("surendra")
driver.find_element(By.NAME,"go").click()

# driver.switch_to.default_content()

driver.switch_to.window(first)

time.sleep(8)
driver.quit()