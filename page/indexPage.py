from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class IndexPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_login_success(self):
        try:
            self.driver.find_element(By.XPATH, '//a[text()="退出"]')
        except:
            res = "登录失败"
        else:
            res = "登录成功"
        return res
