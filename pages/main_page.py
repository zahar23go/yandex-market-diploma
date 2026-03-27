"""Page Object для главной страницы"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    """Главная страница Яндекс Маркет"""

    SEARCH_INPUT = (By.ID, "header-search")

    def open(self) -> None:
        with allure.step("Открыть главную страницу"):
            super().open("https://market.yandex.ru")

    def search_product(self, query: str) -> None:
        with allure.step(f"Поиск товара '{query}'"):
            element = self.find_element(self.SEARCH_INPUT)
            element.clear()
            element.send_keys(query)
            element.send_keys(Keys.RETURN)