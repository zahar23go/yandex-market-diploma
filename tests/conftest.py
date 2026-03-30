"""Фикстуры для тестов"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import requests
from config.settings import settings


@pytest.fixture
def driver():
    """Фикстура для WebDriver"""
    options = ChromeOptions()
    if settings.HEADLESS:
        options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(settings.IMPLICIT_WAIT)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()


@pytest.fixture
def api_client():
    """Фикстура для API клиента"""
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    })
    if settings.API_KEY:
        session.headers.update({"Authorization": f"Bearer {settings.API_KEY}"})
    return session


@pytest.fixture
def auth_headers():
    """Фикстура для заголовков авторизации"""
    headers = {}
    if settings.API_KEY:
        headers["Authorization"] = f"Bearer {settings.API_KEY}"
    return headers