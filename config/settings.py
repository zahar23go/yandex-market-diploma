"""Настройки окружения проекта"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Класс с настройками окружения"""

    BASE_URL = os.getenv("BASE_URL", "https://market.yandex.ru")
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.market.yandex.ru")

    API_KEY = os.getenv("API_KEY", "")
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))


settings = Settings()