import pytest, time
from utils import environment as env
from utils.environment import Pages as on


@pytest.mark.usefixtures("test_setup")
class TestWebbysProject(object):
    def test_webbys_placeholder(self):
        self.driver.get(env.page_url)

        on.Webbys.identify_placeholder_image(self)

