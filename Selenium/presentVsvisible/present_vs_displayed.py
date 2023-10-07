
from selenium import webdriver


driver = webdriver.Firefox()
driver.implicitly_wait(5)


url = 'file:///Users/Claudio.Correia/Documents/git_repo/python_udemy/my_code/my_code_venv/Selenium/presentVsvisible/present_vs_displayed.py'

driver.get(url)