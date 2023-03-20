from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set up the web driver (make sure you have the appropriate driver installed and its path is added to your system's PATH environment variable)
driver = webdriver.Chrome()

# Navigate to Google.com
driver.get('https://www.google.com')

# Find the search bar, enter your search query and press Enter
search_bar = driver.find_element(By.NAME, 'q')
search_bar.send_keys('Silicon Valley')
search_bar.send_keys(Keys.RETURN)
driver.maximize_window()
driver.close()

driver = webdriver.Chrome()

# Navigate to Google.com
driver.get('https://www.google.com')

# Find the search bar, enter your search and press Enter
search_bar = driver.find_element(By.NAME, 'q')
search_bar.send_keys('browserstack')
search_bar.send_keys(Keys.RETURN)

#Navigate to browserstack.com
driver.get('https://www.browserstack.com/')

#Log in to browser stack using email and password

sign_in_button = driver.find_element(By.XPATH, '//a[@title="Sign In"][1]').click()
email_textbox = driver.find_element(By.ID, 'user_email_login')
email_textbox.send_keys('info@scratchtechsolutions.com')


password_textbox = driver.find_element(By.ID, 'user_password')
password_textbox.send_keys('Surma2009?')
click_on_signIn = driver.find_element(By.XPATH, '//input[@type="submit"][1]').click()
time.sleep(10)






