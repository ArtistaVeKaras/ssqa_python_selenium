from selenium import webdriver

driver = webdriver.Firefox()

url = 'file:///Users/Claudio.Correia/Documents/git_repo/python_udemy/provided_code/python_selenium_course_material/SELENIUM_SECTION/Alerts/alerts_example.html'

driver.get(url)

# EXAMPLE 1
# alert_btn_1 = driver.find_element('css selector', 'div#jsAlertExample button')
# alert_btn_1.click()

# my_alert = driver.switch_to.alert

# assert my_alert.text == 'I am a JavaScript Alert', "Unexpected text on alert"
# my_alert.accept


# EXAMPLE 2
alert_btn_1 = driver.find_element('css selector', 'div#jsConfirmExample button')
alert_btn_1.click()

confirm_alert = driver.switch_to.alert
confirm_alert.accept()

resMessage = driver.find_element('id', 'userResponse1').text
assert resMessage == 'Great! You will love it!', "Unexpected text on alert"

# Dismiss() function negative scenario
# confirm_alert = driver.switch_to.alert
# confirm_alert.dismiss()

# resMessage = driver.find_element('id', 'userResponse1').text
# assert resMessage == "Too bad!!! You would've loved it!", "Unexpected text on alert"
driver.quit()
 
# import pdb; pdb.set_trace()
