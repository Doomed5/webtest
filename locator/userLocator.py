from selenium.webdriver.common.by import By


class LoginLocator:
    mobile_loc = (By.XPATH, '//input[@placeholder="请输入邮箱/手机号/账号"]')
    pwd_loc = (By.XPATH, '//input[@placeholder="请输入密码"]')
    login_btn_loc = (By.XPATH, '//button[@class="el-button el-button--primary el-button--medium"]')
    page_error_info_loc = (By.XPATH, '//div[@class="el-form-item__error"]')
    pop_window_info_loc = (By.XPATH, '//p[@class="el-message__content"]')