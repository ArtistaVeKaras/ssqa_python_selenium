from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Firefox()
driver.get('http://demostore.supersqa.com/')

# find elements by Id
cart = driver.find_element(By.ID, 'site-header-cart')
cart.click()


driver.get('http://demostore.supersqa.com/my-account')
pdb.set_trace()
time.sleep(3)
driver.quit()