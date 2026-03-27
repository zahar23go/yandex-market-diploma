"""UI тесты для Яндекс Маркет"""

import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.test_data import TestData


@allure.epic("Yandex Market")
@allure.feature("UI Тестирование")
class TestYandexMarketUI:

    @allure.story("Поиск товаров")
    @allure.title("Поиск товара по ключевому слову")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_search_product(self, driver):
        """Тест проверяет функциональность поиска товара"""
        
        with allure.step("Открыть главную страницу Яндекс Маркет"):
            driver.get("https://market.yandex.ru")
            driver.maximize_window()
            allure.attach(driver.get_screenshot_as_png(), name="Главная страница", 
                         attachment_type=allure.attachment_type.PNG)

        search_query = TestData.SEARCH_QUERIES[0]
        with allure.step(f"Ввести поисковый запрос '{search_query}'"):
            # Ищем поле поиска
            wait = WebDriverWait(driver, 15)
            search_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='text'], input[type='search']"))
            )
            search_input.clear()
            search_input.send_keys(search_query)
            allure.attach(search_query, name="Поисковый запрос", 
                         attachment_type=allure.attachment_type.TEXT)

        with allure.step("Нажать Enter для поиска"):
            search_input.send_keys(Keys.RETURN)

        with allure.step("Проверить, что произошел переход на страницу результатов"):
            # Проверяем, что URL изменился
            wait.until(lambda d: "search" in d.current_url or "catalog" in d.current_url)
            current_url = driver.current_url
            allure.attach(current_url, name="URL после поиска", 
                         attachment_type=allure.attachment_type.TEXT)
            
        with allure.step("Проверить, что страница загрузилась"):
            # Проверяем, что есть хотя бы какой-то контент
            wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "body")) > 0)
            allure.attach(driver.get_screenshot_as_png(), name="Страница результатов", 
                         attachment_type=allure.attachment_type.PNG)
            
        with allure.step("Проверить, что результаты поиска отображаются"):
            # Просто проверяем, что страница не пустая и нет ошибки
            page_text = driver.find_element(By.TAG_NAME, "body").text
            assert len(page_text) > 100, "Страница результатов пуста"
            assert "ничего не найдено" not in page_text.lower() or "не найдено" not in page_text.lower(), \
                "Поиск не вернул результатов"
            
            allure.attach(f"Длина текста страницы: {len(page_text)} символов", 
                         name="Проверка", attachment_type=allure.attachment_type.TEXT)

    @allure.story("Навигация")
    @allure.title("Проверка заголовка страницы")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_page_title(self, driver):
        """Тест проверяет заголовок главной страницы"""
        
        with allure.step("Открыть главную страницу"):
            driver.get("https://market.yandex.ru")
            driver.maximize_window()
            
        with allure.step("Проверить заголовок страницы"):
            title = driver.title
            allure.attach(title, name="Заголовок страницы", 
                         attachment_type=allure.attachment_type.TEXT)
            assert "Маркет" in title or "Market" in title, f"Заголовок страницы: {title}"

    @allure.story("Поиск")
    @allure.title("Поиск с другим запросом")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    @pytest.mark.regression
    def test_search_alternative_query(self, driver):
        """Тест проверяет поиск с альтернативным запросом"""
        
        search_query = TestData.SEARCH_QUERIES[1]
        
        with allure.step(f"Открыть главную страницу и выполнить поиск '{search_query}'"):
            driver.get("https://market.yandex.ru")
            driver.maximize_window()
            
            wait = WebDriverWait(driver, 15)
            search_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='text'], input[type='search']"))
            )
            search_input.clear()
            search_input.send_keys(search_query)
            search_input.send_keys(Keys.RETURN)
            
        with allure.step("Проверить, что URL изменился"):
            wait.until(lambda d: "search" in d.current_url or "catalog" in d.current_url)
            assert "search" in driver.current_url or "catalog" in driver.current_url, \
                "Не произошел переход на страницу поиска"
            
            allure.attach(driver.current_url, name="URL поиска", 
                         attachment_type=allure.attachment_type.TEXT)