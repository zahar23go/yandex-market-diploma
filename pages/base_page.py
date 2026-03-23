from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
from config.settings import Config

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.DEFAULT_TIMEOUT)
    
    @allure.step("Open page: {url}")
    def open(self, url):
        self.driver.get(url)
    
    @allure.step("Find element")
    def find_element(self, locator, timeout=Config.DEFAULT_TIMEOUT):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Element {locator} not found")
    
    @allure.step("Click element")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    @allure.step("Input text: {text}")
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Attach screenshot")
    def attach_screenshot(self):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
