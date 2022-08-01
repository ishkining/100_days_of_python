from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

SPEED_TEST_URL = 'https://www.speedtest.net/'

chrome_driver_path = 'N:/Development/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(SPEED_TEST_URL)

speed_test_button = driver.find_element(By.CLASS_NAME, 'start-text')
speed_test_button.click()

def get_this_speed_info():
    try:
        download_speed = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                       'div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')))
        upload_speed = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                       'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')))
        # print("Speed test is ready!")

    except TimeoutException:
        print("Ohhh it is so painful!")
    return (download_speed.text, upload_speed.text)


download_speed = ''
upload_speed = ''
while download_speed == '' or download_speed == '--' or upload_speed == '' or upload_speed == '--':
    (download_speed, upload_speed) = get_this_speed_info()
print(float(download_speed))
print(float(upload_speed))

# EDITOR NOTE Twitter was blocked in Russian Federation, so I unfortunately cant use 

