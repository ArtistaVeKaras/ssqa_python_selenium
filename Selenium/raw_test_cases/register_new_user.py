from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
import time


driver = webdriver.Firefox()
driver.implicitly_wait(10)

url = 'http://demostore.supersqa.com/my-account/'


driver.get(url)
email_field_id = 'reg_email'
password_field_id = 'reg_password'
click_button = 'register'
logout_btn_css = 'li.woocommerce-MyAccount-navigation-link--customer-logout a'

# geneate a random email
letter = string.ascii_lowercase
rand_string = ''.join(random.choice(letter) for i in range(15))
random_email = rand_string + "@supperqa.com"

# type in the email field
email_field = driver.find_element(By.ID, email_field_id)
email_field.send_keys(random_email)

# type in the password
password_field = driver.find_element(By.ID, password_field_id)
password_field.send_keys('thijadfjaksj!?k')

time.sleep(2)
# click the register button
click_register_button = driver.find_element(By.NAME, click_button)
click_register_button.click()

# assert logout btn is displayed
logout_btn = driver.find_element(By.CSS_SELECTOR, logout_btn_css)

if logout_btn.is_displayed():
    pass
else:
    raise Exception("User not looger in after registration")
