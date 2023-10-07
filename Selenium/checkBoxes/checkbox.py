from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
url = 'file:///Users/Claudio.Correia/Documents/git_repo/python_udemy/my_code/my_code_venv/Selenium/checkBoxes/checkbox.html'
driver .get(url)

# example 1
# to_select_value = '61-80'
# locator_by_value = f'input[name="age-group-checkbox"][value="{to_select_value}"]'

# my_choice = driver.find_element(By.CSS_SELECTOR, locator_by_value)
# my_choice.click()
# assert my_choice.is_selected(), f"After clicking value {to_select_value} it is not Select"

# example 2
# verify number of checkboxes and they are selectable
except_number_of_options = 4
all_checkboxes = driver.find_elements(By.NAME, 'age-group-checkbox')
assert len(all_checkboxes) == except_number_of_options, "Number of checkboxes is not the expected"

for checkbox in all_checkboxes:
    checkbox.click()
    value = checkbox.get_attribute('value')
    if checkbox.is_selected():
        print(f"Checkobox with value '{value}' is selectable")
    else:
         raise Exception(f"Value '{value}' is not selectable")