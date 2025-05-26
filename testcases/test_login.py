import pytest
from configurations.config import Config
from pages.login_page import LoginPage
import pytest

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login_valid_credentials(self, setup):
        login_page = LoginPage(setup)
        login_page.login(Config.LOGIN_USERNAME, Config.LOGIN_PASSWORD)
        assert "Employee Profile" in login_page.profile_title()

