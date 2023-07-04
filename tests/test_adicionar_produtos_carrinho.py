from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')


driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

#clica no link para abrir o produto
driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
#adiciona produto ao carrinho
driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
#clica no carrinho
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

#valida se o produto está exibindo na pagina - se adicionou ao carrinho
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

#volta e adiciona um novo item
driver.find_element(By.ID, "continue-shopping").click()
driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").click()
driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

#valida se os dois itens estão exibindo na tela - se os dois produtos foram adicionados no carrinho
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()