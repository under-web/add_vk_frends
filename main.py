import time
from selenium import webdriver


try:
    # fox_options = webdriver.FirefoxOptions()
    # set_headless = True
    # browser = webdriver.Firefox(firefox_options=fox_options)
    browser = webdriver.Firefox()
    browser.get('https://vk.com/')
    time.sleep(1)
    phone_box = browser.find_element_by_id('index_email').send_keys('your_phone')
    paswd_box = browser.find_element_by_id('index_pass').send_keys('your_pass')
    time.sleep(1)
    sign_bottom = browser.find_element_by_id('index_login_button').click()
    time.sleep(10)
    browser.close()
    browser.quit()
except Exception as e:
    print(e)
