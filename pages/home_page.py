from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.botao_adicionar_carrinho = (By.XPATH, "//*[text()='Add to cart']")
        self.icone_carrinho = (By.XPATH, "//*[@class='shopping_cart_link']")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        # formata a string montando um novo locator adicionando no lugar das {} o nome do item passado - locator dinamico
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item)) #encontra o elemento
        self.clicar(item) # clica no elemento
        self.clicar(self.botao_adicionar_carrinho) # clica no botao para adicionar o item ao carrinho

    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)
