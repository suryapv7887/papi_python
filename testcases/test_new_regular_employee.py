import logging
import pytest
from pages.new_regular_employee_page import NEW_REGULAR_EMPLOYEE
from pages.people_dashboard_page import DashboardPage
from testdata.regular_employee import PeopleData
from utils.helpers import Helpers

@pytest.mark.usefixtures("login_user")
class TestAddNewRegularEmployee:

    @pytest.fixture(autouse=True)
    def setup_pages(self, login_user):
        self.driver = login_user
        self.dashboard_page = DashboardPage(self.driver)
        self.employee_form_page = NEW_REGULAR_EMPLOYEE(self.driver)
        self.employee_data = PeopleData.ADD_EMPLOYEE_DATA

        self.dashboard_page.click_regular_employees()
        self.employee_form_page.click_add_employee()
        self.logger = Helpers.use_logger()

    #@pytest.mark.parametrize("employee_data", PeopleData.ADD_EMPLOYEE_DATA)
    def test_fill_new_employee_details(self):
        self.logger.info("Started New employee update")
        self.employee_form_page.fill_basic_details(
            self.employee_data["first_name"],
            self.employee_data["last_name"],
            self.employee_data["email"],
            self.employee_data["mobile"],
            self.employee_data["linkedin"]
        )
        self.logger.info("Updated Basic details")
        self.logger.info("Filling Personal details")
        self.employee_form_page.fill_personal_details(
            self.employee_data["dob"],
            self.employee_data["age"],
            self.employee_data["blood_group"],
            self.employee_data["gender"],
            self.employee_data["marital_status"]
        )
        self.logger.info("Updated Personal details")

        self.logger.info("Filling Address details")
        self.employee_form_page.fill_address_details(
            present_address=self.employee_data["present_address"],
            permanent_address=self.employee_data.get("permanent_address"),
            same_as_present=self.employee_data.get("same_as_present")
        )
        self.logger.info("Updated address details")

        self.logger.info("Filling Bank details")
        self.employee_form_page.fill_bank_details(
            self.employee_data["aadhar"],
            self.employee_data["aadhar_file"],
            self.employee_data["pan"],
            self.employee_data["pan_file"],
            self.employee_data["bank"],
            self.employee_data["account_number"],
            self.employee_data["ifsc"],
            self.employee_data["passport_file"]
        )
        self.logger.info("Updated Bank details")
        self.logger.info("Filling Emergency details")
        self.employee_form_page.fill_emergency_details(
            self.employee_data["emergency_name"],
            self.employee_data["emergency_contact"]
        )
        self.logger.info("Updated Emergency details")
        self.logger.info("Filling employment details")
        self.employee_form_page.upload_employment_documents(
            self.employee_data["releiving_letter_file"],
            self.employee_data["payslips_file"],
            self.employee_data["experience_certificate_file"],
            self.employee_data["educational_certificate_file"]
        )
        self.logger.info("Updated employment details")
        self.logger.info("Filling Insurance details")
        self.employee_form_page.update_insurance_details(
            dependent_data=self.employee_data.get("dependent_data"),
            Insurance_required=self.employee_data.get("insurance_required")
        )
        self.logger.info("Updated Insurance details")
        self.logger.info("Filling PF details")
        self.employee_form_page.update_PF_and_Gratuity_details(
            PF_data=self.employee_data.get("PF_data"),
            PF_required=self.employee_data.get("PF_required"),
            Gratuity_data=self.employee_data.get("Gratuity_data")
        )
        self.logger.info("Updated PF details")
        self.logger.info("Filling Skill details")
        self.employee_form_page.update_skill_details(
            category=self.employee_data["skill_category"],
            skill=self.employee_data["skill"],
            experience_years=self.employee_data["experience_years"],
            experience_months=self.employee_data["experience_months"],
            #proficiency=self.employee_data["proficiency"]
        )
        self.logger.info("Updated Skill details")
        self.logger.info("Filling Work details")
        self.employee_form_page.update_work_details(
            self.employee_data["department"],
            self.employee_data["title"],
            self.employee_data["L2_manager"],
            self.employee_data["L3_manager"],
            self.employee_data["official_email"],
            self.employee_data["total_experience"],
            self.employee_data["location"],
            self.employee_data["work_mode"]
        )
        self.logger.info("Updated Work details")
        self.logger.info("Filling Education details")
        self.employee_form_page.fill_education_details(
            self.employee_data["institution"],
            self.employee_data["degree"],
            self.employee_data["field"],
            self.employee_data["year"],
        )
        self.logger.info("Updated Education details")

        self.logger.info("Submit the employment details")
        message = self.employee_form_page.submit_details_and_verify_message()
        assert "Employee added successfully" in message, f"Expected success message not found. Actual message: '{message}'"
        self.logger.info("Added New Employee details")
