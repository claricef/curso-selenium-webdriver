from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bolt T-Shirt']").is_displayed()

driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("maria")
driver.find_element(By.ID, "last-name").send_keys("sousa")
driver.find_element(By.ID, "postal-code").send_keys("123")

driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()
assert driver.find_element(By.XPATH, "//*[@class='complete-header']").is_displayed()



