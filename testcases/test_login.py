import pytest
from configurations.config import Config
from pages.login_page import LoginPage
import pytest

<<<<<<< HEAD
=======
@pytest.mark.usefixtures("setup")
>>>>>>> f2ad849fc8254f0190824d4ff5933248258d6483
class TestLogin:
    def test_login_valid_credentials(self, setup):
        login_page = LoginPage(setup)
        login_page.login(Config.LOGIN_USERNAME, Config.LOGIN_PASSWORD)
        assert "Employee Profile" in login_page.profile_title()

