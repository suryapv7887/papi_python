import pytest

from pages.login_page import LoginPage

class TestLogin:
    def test_login_valid_credentials(self, setup):
        login_page = LoginPage(setup)
        login_page.login("dev@simelabs.in", "1~5An)4VlQrl")
        assert "Employee Profile" in login_page.profile_title()


