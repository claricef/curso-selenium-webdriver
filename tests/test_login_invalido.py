from selenium.webdriver.common.by import By
import conftest
import pytest


@pytest.mark.usefixtures("setup_teardown")
# switch de teste pode ser utilizada para rodar o teste individualmente pytest -v -m login
@pytest.mark.login
class TestCT03:
    def test_ct03_login_invalido(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.ID, "login-button").click()

        assert driver.find_element(By.XPATH, "//*[@class='error-message-container error']").is_displayed()

        # verifica se nao está visivel o texto da pagina de produtos
        # usar find elements pq retorna true ou false como retorna uma lista valido se está vazia
        assert len(driver.find_elements(By.XPATH, "//span[@class='title']")) == 0

