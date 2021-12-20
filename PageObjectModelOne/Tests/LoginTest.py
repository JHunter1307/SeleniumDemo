import unittest
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import HtmlTestRunner
from PageObjectModelOne.Pages.LoginPage import LoginPageProp
from PageObjectModelOne.Pages.HomePage import HomePageProp
from PageObjectModelOne.Pages.CreateUserPage import CreateUserProp

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
        loginProp=LoginPageProp()

        # in this test I want to create logic which will login into the app
        # mean it will enter uname and password, click on login button
        self.driver.find_element_by_id(loginProp.username_text_field_id).send_keys("chaitusarma99@gmail.com")
        self.driver.find_element_by_id(loginProp.password_text_field_id).send_keys("NewPass@123")
        self.driver.find_element_by_id(loginProp.login_button_id).click()
        time.sleep(35)

    # def test_b_createAccount(self):
    #     homePage=HomePageProp()
    #     # I want to write logic to perform click operation and on create user and enter firstname
    #     self.driver.find_element_by_xpath(homePage.create_button_xpath).click()
    #     self.driver.find_element_by_xpath(homePage.create_user_xpath).click()
    #     time.sleep(8)
    #     createUser=CreateUserProp()
    #     frame1 = self.driver.find_element_by_xpath(createUser.create_user_new_frame_xpath)
    #     self.driver.switch_to.frame(frame1)
    #     self.driver.find_element_by_id(createUser.firstname_id).send_keys("James Hunter")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/jhunter/PycharmProjects/SeleniumExamples/reports'),verbosity=2)
