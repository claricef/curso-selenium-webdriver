import pytest

from pages.carrinho_page import CarrinhoPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.overview_page import OverviewPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT04:
    def test_ct04_realizar_compra_1_produto(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        checkout_page = CheckoutPage()
        overview_page = OverviewPage()
        checkout_complete_page = CheckoutCompletePage()

        produto_1 = "Sauce Labs Backpack"
        first_name = "Maria"
        last_name = "Santos"
        postal_code = "123456"
        header_text = "Thank you for your order!"

        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.adicionar_ao_carrinho(produto_1)
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)

        # clica para checkout
        carrinho_page.clicar_checkout()

        # preenche os dados do checkout
        checkout_page.preencher_checkout(first_name, last_name, postal_code)

        # clica para continuar
        checkout_page.clicar_continuar()

        # finaliza compra
        overview_page.clicar_finish()

        # verificar se a compra foi realizada
        checkout_complete_page.verifica_header_existe()

        # verifica texto ao finalizar compra
        checkout_complete_page.verifica_texto_header(header_text)