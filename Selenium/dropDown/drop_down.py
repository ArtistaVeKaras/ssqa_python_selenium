from selenium import webdriver
from selenium.webdriver.support.select import Select
import pdb

driver = webdriver.Firefox()

driver.get('http://demostore.supersqa.com/')

my_dropDown = driver.find_element('name', 'orderby')
drop_down_obj = Select(my_dropDown)
drop_down_obj.select_by_index(2)

# for option in drop_down_obj.options: print(option.text)
# drop_down_obj = Select(my_dropDown)
# dir(drop_down_obj)
# drop_down_obj.all_selected_options[0].text
# drop_down_obj.options
# len(drop_down_obj.options)
pdb.set_trace()
# driver.quit()
