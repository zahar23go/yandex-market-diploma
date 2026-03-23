from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class SearchResultsPage(BasePage):
    PRODUCT_CARD = (By.CSS_SELECTOR, ".product-card")
    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, ".no-results")
    
    @allure.step("Get results count")
    def get_results_count(self):
        products = self.driver.find_elements(*self.PRODUCT_CARD)
        return len(products)
    
    @allure.step("Check if results are displayed")
    def are_results_displayed(self):
        return self.get_results_count() > 0
    
    @allure.step("Check if no results message is displayed")
    def is_no_results_message_displayed(self):
        try:
            return self.driver.find_element(*self.NO_RESULTS_MESSAGE).is_displayed()
        except:
            return False
