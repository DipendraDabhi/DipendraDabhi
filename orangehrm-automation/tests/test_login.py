import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from utils.base_test import BaseTest
import time

class TestLogin(BaseTest):

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        time.sleep(10)  # optional: wait to visually confirm

        assert "dashboard" in self.driver.current_url.lower(), "Login failed or dashboard not reached"
