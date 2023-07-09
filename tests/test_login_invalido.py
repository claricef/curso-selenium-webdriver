import pytest

from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_ct03_login_invalido(self):
        mensagem_erro_esperada = "Epic sadface: Username and password do not match any user in this service"

        login_page = LoginPage()

        login_page.fazer_login("standard_user", "1234")

        # verifica se a mensagem de erro apareceu
        login_page.verifica_login_invalido()

        # verifica o texto da mensagem de erro
        login_page.verificar_texto_mensagem_erro_login(mensagem_erro_esperada)

