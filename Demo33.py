import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.w3schools.com/TAGS/default.ASP")
driver.maximize_window()
time.sleep(15)

a=driver.switch_to.alert

# a.text #which will get the text
# a.send_keys("data") #will enter data into that field
# a.accept() #click on ok button
# a.dismiss() #cancel on the alert

print(a.text)

a.accept()

print("succesfully handled alerts")


time.sleep(8)
driver.quit()