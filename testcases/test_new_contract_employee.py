import logging
import pytest
from pages.new_contract_employee import NEW_CONTRACT_EMPLOYEE
from pages.people_dashboard_page import DashboardPage
from utils.helpers import Helpers

@pytest.mark.usefixtures("login_user")
class TestAddNewContractEmployee:

    def test_contract_employee(self, login_user):
        self.driver = login_user
        self.dashboard_page = DashboardPage(self.driver)
        self.employee_form_page = NEW_CONTRACT_EMPLOYEE(self.driver)
        self.dashboard_page.click_contract_employees()
        self.employee_form_page.click_add_employee()


