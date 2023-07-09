import conftest


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator) #usando o * o python entende que o by é o primeiro parametro e o user_name é o segundo parametro, que é esperado pelo find element

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def escrever(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def clicar(self,locator):
        self.encontrar_elemento(locator).click()

    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), "O elemento '{locator}' não foi encontrado na tela"


    def capturar_texto_elemento(self, locator):
        return self.encontrar_elemento(locator).text