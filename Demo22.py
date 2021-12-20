import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("http://www.bing.com")
driver.maximize_window()

driver.find_element(By.ID,"sb_form_q").send_keys("test")
driver.find_element(By.ID,"sb_form_q").send_keys(Keys.ENTER)
time.sleep(2)

# Having a bit of fun with ActionChains
# a = ActionChains(driver)
# m = driver.find_element(By.ID,"sb_form_q")
# a.move_to_element(m).perform()
driver.find_element(By.ID,"sb_form_q").click()
time.sleep(5)
p1=driver.find_elements(By.XPATH,"//*[@id='sa_ul']")

# /html/body/header/form/div/input[1]
# //*[@id="sb_form_q"]
# "//*[@id="sb_form_q"]")

# Below line will print total number of values in the list (not working??)
print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)
    # print(p1[element].text)

# let me try to capture screenshot
# in order to capture screen shot we need to mention in which location it needs to capture
# we need to specify file location and file name also as an input to this function

# driver.get_screenshot_as_png("C:/python stuff/screenshots/demo22.png")
driver.get_screenshot_as_file("C:/python stuff/screenshots/demo22.png")

time.sleep(1)
driver.quit()