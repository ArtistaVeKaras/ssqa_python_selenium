from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InvalidUserLoginError:
    

    invalid_email = "abc@superqa.com" 
    url = "http://demostore.supersqa.com/my-account/"
    expected_msg = "Error: Please provide a valid email address."

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        
    def go_to_my_account(self):
        self.driver.get(self.url)
    
    def input_email(self):
        field = self.driver.find_element(By.ID, 'username')
        field.send_keys(self.invalid_email)
    
    def input_password(self):
        field = self.driver.find_element(By.ID, 'password')
        field.send_keys("sadfasdfad")
    
    def click_button(self):
        self.driver.find_element(By.NAME, 'login').click()
    
    def verify_erro_message(self):
        err_elm = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li/text()')
        displayed_err = err_elm.text
        assert displayed_err == self.expected_msg, "The displayed error is not expectted"

    def main(self):
        self.go_to_my_account()
        self.input_email()
        self.input_password()
        self.verify_erro_message()
        self.click_button()
        self.verify_erro_message()
        # self.driver.quit()

        
if __name__ == '__main__':
    
    obj = InvalidUserLoginError()