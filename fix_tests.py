import os
import shutil

# Пути к файлам
TEST_UI_PATH = "tests/test_ui.py"
TEST_API_PATH = "tests/test_api.py"

def create_test_data():
    """Создание файла с тестовыми данными"""
    os.makedirs("data", exist_ok=True)
    
    content = '''# data/test_data.py
"""Тестовые данные для автоматизации"""

class TestData:
    """Класс с тестовыми данными"""
    
    # UI тестовые данные
    SEARCH_QUERY = "iPhone 15"
    MIN_PRICE = 50000
    MAX_PRICE = 100000
    
    # API тестовые данные
    REVIEW_RATING = 5
    REVIEW_COMMENT = "Отличный товар! Рекомендую к покупке."
    REVIEW_AUTHOR = "Захар"
    
    # Категории
    CATEGORY_ELECTRONICS = "Электроника"
    SUBCATEGORY_PHONES = "Смартфоны"
'''
    
    with open("data/test_data.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ test_data.py создан")

def create_pytest_ini():
    """Создание pytest.ini"""
    content = '''[pytest]
markers =
    ui: UI tests
    api: API tests
    smoke: Smoke tests
    regression: Regression tests
    slow: Slow tests

addopts = 
    -v
    --strict-markers
    --tb=short
    --alluredir=allure-results

testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
'''
    
    with open("pytest.ini", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ pytest.ini создан")

def create_env_example():
    """Создание .env.example"""
    content = '''# Yandex Market Test Configuration

# URLs
BASE_URL=https://market.yandex.ru
API_BASE_URL=https://api.market.yandex.ru

# API Authentication
API_KEY=your_api_key_here

# Browser settings
BROWSER=chrome
HEADLESS=false
WINDOW_WIDTH=1920
WINDOW_HEIGHT=1080

# Timeouts (seconds)
IMPLICIT_WAIT=10
EXPLICIT_WAIT=20

# Test data
SEARCH_QUERY=iPhone 15
MIN_PRICE=50000
MAX_PRICE=100000
'''
    
    with open(".env.example", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ .env.example создан")

def create_requirements():
    """Создание requirements.txt"""
    content = '''selenium==4.15.0
pytest==7.4.3
pytest-xdist==3.5.0
allure-pytest==2.13.2
requests==2.31.0
webdriver-manager==4.0.1
python-dotenv==1.0.0
'''
    
    with open("requirements.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ requirements.txt создан")

def fix_ui_test():
    """Добавление Allure декораторов в UI тесты"""
    if not os.path.exists(TEST_UI_PATH):
        print(f"❌ Файл {TEST_UI_PATH} не найден")
        return
    
    with open(TEST_UI_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Добавляем импорт allure если нет
    if "import allure" not in content:
        content = content.replace("import pytest", "import pytest\nimport allure")
    
    # Добавляем импорт TestData если нет
    if "from data.test_data import TestData" not in content:
        content = content.replace(
            "from pages.search_results_page import SearchResultsPage",
            "from pages.search_results_page import SearchResultsPage\nfrom data.test_data import TestData"
        )
    
    with open(TEST_UI_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ UI тесты обновлены")

def fix_api_test():
    """Добавление Allure декораторов в API тесты"""
    if not os.path.exists(TEST_API_PATH):
        print(f"❌ Файл {TEST_API_PATH} не найден")
        return
    
    with open(TEST_API_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Добавляем импорт allure если нет
    if "import allure" not in content:
        content = content.replace("import pytest", "import pytest\nimport allure")
    
    # Добавляем импорт TestData если нет
    if "from data.test_data import TestData" not in content:
        content = content.replace(
            "from config.settings import Settings",
            "from config.settings import Settings\nfrom data.test_data import TestData"
        )
    
    with open(TEST_API_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ API тесты обновлены")

def main():
    print("=" * 50)
    print("🚀 НАЧАЛО ИСПРАВЛЕНИЯ ТЕСТОВ")
    print("=" * 50)
    
    # Создаем папки
    os.makedirs("tests", exist_ok=True)
    os.makedirs("pages", exist_ok=True)
    os.makedirs("config", exist_ok=True)
    os.makedirs("utils", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    
    # Создаем файлы конфигурации
    create_test_data()
    create_pytest_ini()
    create_env_example()
    create_requirements()
    
    # Обновляем тесты
    fix_ui_test()
    fix_api_test()
    
    print("=" * 50)
    print("✅ ВСЕ ИСПРАВЛЕНИЯ ПРИМЕНЕНЫ")
    print("=" * 50)
    print("\n📝 Для запуска тестов:")
    print("  pytest -v")
    print("\n📝 Для запуска с Allure отчетом:")
    print("  pytest --alluredir=allure-results -v")
    print("  allure serve allure-results")

if __name__ == "__main__":
    main()