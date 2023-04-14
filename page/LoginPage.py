from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator.userLocator import LoginLocator as loc
from page.basepage import BasePage


class LoginPage(BasePage):

    def login(self, mobile, pwd):
        # 输入账号
        self.input_send_keys(loc.mobile_loc, mobile, '登录页面账号输入框')
        # 输入密码
        self.input_send_keys(loc.pwd_loc, pwd, '登录页面密码输入框')
        # self.driver.find_element(*loc.pwd_loc).send_keys(pwd)
        # 点击登录
        # ele = self.driver.find_element(*loc.login_btn_loc)
        ele = self.get_element(loc.login_btn_loc, '登录页面登录按钮')
        self.driver.execute_script("arguments[0].click()", ele)

    def get_page_error_info(self):
        # 获取页面错误信息
        # res = self.driver.find_element(*loc.page_error_info_loc).text
        res = self.get_element_text(loc.page_error_info_loc, '登录页面获取页面错误信息')
        return res

    def get_pop_window_error_info(self):
        # 获取弹窗错误信息
        # ele = WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(
        #     loc.pop_window_info_loc))
        # res = ele.text
        self.wait_element_visibility(loc.pop_window_info_loc, '登录页面获取弹窗错误信息', 10)
        res = self.get_element_text(loc.pop_window_info_loc)
        return res
