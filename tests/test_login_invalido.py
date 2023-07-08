import pytest

from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
# switch de teste pode ser utilizada para rodar o teste individualmente pytest -v -m login
@pytest.mark.login
class TestCT03:
    def test_ct03_login_invalido(self):
        login_page = LoginPage()

        login_page.fazer_login("standard_user", "1234")
        login_page.verifica_login_invalido()
        # driver = conftest.driver

        # assert driver.find_element(By.XPATH, "//*[@class='error-message-container error']").is_displayed()

        # verifica se nao está visivel o texto da pagina de produtos
        # usar find elements pq retorna true ou false como retorna uma lista valido se está vazia
        # assert len(driver.find_elements(By.XPATH, "//span[@class='title']")) == 0
