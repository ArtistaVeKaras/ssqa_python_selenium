from selenium import webdriver

driver = webdriver.Firefox()

url = 'file:///Users/Claudio.Correia/Documents/git_repo/python_udemy/provided_code/python_selenium_course_material/SELENIUM_SECTION/Multiple_Windows_and_Tabs/windows-and_tabs_example.html'


driver.get(url)

btn = driver.find_element('xpath', '/html/body/div[2]/a[1]')
btn.click()

print("Before switiching focus:" + driver.title)
current_window_hanle = driver.current_window_handle
all_window_handle = driver.window_handles
original_window_handle = all_window_handle[0]
new_window = all_window_handle[1]
# driver._switch_to.window(new_window)
# print("After switiching focus:" + driver.title)
# print("Closing Tabs")
# driver.close()
# print("Switiching back to the original")
# driver.switch_to.window(original_window_handle)

import pdb 
pdb.set_trace()
# driver.title()
# driver.current_window_handle
# driver.window_handles