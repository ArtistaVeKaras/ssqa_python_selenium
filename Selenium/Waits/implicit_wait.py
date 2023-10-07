from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(15)

driver.get('file:///Users/Claudio.Correia/Documents/git_repo/python_udemy/my_code/my_code_venv/Waits/page_with_slow.html')

img = driver.find_element(By.ID, 'the_slow_image')
img.click()
print('Foudn image')
driver.quit()