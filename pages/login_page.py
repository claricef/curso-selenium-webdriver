import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage): #herda a basepage pode usar os metodos dela

    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message_login = (By.XPATH, "//*[@class='error-message-container error']")


    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)

    def verifica_login_invalido(self):
       self.verificar_se_elemento_existe(self.error_message_login)

    def verificar_texto_mensagem_erro_login(self, texto_esperado):
        texto_encontrado = self.capturar_texto_elemento(self.error_message_login)
        assert texto_encontrado == texto_esperado, f"O texto retornado foi '{texto_encontrado}', mas era esperado '{texto_esperado}'"




