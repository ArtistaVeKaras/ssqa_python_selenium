import unittest
from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory

class LoginPage(PageFactory):

    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver

    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "edtUserName": ('ID', 'user_login'),
        "edtPassword": ('NAME', 'pwd'),
        "btnSignIn": ('XPATH', '//input[@value="Log In"]')
    }

    def login(self):
        # set_text(), click_button() methods are extended methods in PageFactory self.edtUserName.set_text("<USERNAME>")               
        # # edtUserName become class variable using PageFactory
        self.edtUserName.set_text("<USERNAME>")
        self.edtPassword.set_text("<PASSWORD>")
        self.btnSignIn.click_button()


class LoginTest(unittest.TestCase):

    def test_Login(self):
        driver = webdriver.Firefox()
        driver.get("https://s1.demo.opensourcecms.com/wordpress/wp-login.php")

        pglogin = LoginPage(driver)
        pglogin.login()

if __name__ == "__main__":
     unittest.main()