from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.get('http://demostore.supersqa.com/my-account/')

username = driver.find_element('id', 'username')
password = driver.find_element('id', 'password')
reg_email = driver.find_element('id', 'reg_email')
reg_email_pass = driver.find_element('id', 'reg_password')
registerBtn = driver.find_element('name', 'register')

# search_fields = driver.find_element('id', 'woocommerce-product-search-field-0')
# search_fields.send_keys('hoodie')
# search_fields.send_keys(Keys.ENTER)

username.send_keys('testusername')
password.send_keys('password1')
reg_email.send_keys('test@supersqa1.com')
reg_email_pass.send_keys('passswordagain')
registerBtn.click()
time.sleep(3)
print ('Registration successful')