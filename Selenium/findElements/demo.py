from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

# open firefox driver
se = Service(executable_path="/usr/local/bin/firefox")
driver = webdriver.Firefox(service=se)

# go to url
driver.get('http://demostore.superqa.com/')
time.sleep(3)

# click on 'Myaccount' tab
my_acct_tab = driver.find_element(By.CLASS_NAME, "MyAccount")
vegetable = driver.find_element(By.CLASS_NAME, "tomatoes")
driver.quit()
  
my_acct_tab.click()
time.sleep(3)

# scrole the page up
driver.execute_script('window.scrollTo(0, 300)')


# find username field and input username
u_name_field = driver.find_element('username') 
u_name_field.send_keys('fakename')


# find password field and input password
p_field =driver.find_element(By.ID, 'password') 
p_field.send_keys('aaaaaaaa')

# click login button
login_btn = driver.find_element(By.ID, 'login')
login_btn.click()

# get displayed error mgs
error_list_elm = driver.find_element(By.CLASS_NAME, 'ul.woocommerce-error li')
# first_error_elm = error_list_elm[0]
# displayed_error_text = first_error_elm.text

# verify the displayed error is as expecetd
expected_error = "ERROR: Invalid username. Lost your password?"
# assert expected_error == displayed_error_text, "Disaplyed error is not as expected"
print("success")