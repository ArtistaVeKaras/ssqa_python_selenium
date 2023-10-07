from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('file:///Users/Claudio.Correia/Documents/git_repo/python_udemy/provided_code/python_selenium_course_material/SELENIUM_SECTION/Radios/radios_example.html')

expected_deafult_value = '21-40'
locator_by_value = 'input[name="age-group-radio"][value="{value}"]'

# example 1 verify dafault is selected
default_element = driver.find_element(By.CSS_SELECTOR, locator_by_value.format(value = expected_deafult_value))
assert default_element.is_selected(), f"The default value of {expected_deafult_value} is not selected."

# example 2 verify dafault are present
expected_values = ['21-40','41-60','61-80','81+']
all_radios = driver.find_elements(By.NAME, 'age-group-radio')
assert len(all_radios) == len(expected_values), "The number of radious does not match the expected"