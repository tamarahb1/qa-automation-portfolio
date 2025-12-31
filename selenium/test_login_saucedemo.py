"""
Automated Login Test for Sauce Demo
Application: https://www.saucedemo.com
Purpose: Portfolio demonstration using public demo application
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_valid_login():
    # Initialize browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Navigate to Sauce Demo
        driver.get("https://www.saucedemo.com")

        # Locate login fields
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")

        # Enter credentials
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        password.send_keys(Keys.RETURN)

        time.sleep(2)

        # Validate successful login
        assert "inventory" in driver.current_url
        print("Login test passed")

    finally:
        driver.quit()
