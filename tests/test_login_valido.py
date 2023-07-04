from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #instancia webdriver
driver.implicitly_wait(5) #espera implicita
driver.maximize_window() #maximiza a tela
driver.get('https://www.saucedemo.com/')

 #encontra o input de usuario por id e seta um valor nele atraves do "send_keys"
driver.find_element(By.ID, "user-name").send_keys("standard_user")

#encontra o input de senha por id e seta um valor nele atraves do "send_keys"
driver.find_element(By.ID, "password").send_keys("secret_sauce")

#encontra  o botao de login e clica
driver.find_element(By.ID, "login-button").click()

#valida se logou conferindo o titulo está visivel da pagina que abriu após o clique no botao login
assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
