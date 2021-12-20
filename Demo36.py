import time
from selenium import webdriver
import xlrd
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("http://www.bing.com")
driver.maximize_window()


loc = "C:/python stuff/dd.xls"

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)

p1 = sheet.cell(0, 0).value
print(p1)

print(sheet.nrows)
print(sheet.ncols)

for i in range(sheet.nrows):
    p2 = sheet.cell(i, 0).value
    print(p2)
    driver.find_element(By.ID,"sb_form_q").clear()
    driver.find_element(By.ID,"sb_form_q").send_keys(p2)
    time.sleep(1)

time.sleep(5)  #which will wait for 5 seconds
driver.quit()  #which will termante the browser and release