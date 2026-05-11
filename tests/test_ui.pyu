from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

def get_driver():
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=opts)

def test_homepage_loads():
    driver = get_driver()
    driver.get("http://localhost:5000")
    assert "Welcome" in driver.page_source
    driver.quit()

def test_form_submission():
    driver = get_driver()
    driver.get("http://localhost:5000/submit")
    driver.find_element(By.ID, "name").send_keys("TestUser")
    driver.find_element(By.ID, "submit-btn").click()
    assert "Success" in driver.page_source
    driver.quit()
