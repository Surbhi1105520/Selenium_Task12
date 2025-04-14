import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in")
    driver.maximize_window()
    yield driver
    driver.quit()

