import pytest
import allure
import requests
from config.settings import Config
from config.test_data import TestData

@allure.feature("API Тесты Яндекс Маркета")
class TestAPISearch:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.base_url = Config.API_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        yield
        self.session.close()
    
    @allure.title("API Тест 1: Поиск по одному слову")
    @pytest.mark.api
    def test_api_search_single_word(self):
        response = self.session.get(
            f"{self.base_url}/api/v1/search",
            params={"text": TestData.SEARCH_QUERIES["single_word"]}
        )
        assert response.status_code == 200
        data = response.json()
        assert "products" in data
    
    @allure.title("API Тест 2: Получение подсказок")
    @pytest.mark.api
    def test_api_get_suggestions(self):
        response = self.session.get(
            f"{self.base_url}/api/v1/suggest",
            params={"text": TestData.SEARCH_QUERIES["partial"]}
        )
        assert response.status_code == 200
        data = response.json()
        assert "suggestions" in data
        assert len(data["suggestions"]) > 0
    
    @allure.title("API Тест 3: Поиск несуществующего товара")
    @pytest.mark.api
    def test_api_search_non_existent(self):
        response = self.session.get(
            f"{self.base_url}/api/v1/search",
            params={"text": TestData.SEARCH_QUERIES["non_existent"]}
        )
        assert response.status_code == 200
        data = response.json()
        assert data.get("total", 0) == 0
    
    @allure.title("API Тест 4: Поиск с номером модели")
    @pytest.mark.api
    def test_api_search_with_number(self):
        response = self.session.get(
            f"{self.base_url}/api/v1/search",
            params={"text": TestData.SEARCH_QUERIES["with_number"]}
        )
        assert response.status_code == 200
        data = response.json()
        assert "products" in data
    
    @allure.title("API Тест 5: Поиск с жалобным запросом")
    @pytest.mark.api
    def test_api_search_complaint(self):
        response = self.session.get(
            f"{self.base_url}/api/v1/search",
            params={"text": TestData.SEARCH_QUERIES["complaint"]}
        )
        assert response.status_code == 200
        data = response.json()
        response_text = str(data).lower()
        assert "support" in response_text or "помощь" in response_text
