import time

import pytest
from pages.new_regular_employee_page import NEW_REGULAR_EMPLOYEE
from pages.people_dashboard_page import DashboardPage
from testdata.regular_employee import PeopleData

@pytest.mark.skip
def test_navigate_to_add_employee_form(login_user):
    dashboard_page = DashboardPage(login_user)
    dashboard_page.click_regular_employees()

    employee_form_page = NEW_REGULAR_EMPLOYEE(login_user)
    employee_form_page.click_add_employee()
    assert employee_form_page.is_displayed(), "Employee form page did not load successfully"

def test_fill_regular_basic_details(login_user):
    employee_data = PeopleData.ADD_EMPLOYEE_DATA

    dashboard_page = DashboardPage(login_user)
    dashboard_page.click_regular_employees()

    employee_form_page = NEW_REGULAR_EMPLOYEE(login_user)
    employee_form_page.click_add_employee()

    employee_form_page.fill_basic_info(
        employee_data["first_name"],
        employee_data["last_name"],
        employee_data["email"],
        employee_data["mobile"],
        employee_data["linkedin"])
    employee_form_page.fill_personal_details(
        employee_data["dob"],
        employee_data["age"],
        employee_data["blood_group"],
        employee_data["gender"],
        employee_data["marital_status"]
    )

    employee_form_page.fill_address_details(
        present_address=employee_data["present_address"],
        permanent_address=employee_data.get("Permanent_address"),
        same_as_present=employee_data.get("same_as_present", False)
    )
    employee_form_page.fill_bank_details(
        employee_data["aadhar"],
        employee_data["aadhar_file"],
        employee_data["pan"],
        employee_data["pan_file"],
        employee_data["bank"],
        employee_data["account_number"],
        employee_data["ifsc"],
        employee_data["passport_file"]
    )
    employee_form_page.fill_Emergency_details(
        employee_data["emergency_name"],
        employee_data["emergency_contact"]
    )
    employee_form_page.upload_employment_documents(
        employee_data["releiving_letter_file"],
        employee_data["payslips_file"],
        employee_data["experience_certificate_file"],
        employee_data["educational_certificate_file"]
    )
    employee_form_page.update_insurance_details(
        dependent_data=employee_data.get["dependent_data"],
        Insurance_required=employee_data.get["insurance_required"]
    )

