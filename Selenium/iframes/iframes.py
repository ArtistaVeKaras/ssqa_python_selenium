from selenium import webdriver


driver = webdriver.Firefox()

url = "file:///Users/Claudio.Correia/Documents/git_repo/python_udemy/provided_code/python_selenium_course_material/SELENIUM_SECTION/iFrames/iFrames_example.html"
driver.get(url)

# # outside of an iframe
# driver.find_element('id','btnOutFrame').click()
# my_alert = driver.switch_to.alert
# my_alert_txt = my_alert.text
# assert my_alert_txt == 'Just Clicked Outside iFrame'

# inside an iframe
my_iframe = driver.find_element('id','btnInFrame')
driver.switch_to.frame(my_iframe)
driver.find_element('id','btnInFrame').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()

