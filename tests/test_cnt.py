import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestCNTProject(object):
    def test_cnt(self):
        self.driver.get(env.page_url)

        on.CNT.navigate_to_about_us_page(self)
        on.CNT.verify_email_address_invalid(self)

