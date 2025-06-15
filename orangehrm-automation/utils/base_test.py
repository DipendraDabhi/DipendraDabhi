import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class BaseTest:
    def setup_method(self):
        # Suppress TensorFlow and internal logs
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

        # ChromeOptions to suppress ChromeDriver logs
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")  # Suppress INFO/WARN
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        # Setup ChromeDriver with options
        self.driver = webdriver.Chrome(
            service=Service(),  # Automatically uses default chromedriver in PATH
            options=chrome_options
        )

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def teardown_method(self):
        self.driver.quit()
