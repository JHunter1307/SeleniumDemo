from selenium import webdriver

driver=webdriver.Chrome("C:/Drivers/chromedriver_win32/chromedriver.exe")

# get is command which is used to open application on the browser
# driver. for everything we are creating an instance to chrome (means the browser itself) and we are storing that
# reference in drivers so moving further if you would like to preform operations on browser we can use this driver
# instance itself
driver.get("http://www.bing.com")
