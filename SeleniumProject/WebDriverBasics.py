
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="\\Users\\nibirhasan\\Downloads\\chromedriver")
driver.implicitly_wait(5)
driver.get("https://www.google.com")
driver.find_element(By.NAME, 'q').send_keys("naveen automationlabs")
driver.find_elements(By.CSS_SELECTOR, '')
driver.maximize_window()
time.sleep(10)


