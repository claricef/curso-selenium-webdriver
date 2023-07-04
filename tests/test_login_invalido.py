from selenium import webdriver
from selenium.webdriver.common.by import By

driver: webdriver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.ID, "login-button").click()

assert driver.find_element(By.XPATH, "//*[@class='error-message-container error']").is_displayed()

