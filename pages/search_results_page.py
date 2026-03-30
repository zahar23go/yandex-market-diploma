"""Page Object для страницы результатов поиска"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class SearchResultsPage(BasePage):
    """Страница результатов поиска"""

    PRODUCTS = (By.CSS_SELECTOR, "[data-autotest-id='product-snippet']")

    def is_results_displayed(self) -> bool:
        with allure.step("Проверить отображение результатов"):
            return len(self.driver.find_elements(*self.PRODUCTS)) > 0

    def get_products_count(self) -> int:
        with allure.step("Получить количество товаров"):
            return len(self.driver.find_elements(*self.PRODUCTS))