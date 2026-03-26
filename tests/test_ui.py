import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

BASE_URL = "https://market.yandex.ru"

class TestYandexMarketUI:
    
    @pytest.fixture
    def driver(self):
        """Setup Chrome driver"""
        try:
            from webdriver_manager.chrome import ChromeDriverManager
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
        except:
            driver = webdriver.Chrome()
        
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.quit()
    
    def test_page_title(self, driver):
        """Test page title contains expected text"""
        driver.get(BASE_URL)
        time.sleep(2)
        title = driver.title
        print(f"Page title: {title}")
        
        # Check for Russian or English text using Unicode
        has_market = "Market" in title
        has_market_ru = "\u041c\u0430\u0440\u043a\u0435\u0442" in title  # "??????" in Unicode
        has_yandex = "Yandex" in title
        has_yandex_ru = "\u042f\u043d\u0434\u0435\u043a\u0441" in title  # "??????" in Unicode
        
        assert (has_market or has_market_ru or has_yandex or has_yandex_ru), \
            f"Unexpected title: {title}"
    
    def test_page_loads(self, driver):
        """Test page loads successfully"""
        driver.get(BASE_URL)
        time.sleep(2)
        current_url = driver.current_url
        print(f"Current URL: {current_url}")
        assert "market.yandex.ru" in current_url