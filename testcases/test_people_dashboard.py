import time
from pages.people_dashboard_page import DashboardPage
import pytest

from utils.helpers import Helpers


@pytest.mark.usefixtures("login_user","logger")
class Test_PeopleDashboard:

    def test_navigate_to_regular_employees(self, login_user,logger):
        dashboard = DashboardPage(login_user,logger)
        dashboard.click_regular_employees()
        header_text_1 = dashboard.get_header_text()
        assert "People Master-Employeesss" in header_text_1, f"Expected 'People Master-Employees' in header, got '{header_text_1}'"
        logger.info(header_text_1)

    @pytest.mark.skip
    def test_navigate_to_contract_employees(self, login_user,logger):
        dashboard = DashboardPage(login_user,logger)
        dashboard.click_contract_employees()
        #assert result, "Failed to click on 'Contract Employees'"
        header_text_2 = dashboard.get_header_text()
        logger.info(header_text_2)
        assert "People Master-Contractors" in header_text_2, f"Expected 'People Master-Contractors' in header, got '{header_text_2}'"



