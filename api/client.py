import requests
import allure
from config.settings import Config

class APIClient:
    def __init__(self, base_url=Config.API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    @allure.step("GET request to {endpoint}")
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params)
        allure.attach(str(response.status_code), "Status Code", allure.attachment_type.TEXT)
        return response
    
    @allure.step("Search products: {query}")
    def search_products(self, query):
        return self.get("/api/v1/search", params={"text": query})
    
    @allure.step("Get suggestions: {query}")
    def get_suggestions(self, query):
        return self.get("/api/v1/suggest", params={"text": query})
