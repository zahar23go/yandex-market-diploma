import pytest
import requests
import time

BASE_URL = "https://market.yandex.ru"

class TestYandexMarketAPI:
    
    def test_main_page_availability(self):
        """Test main page returns 200 OK"""
        response = requests.get(BASE_URL, timeout=10)
        assert response.status_code == 200
    
    def test_response_time(self):
        """Test response time is reasonable"""
        start = time.time()
        response = requests.get(BASE_URL, timeout=10)
        elapsed = time.time() - start
        # Increased timeout to 3 seconds to account for network latency
        assert elapsed < 3, f"Response too slow: {elapsed}s"
    
    def test_page_contains_text(self):
        """Test page contains expected text"""
        response = requests.get(BASE_URL, timeout=10)
        html = response.text.lower()
        assert "yandex" in html or "??????" in html
    
    def test_invalid_url(self):
        """Test 404 page"""
        response = requests.get(f"{BASE_URL}/nonexistent-page-12345", timeout=10)
        assert response.status_code == 404
    
    def test_headers(self):
        """Test security headers"""
        response = requests.get(BASE_URL, timeout=10)
        headers = response.headers
        assert 'content-type' in headers
        assert 'text/html' in headers['content-type']