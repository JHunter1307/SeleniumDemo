import unittest
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import HtmlTestRunner


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # will write logic to launch the borwser and open the application even I will maximize browser also
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://login.salesforce.com/")
        cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls):
        # I will logic to wait for sometime and terminate the browser
        time.sleep(5)
        cls.driver.quit()

    def test_a_login(self):
        # in this test I want to create logic which will login into the app
        # mean it will enter uname and password, click on login button
        self.driver.find_element_by_id("username").send_keys("chaitusarma99@gmail.com")
        self.driver.find_element_by_id("password").send_keys("NewPass@123")
        self.driver.find_element_by_id("Login").click()
        time.sleep(5)

    def test_b_createAccount(self):
        # I want to write logic to perform click operation and on create user and enter firstname
        self.driver.find_element_by_xpath("//a[@tittle='Create Menu']").click()
        self.driver.find_element_by_xpath("//span[@class='slds-align-middle']").click()
        time.sleep(8)
        frame1 = self.driver.find_element_by_xpath("//iframe[@title='New User ~ Salesforce - Developer Edition']")
        self.driver.switch_to.frame(frame1)
        self.driver.find_element_by_id("name_firstName").send_keys("James Hunter")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/jhunter/PycharmProjects/SeleniumExamples/reports'),verbosity=2)
