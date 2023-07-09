import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.button_continue = (By.ID, "continue")

    def preencher_checkout(self, first_name, last_name, postal_code):
       self.escrever(self.first_name_field, first_name)
       self.escrever(self.last_name_field, last_name)
       self.escrever(self.postal_code_field, postal_code)

    def clicar_continuar(self):
        self.clicar(self.button_continue)