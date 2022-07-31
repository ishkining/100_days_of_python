from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = 'N:/Development/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

python_org_dict = {}

driver.get('https://www.python.org')
assert "Python" in driver.title
menu = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')[0].text.split('\n')
for index in range(0, len(menu), 2):
    python_org_dict[index] = {'time': f'2022-{menu[index]}', 'name': menu[index+1]}
assert "No results found." not in driver.page_source

print(python_org_dict)
driver.quit()