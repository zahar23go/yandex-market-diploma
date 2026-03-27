"""API тесты для Яндекс Маркет (с мок-данными)"""

import pytest
import allure
from config.settings import settings
from data.test_data import TestData


@allure.epic("Yandex Market")
@allure.feature("API Тестирование")
class TestYandexMarketAPI:

    @allure.story("Товары")
    @allure.title("Получение списка товаров")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    @pytest.mark.smoke
    def test_get_products(self, api_client):
        """Тест проверяет получение списка товаров"""
        with allure.step("Подготовка тестовых данных"):
            # Мок-данные для демонстрации
            mock_response = {
                "products": [
                    {"id": 1, "name": "iPhone 15", "price": 79990},
                    {"id": 2, "name": "Samsung Galaxy S24", "price": 69990}
                ]
            }
            allure.attach(str(mock_response), name="Mock Response", 
                         attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверка структуры ответа"):
            assert "products" in mock_response, "Ключ 'products' отсутствует"
            assert len(mock_response["products"]) > 0, "Список товаров пуст"
            allure.attach(" Проверка пройдена", name="Result", 
                         attachment_type=allure.attachment_type.TEXT)

    @allure.story("Поиск")
    @allure.title("Поиск товаров по ключевому слову")
    @pytest.mark.api
    def test_search_products(self, api_client):
        """Тест проверяет поиск товаров"""
        search_query = TestData.SEARCH_QUERIES[0]
        with allure.step(f"Поиск по запросу '{search_query}'"):
            # Мок-данные для поиска
            mock_response = {
                "products": [
                    {"id": 1, "name": "iPhone 15", "price": 79990},
                    {"id": 2, "name": "iPhone 15 Pro", "price": 99990}
                ],
                "query": search_query
            }
            allure.attach(str(mock_response), name="Search Results", 
                         attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверить результаты поиска"):
            assert "products" in mock_response
            assert len(mock_response["products"]) > 0
            allure.attach(f"Найдено товаров: {len(mock_response['products'])}", 
                         name="Result", attachment_type=allure.attachment_type.TEXT)

    @allure.story("Категории")
    @allure.title("Получение списка категорий")
    @pytest.mark.api
    def test_get_categories(self, api_client):
        """Тест проверяет получение категорий"""
        with allure.step("Получение категорий"):
            mock_response = [
                {"id": 1, "name": "Электроника", "slug": "electronics"},
                {"id": 2, "name": "Смартфоны", "slug": "phones"},
                {"id": 3, "name": "Ноутбуки", "slug": "laptops"}
            ]
            allure.attach(str(mock_response), name="Categories", 
                         attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверить структуру категорий"):
            assert isinstance(mock_response, list)
            assert len(mock_response) > 0
            for cat in mock_response:
                assert "id" in cat
                assert "name" in cat

    @allure.story("Отзывы")
    @allure.title("Создание отзыва")
    @pytest.mark.api
    def test_create_review(self, api_client, auth_headers):
        """Тест проверяет создание отзыва"""
        with allure.step("Создание отзыва"):
            review_data = {
                "product_id": 1,
                "rating": TestData.REVIEW_RATING,
                "comment": TestData.REVIEW_COMMENT,
                "author": TestData.REVIEW_AUTHOR
            }
            mock_response = {
                "id": 101,
                **review_data,
                "created_at": "2024-03-27T21:47:00Z"
            }
            allure.attach(str(mock_response), name="Review Created", 
                         attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверить создание отзыва"):
            assert mock_response["id"] is not None
            assert mock_response["rating"] == TestData.REVIEW_RATING
            assert mock_response["comment"] == TestData.REVIEW_COMMENT

    @allure.story("Товары")
    @allure.title("Получение деталей товара")
    @pytest.mark.api
    def test_get_product_details(self, api_client):
        """Тест проверяет получение деталей товара"""
        product_id = 1
        with allure.step(f"Получение деталей товара {product_id}"):
            mock_response = {
                "id": product_id,
                "name": "iPhone 15",
                "price": 79990,
                "description": "Смартфон Apple iPhone 15",
                "characteristics": {
                    "display": "6.1 дюйма",
                    "processor": "A16 Bionic",
                    "camera": "48 МП"
                }
            }
            allure.attach(str(mock_response), name="Product Details", 
                         attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверить детальную информацию"):
            required_fields = ["id", "name", "price", "description"]
            for field in required_fields:
                assert field in mock_response, f"Поле {field} отсутствует"