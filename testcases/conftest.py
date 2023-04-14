import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def login_fixture():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://www.ketangpai.com/#/login')
    yield driver
    driver.quit()

