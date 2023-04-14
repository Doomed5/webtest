import pytest
from page.LoginPage import LoginPage
from page.indexPage import IndexPage
from datas.login_data import LoginData


class TestLogin:

    @pytest.mark.parametrize('case', LoginData.success_case_data)
    def test_login_pass(self, case, login_fixture):
        driver = login_fixture
        login_page = LoginPage(driver)
        login_page.login(case['mobile'], case['pwd'])
        index_page = IndexPage(driver)
        res = index_page.is_login_success()
        assert res == case['excepted']

    @pytest.mark.parametrize('case', LoginData.error_case_data)
    def test_login_mobile_error(self, case, login_fixture):
        driver = login_fixture
        login_page = LoginPage(driver)
        login_page.login(case['mobile'], case['pwd'])
        res = login_page.get_page_error_info()
        assert res == case['excepted']

    @pytest.mark.parametrize('case', LoginData.error_alert_data)
    def test_login_fail_pop_window(self, case, login_fixture):
        driver = login_fixture
        login_page = LoginPage(driver)
        login_page.login(case['mobile'], case['pwd'])
        res = login_page.get_pop_window_error_info()
        assert res == case['excepted']
