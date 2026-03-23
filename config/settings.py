import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv('BASE_URL', 'https://market-delivery.yandex.ru')
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://api.market-delivery.yandex.ru')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    BROWSER = os.getenv('BROWSER', 'chrome')
    DEFAULT_TIMEOUT = 10
    IMPLICIT_WAIT = 5
    TEST_LOCATION = os.getenv('TEST_LOCATION', 'Москва')
