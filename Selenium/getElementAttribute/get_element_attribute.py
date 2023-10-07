from selenium import webdriver
import pdb
 
driver = webdriver.Firefox()
driver.get('http://demostore.supersqa.com/')

# exmaple 1 (placeholder)
# search_field = driver.find_element('id', 'woocommerce-product-search-field-0')
# placeHolder = search_field.get_attribute('placeholder')
# if placeHolder != "Search products…":
#     raise Exception("Please holder for serach field is not as expected. Actual: {}".format(placeHolder))
# else:
#     print('Pass')
# # pdb.set_trace()

# exmaple 2 (see which tab is selected)
my_acct = driver.find_element('css selector', 'li.page-item-9')
my_acct.click()

# select all nav elements and loop through them to get the item class and see which one is selected
nav_items = driver.find_elements('css selector', 'ul.nav-menu li')
for item in nav_items:
    item_class = item.get_attribute('class')
    # if "current_page_item" in item_class: # there an issue with this line
        # print('The selected tab is: {}'.format(item_class))
        # print(item_class)
        # print('print something')
        # driver.quit()
