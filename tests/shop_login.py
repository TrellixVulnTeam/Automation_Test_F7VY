import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestProjectLogin(object):
    def test_successful_login(self):
        self.driver.get(env.page_url)

        on.LoginPageShop.is_title_matches(self)
        on.LoginPageShop.click_signin(self)
        on.LoginPageShop.signin_invalid_email(self)
        on.LoginPageShop.signin_invalid_password(self)
        on.LoginPageShop.signin_successful(self)


