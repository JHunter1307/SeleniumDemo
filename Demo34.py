import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.maximize_window()

driver.execute_script("window.location='https://www.bing.com'")
driver.execute_script("document.getElementById('sb_form_q').value='James Hunter'")
driver.execute_script("document.getElementById('sb_form_go').click();")


time.sleep(5)
driver.quit()