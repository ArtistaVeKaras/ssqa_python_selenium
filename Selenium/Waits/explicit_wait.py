from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get('file:///Users/Claudio.Correia/Documents/git_repo/python_udemy/my_code/my_code_venv/Waits/page_with_slow.html')

img = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'the_slow_image')))
print('Image found')