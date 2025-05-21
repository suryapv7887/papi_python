import time
import pytest
from pages.new_contract_employee import NEW_CONTRACT_EMPLOYEE
from pages.new_regular_employee_page import NEW_REGULAR_EMPLOYEE
from pages.people_dashboard_page import DashboardPage
from testdata.regular_employee import PeopleData


class Test_ADD_NEW_CONTRACT_EMPLOYEE:
   def test_navigate_to_add_employee_form(self,login_user):
        dashboard_page = DashboardPage(login_user)
        dashboard_page.click_contract_employees()
        employee_form_page = NEW_CONTRACT_EMPLOYEE(login_user)
        employee_form_page.click_add_employee()
        assert employee_form_page.is_displayed(), "Employee form page did not load successfully"
        time.sleep(2)