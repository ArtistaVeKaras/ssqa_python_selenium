from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Firefox()
driver.get('http://demostore.supersqa.com/')

# find elements by CssSelector
cart = driver.find_element(By.CSS_SELECTOR, '#site-header-cart')
cart.click()

# driver.quit()