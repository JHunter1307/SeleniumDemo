...
"we have already installed selenium package to the computer" \
"Webdriver is a component of selieniumm which we already know this" \
"Within the editor I want to write my webdriver proram for which i need to use those commands" \
"in order to use those commands we need to specify to our editor that use this webdriver from the selenium" \
"package whatever we have installed for that reason we are using from"
"with the line 13 we are specifying that in this class we can create a program for webdriver" \
"as we have successfully imported it" \
"for chrome browser chromedriver.exe" \
"for firefox browser we need geckodriver.exe"
...

# from selenium import webdriver

from selenium import webdriver
browser=webdriver.Firefox(executable_path="C:/Drivers/geckodriver-v0.30.0-win64/geckodriver.exe")
browser.get("http://seleniumhq.org/")