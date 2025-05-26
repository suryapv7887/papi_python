import logging
import pytest
from pages.new_contract_employee import NewContractEmployee
from pages.people_dashboard_page import DashboardPage
from utils.helpers import Helpers

@pytest.mark.usefixtures("login_user","logger")
class TestAddNewContractEmployee:

    def test_contract_employee(self, login_user,logger):
        self.driver = login_user
        self.dashboard_page = DashboardPage(self.driver,logger)
        self.employee_form_page = NewContractEmployee(self.driver)
        self.dashboard_page.click_contract_employees()
        self.employee_form_page.click_add_employee()


