# Дипломный проект: Автоматизация тестирования Яндекс Маркета

#### Описание проекта

#### Проект по автоматизации тестирования сайта Яндекс Маркет с использованием:

\-Python - язык программирования

\- Pytest - фреймворк для тестирования

\- Selenium WebDriver - для UI тестов

\- Requests - для API тестов

\- Allure - для отчетов

### Требования

\- Python 3.13+

\- Google Chrome (последняя версия)

\- Git

#### Установка и настройка

###### Клонирование репозитория

bash

git clone https://github.com/zahar23go/yandex-market-diploma.git

cd yandex-market-diploma

##### Создание виртуального окружения

bash

python -m venv venv

##### Активация виртуального окружения

Windows:

bash

venv\\Scripts\\activate

#### Установка зависимостей

bash

pip install -r requirements.txt

##### Настройка переменных окружения

Скопируйте .env.example в .env и заполните необходимые значения.

##### Команды для запуска тестов

**Все тесты (UI + API)**

bash

pytest -v

**Только API тесты**

bash

pytest -m api -v

**Только UI тесты**

bash

pytest -m ui -v

**Smoke тесты** (критическая функциональность)

bash

pytest -m smoke -v

**Регрессионные тесты**

bash

pytest -m regression -v

**Запуск с Allure отчетом**

bash

pytest --alluredir=allure-results -v

allure serve allure-results

**Параллельный запуск тестов**

bash

pytest -n auto -v

**Запуск конкретного тестового файла**

bash

pytest tests/test\_api.py -v

pytest tests/test\_ui.py -v

**Запуск конкретного теста по имени**

bash

pytest -k "test\_get\_products" -v

**Ссылка на финальный проект**

GitHub репозиторий: https://github.com/zahar23go/yandex-market-diploma

**Ветка с дипломным проектом:** diploma

**Прямая ссылка:** https://github.com/zahar23go/yandex-market-diploma/tree/diploma

Результаты тестирования

Тип тестов	        Кол-во	Результат

API тесты	        5	        Все пройдены

UI тесты	                3	        Все пройдены

Общее покрытие	8	       100% успешно

**Структура проекта**

yandex-market-diploma/

├── config/

│   └── settings.py           # Конфигурация проекта

├── data/

│   └── test\_data.py          # Тестовые данные

├── pages/

│   ├── base\_page.py          # Базовый Page Object

│   ├── main\_page.py          # Главная страница

│   └── search\_results\_page.py # Страница результатов поиска

├── tests/

│   ├── test\_api.py           # API тесты (5 шт.)

│   ├── test\_ui.py            # UI тесты (3 шт.)

│   └── conftest.py           # Фикстуры для тестов

├── .env.example              # Пример переменных окружения

├── .gitignore                # Игнорируемые файлы

├── pytest.ini                # Конфигурация pytest

├── requirements.txt          # Зависимости проекта

└── README.md                 # Документация 

**Что автоматизировано**

**API тесты (5 тестов):**

test\_get\_products - получение списка товаров

test\_search\_products - поиск товаров по ключевому слову

test\_get\_categories - получение списка категорий

test\_create\_review - создание отзыва на товар

test\_get\_product\_details - получение деталей товара

**UI тесты (3 теста):**

test\_search\_product - поиск товара по ключевому слову

test\_page\_title - проверка заголовка главной страницы

test\_search\_alternative\_query - поиск с альтернативным запросом

**Отчеты**

После запуска тестов с Allure отчет будет доступен по адресу: http://localhost:63342

**Автор**

Цирулин Захар - Дипломный проект по автоматизации тестирования

**Дата** 

29 марта 2026 г.

