from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class OverviewPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.button_finish = (By.ID, "finish")

    def clicar_finish(self):
        self.clicar(self.button_finish)
