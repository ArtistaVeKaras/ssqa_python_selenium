from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def add_1_item_to_cart():
    driver.find_element(By.CLASS_NAME, 'add_to_cart_button').click()
    wait.until(
         EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[2]/header/div[2]/div/ul/li[1]/a'), '1 item')
     )

def click_cart_in_top_menu():
    driver.find_element(By.XPATH, '/html/body/div[2]/header/div[2]/div/ul/li[1]/a').click()
     

def input_coupon__and_hit_enter(coupon_code):
    coupon_field = wait.until (EC.visibility_of_any_elements_located((By.ID, 'coupon_code')))
    coupon_field.send_keys(coupon_code)
    coupon_field.send_keys(Keys.ENTER)
    
def verify_total_is_0():
    wait.until(EC.visibility_of_any_elements_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/main/article/div/div/div[2]/div/div/a')))
    pass 

if __name__ == '__main__':
    
    
    coupon_code = 'SSQA100'
    
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    
    driver.get('http://demostore.supersqa.com/')
    
    add_1_item_to_cart()
    click_cart_in_top_menu()
    input_coupon__and_hit_enter(coupon_code)
    verify_total_is_0()