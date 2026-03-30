"""Тестовые данные для автоматизации"""


class TestData:
    """Класс с тестовыми данными"""

    # Поисковые запросы для UI тестов
    SEARCH_QUERIES = [
        "iPhone 15",
        "Samsung Galaxy S24",
        "Xiaomi Redmi Note 13",
        "MacBook Pro",
        "Наушники Sony"
    ]
    
    # Фильтры для тестирования
    PRICE_FILTERS = [
        {"min": 50000, "max": 100000, "description": "Средний сегмент"},
        {"min": 0, "max": 30000, "description": "Бюджетный"},
        {"min": 100000, "max": 200000, "description": "Премиум"}
    ]
    
    # Категории
    CATEGORIES = {
        "electronics": "Электроника",
        "phones": "Смартфоны",
        "laptops": "Ноутбуки",
        "audio": "Наушники"
    }
    
    # API тестовые данные
    REVIEW_RATING = 5
    REVIEW_COMMENT = "Отличный товар! Полностью соответствует описанию. Рекомендую!"
    REVIEW_AUTHOR = "TestUser"