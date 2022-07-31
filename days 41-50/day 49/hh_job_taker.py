from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

# EDITOR NOTE: LinkedIn doesnt work in Russian Federation, so I choose light implementation of task
URL = 'https://ufa.hh.ru/'

chrome_driver_path = 'N:/Development/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get(URL)

try:
    input_job = WebDriverWait(driver, 1).until(expected_conditions.presence_of_element_located((By.NAME, 'text')))
    print("Page is ready!")

except TimeoutException:
    print("Loading took too much time!")

input_job.send_keys('python')
driver.find_element(By.XPATH,
                    '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div[1]/div/div/div[2]/div/form/div/div[2]/button/span/span[2]').click()

print([button.click() for button in driver.find_elements(By.CSS_SELECTOR, '.vacancy-serp-actions a')])
