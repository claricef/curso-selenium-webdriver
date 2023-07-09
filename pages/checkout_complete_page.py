from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.text_complete_header = (By.XPATH, "//*[@class='complete-header']")

    def verifica_header_existe(self):
        self.verificar_se_elemento_existe(self.text_complete_header)

    def verifica_texto_header(self, texto_esperado):
        texto_encontrado = self.capturar_texto_elemento(self.text_complete_header)
        assert texto_encontrado == texto_esperado,  f"O texto retornado foi '{texto_encontrado}', mas era esperado '{texto_esperado}'"