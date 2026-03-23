from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class SearchPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='text']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    @allure.step("Open search page")
    def open_search_page(self):
        self.open(self.driver.base_url)
    
    @allure.step("Search for: {query}")
    def search(self, query):
        self.input_text(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)
    
    @allure.step("Check if search button is enabled")
    def is_search_button_enabled(self):
        button = self.find_element(self.SEARCH_BUTTON)
        return button.is_enabled()
