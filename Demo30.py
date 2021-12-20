import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.w3schools.com/TAGS/default.ASP")
driver.maximize_window()
driver.implicitly_wait(30)

table=driver.find_element(By.XPATH,"//*[@id='htmltags']/table")

tablerows=table.find_elements(By.TAG_NAME,"tr")

# WebDriverWait(driver,10).until(EX.alert_is_present())

# in order to know how many rows there are we can use len method

print(len(tablerows))

beforeNumber="//tr["
afterNumberTag="]/td[1]"
afterNumberDesc="]/td[2]"

# beforeNumber+2,3,4 (needs to come from for loop) + afternumber

for _ in range(2,len(tablerows)):
    xp1=beforeNumber+str(_)+afterNumberTag
    # xp1=//tr[2]/td[1]
    tagName=driver.find_element(By.XPATH,xp1).text
    # print(tagName)
    xp2=beforeNumber+str(_)+afterNumberDesc
    # xp1 = // tr[2] / td[2]
    desc=driver.find_element(By.XPATH,xp2).text
    # print(desc)
    tagdisc=tagName+": "+desc
    print(tagdisc)



time.sleep(8)
driver.quit()