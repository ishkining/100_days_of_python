from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time


chrome_driver_path = 'N:/Development/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

python_org_dict = {}

driver.get('https://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, 'cookie')
money = 0
store = driver.find_elements(By.CSS_SELECTOR, '#store div')
store_items = [item.get_attribute("id") for item in store]


def click_if_it_is_available():
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
    for item in store_items[::-1]:
        my_store_item = driver.find_element(By.ID, item)
        if my_store_item.get_attribute('class') != 'grayed':
            store_item = WebDriverWait(driver, 500, ignored_exceptions=ignored_exceptions) \
                .until(expected_conditions.presence_of_element_located((By.ID, my_store_item.get_attribute('id'))))
            store_item.click()
            return False


while True:
    [cookie.click() for _ in range(15)]
    money += 1
    click_if_it_is_available()





# driver.quit()