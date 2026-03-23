import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config.settings import Config
from config.test_data import TestData
import time

@allure.feature("UI Тесты Яндекс Маркета")
class TestUISearch:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        chrome_options = Options()
        if Config.HEADLESS:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.implicitly_wait(Config.IMPLICIT_WAIT)
        self.driver.maximize_window()
        self.driver.get(Config.BASE_URL)
        
        yield
        self.driver.quit()
    
    @allure.title("Тест 1: Поиск по одному слову")
    @pytest.mark.ui
    def test_search_single_word(self):
        search_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='text']")
        search_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        search_input.send_keys(TestData.SEARCH_QUERIES["single_word"])
        search_button.click()
        time.sleep(2)
        
        assert TestData.SEARCH_QUERIES["single_word"] in self.driver.page_source.lower()
    
    @allure.title("Тест 2: Поиск несуществующего товара")
    @pytest.mark.ui
    def test_search_non_existent(self):
        search_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='text']")
        search_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        search_input.send_keys(TestData.SEARCH_QUERIES["non_existent"])
        search_button.click()
        time.sleep(2)
        
        assert "ничего не найдено" in self.driver.page_source.lower()
    
    @allure.title("Тест 3: Пустой поисковый запрос")
    @pytest.mark.ui
    def test_empty_search(self):
        search_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        if not search_button.is_enabled():
            assert not search_button.is_enabled()
        else:
            search_button.click()
            time.sleep(1)
            assert "введите запрос" in self.driver.page_source.lower()
    
    @allure.title("Тест 4: Поиск с номером модели")
    @pytest.mark.ui
    def test_search_with_number(self):
        search_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='text']")
        search_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        search_input.send_keys(TestData.SEARCH_QUERIES["with_number"])
        search_button.click()
        time.sleep(2)
        
        assert self.driver.current_url != Config.BASE_URL
    
    @allure.title("Тест 5: Проверка подсказок при вводе")
    @pytest.mark.ui
    def test_search_suggestions(self):
        search_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='text']")
        search_input.send_keys(TestData.SEARCH_QUERIES["partial"])
        time.sleep(2)
        
        suggestions = self.driver.find_elements(By.CSS_SELECTOR, ".suggestions-list div")
        assert len(suggestions) > 0, "Подсказки не появились"
