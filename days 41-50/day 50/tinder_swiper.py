from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

URL = 'https://tinder.com/app/recs'

chrome_driver_path = 'N:/Development/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

# TODO 1: Enter in auth

enter_button = driver.find_element(By.XPATH, '//*[@id="s-906875199"]/div/div[1]/div/main/div[1]/'
                                             'div/div/div/div/header/div/div[2]/div[2]/a')
enter_button.click()

# EDITOR NOTE: It is a total fail cause I can't sign in by myself with silenium so I can't go further
# Google doesn't work with silenium, by SMS it isn't automatic, Facebook can't use in Russian Federation

try:
    enter_by_google_button = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//*[@id="s1659711021"]/div/div/div[1]/div/div/div[3]/span/button')))
    enter_by_google_button.click()
    print("Enter by Google is ready!")

except TimeoutException:
    print("Ohhh it is so painful!")

try:
    enter_by_google_button = WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, '.My(10px) button')))
    enter_by_google_button.click()
    enter_by_google_button.click()
    print("Enter by Google is ready!")

except TimeoutException:
    print("Ohhh it is so painful!")
