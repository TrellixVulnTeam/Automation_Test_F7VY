import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestLinkNavigation(object):
    def test_link_navigation(self):
        self.driver.get(env.page_url)

        on.LinkNav.navigate_links(self)

