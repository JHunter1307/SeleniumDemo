import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.w3schools.com/TAGS/default.ASP")
driver.maximize_window()

beforeNumber="//tr["
afterNumber="]/td[2]"

# beforeNumber+2,3,4 (needs to come from for loop) + afternumber

for _ in range(2,5):
    xp1=beforeNumber+str(_)+afterNumber
    # xp1=//tr[2]/td[2]
    value=driver.find_element(By.XPATH,xp1).text
    print(value)



time.sleep(8)
driver.quit()