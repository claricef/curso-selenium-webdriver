import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage): #herda a basepage pode usar os metodos dela

    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.mensagem_login_invalido = (By.XPATH, "//*[@class='error-message-container error']")


    def fazer_login(self, usuario, senha):
        #self.driver.find_element(*self.username_field).send_keys(usuario)
        #self.driver.find_element(*self.password_field).send_keys(senha)
        #self.driver.find_element(*self.login_button).click()

        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)

    def verifica_login_invalido(self):
       self.verificar_se_elemento_existe(self.mensagem_login_invalido)

  


