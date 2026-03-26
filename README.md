 Yandex Market Diploma Project

Описание
Автоматизация тестирования интернет-магазина Яндекс Маркет.  
Проект содержит UI и API тесты для проверки основных функций сайта.

Технологии
- Python 3.13
- Selenium WebDriver
- Pytest
- Allure
- Requests

Структура проекта
yandex-market-diploma/
├── tests/ # Тесты
│ ├── test_api.py # API тесты (5 тестов)
│ ├── test_ui.py # UI тесты (2 теста)
│ └── test_simple.py # Простые проверки
├── config/ # Конфигурация
├── pages/ # Page Object классы
├── utils/ # Вспомогательные функции
├── data/ # Тестовые данные
├── .env.example # Пример переменных окружения
├── requirements.txt # Зависимости
└── pytest.ini # Настройки pytest