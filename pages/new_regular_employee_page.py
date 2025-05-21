import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import none_of
from selenium.webdriver.support.wait import WebDriverWait
from locators.regular_employee_locators import Regular_EmployeeFormLocators as LOC
from utils.helpers import Helpers


class NEW_REGULAR_EMPLOYEE:

    def __init__(self, driver):
        self.driver = driver
        self.helpers = Helpers(driver)


    def click_add_employee(self):
        element = self.helpers.wait_for_element(LOC.ADD_EMPLOYEE_BUTTON, condition="clickable")
        ActionChains(self.driver).move_to_element(element).pause(2).click().perform()

    def is_displayed(self):
        return self.helpers.wait_for_element(LOC.ADD_EMPLOYEE_FORM, condition="visible", timeout=10)

    def fill_basic_details(self, first, last, email, mobile,linkedin):
        self.helpers.send_keys(LOC.FIRST_NAME, first)
        self.helpers.send_keys(LOC.LAST_NAME, last)
        self.helpers.send_keys(LOC.EMAIL, email)
        self.helpers.send_keys(LOC.MOBILE, mobile)
        self.helpers.send_keys(LOC.LINKEDIN,linkedin)

    def fill_personal_details(self,dob,age,blood_group,gender,marital_status):
        self.helpers.send_keys(LOC.DOB_FIELD, dob)
        self.helpers.send_keys(LOC.AGE_FIELD,age)
        self.helpers.wait_and_click_dropdown_option(LOC.BLOOD_GROUP_DROPDOWN, LOC.BLOOD_GROUP_OPTIONS,blood_group)
        self.helpers.wait_and_click_dropdown_option(LOC.GENDER_DROPDOWN, LOC.GENDER_OPTIONS,gender)
        self.helpers.wait_and_click_dropdown_option(LOC.MARITAL_STATUS_DROPDOWN, LOC.MARITAL_STATUS_OPTIONS,marital_status)

    def fill_address_details(self, present_address, permanent_address=None, same_as_present=None):
        self.helpers.send_keys(LOC.PRESENT_HOUSENO, present_address["house"])
        self.helpers.send_keys(LOC.PRESENT_LOCALITY, present_address["locality"])
        self.helpers.send_keys(LOC.PRESENT_STATE, present_address["state"])
        self.helpers.send_keys(LOC.PRESENT_COUNTRY, present_address["country"])
        self.helpers.send_keys(LOC.PRESENT_PINCODE, present_address["pincode"])

        if same_as_present:
            self.helpers.click(LOC.SAME_AS_PRESENT_CHECKBOX)
        elif permanent_address:
            self.helpers.send_keys(LOC.PERMANENT_HOUSENO, permanent_address["house"])
            self.helpers.send_keys(LOC.PERMANENT_LOCALITY, permanent_address["locality"])
            self.helpers.send_keys(LOC.PERMANENT_STATE, permanent_address["state"])
            self.helpers.send_keys(LOC.PERMANENT_COUNTRY, permanent_address["country"])
            self.helpers.send_keys(LOC.PERMANENT_PINCODE, permanent_address["pincode"])

    def fill_bank_details(self,aadhar,aadhar_file,pan,pan_file,bank,account_number,ifsc,passport):
        self.helpers.send_keys(LOC.AADHAR_NUMBER_BOX, aadhar)
        self.helpers.upload_file(LOC.AADHAR_FILE_UPLOAD,aadhar_file)
        self.helpers.send_keys(LOC.PAN_NUMBER_BOX, pan)
        self.helpers.upload_file(LOC.PAN_FILE_UPLOAD,pan_file)
        self.helpers.send_keys(LOC.BANK_NAME, bank)
        self.helpers.send_keys(LOC.BANK_ACCOUNT_NUMBER,account_number)
        self.helpers.send_keys(LOC.IFSC_CODE, ifsc)
        self.helpers.upload_file(LOC.PASSPORT_UPLOAD,passport)

    def fill_emergency_details(self,name,contact):
        self.helpers.send_keys(LOC.EMERGENCY_NAME,name)
        self.helpers.send_keys(LOC.EMERGENCY_CONTACT,contact)

    def upload_employment_documents(self,Relieving_Document,Payslips,Educational_Certificate,Experience_Certificate):
        self.helpers.upload_file(LOC.RELEIVING_DOCUMENT_UPLOAD,Relieving_Document)
        self.helpers.upload_file(LOC.PAYSLIPS_UPLOAD,Payslips)
        self.helpers.upload_file(LOC.EDUCATIONAL_CERTIFICATE_UPLOAD,Educational_Certificate)
        self.helpers.upload_file(LOC.EXPERIENCE_CERTIFICATE_UPLOAD,Experience_Certificate)

    def update_insurance_details(self, Insurance_required=None, dependent_data=None):
        if Insurance_required:
            self.helpers.click(LOC.INSURANCE_YES)
            self.helpers.click(LOC.ADD_DEPENDENT_BUTTON)
            if dependent_data:
                self.helpers.send_keys(LOC.DEPENDENT_NAME, dependent_data["name"])
                self.helpers.wait_and_click_dropdown_option(
                    LOC.DEPENDENT_RELATIONSHIP_DROPDOWN,
                    LOC.DEPENDENT_RELATIONSHIP_DROPDOWN_OPTIONS,
                    dependent_data["relationship"]
                )
                self.helpers.send_keys(LOC.DEPENDENT_DOB, dependent_data["dep_dob"])
        # else:
        #     self.helpers.click(LOC.INSURANCE_NO)


    def update_PF_and_Gratuity_details(self,PF_required=None, PF_data=None, Gratuity_data=None):
        if PF_required:
            self.helpers.click(LOC.PROVIDENT_FUND_YES)
            self.helpers.send_keys(LOC.UAN_NUMBER,PF_data["uan"])
            self.helpers.send_keys(LOC.PF_NOMINEE_NAME, PF_data["pf_nominee"])
            time.sleep(3)


        self.helpers.send_keys(LOC.Gratuity_NOMINEE_NAME, Gratuity_data["gratuity_nominee_name"])
        self.helpers.wait_and_click_dropdown_option(LOC.Gratuity_NOMINEE_RELATIONSHIP_DROPDOWN,
                                                        LOC.Gratuity_NOMINEE_RELATIONSHIP_DROPDOWN_OPTIONS,
                                                        Gratuity_data["gratuity_nominee_relationship"])
        self.helpers.send_keys(LOC.Gratuity_NOMINEE_AGE, Gratuity_data["gratuity_nominee_age"])
        self.helpers.send_keys(LOC.Gratuity_NOMINEE_DISTRRIBUTION,Gratuity_data["gratuity_nominee_distribution"])

    def update_skill_details(self,category,skill,experience_years,experience_months,proficiency=None):
        self.helpers.wait_and_click_dropdown_option(
            LOC.SKILL_CATEGORY_DROPDOWN,LOC.SKILL_CATEGORY_OPTIONS,category)
        self.helpers.wait_and_click_dropdown_option(LOC.SKILLS_DROPDOWN,LOC.SKILLS_OPTIONS,skill)
        self.helpers.send_keys(LOC.EXPERIENCE_YEARS,experience_years)
        self.helpers.send_keys(LOC.EXPERIENCE_MONTHS,experience_months)
        #self.helpers.click_button(LOC.SKILL_RATINGS,proficiency)
        time.sleep(3)

    def update_work_details(self, Department, Title, L2_manager, L3_manager, official_email, Total_experience, Location,
                            work_mode=None):
        self.helpers.wait_and_click_dropdown_option(
            LOC.DEPARTMENT_DROPDOWN,LOC.DEPARTMENT_DROPDOWN_OPTIONS,Department  )
        self.helpers.wait_and_click_dropdown_option(
            LOC.TITLE_DROPDOWN,LOC.TITLE_DROPDOWN_OPTIONS,Title )
        self.helpers.wait_and_click_dropdown_option(LOC.L2_MANAGER_DROPDOWN,
                                                    LOC.L2_MANAGER_DROPDOWN_OPTIONS,
                                                    L2_manager)
        self.helpers.wait_and_click_dropdown_option(LOC.L3_MANAGER_DROPDOWN,
                                                    LOC.L3_MANAGER_DROPDOWN_OPTIONS,
                                                    L3_manager)
        self.helpers.send_keys(LOC.OFFICIAL_EMAIL_ID,official_email)
        self.helpers.send_keys(LOC.TOTAL_EXPERIENCE,Total_experience)
        self.helpers.wait_and_click_dropdown_option(LOC.LOCATIONS_DROPDOWN,
                                                    LOC.LOCATIONS_DROPDOWN_OPTIONS,
                                                    Location)
        time.sleep(2)
        self.helpers.click_radio_button(LOC.WORK_MODE_BUTTON,work_mode)
        time.sleep(2)
    def fill_education_details(self,Institution,Degree,Field,Year):
        self.helpers.send_keys(LOC.INSTITUTION, Institution)
        self.helpers.send_keys(LOC.DEGREE, Degree)
        self.helpers.send_keys(LOC.FIELD, Field)
        self.helpers.send_keys(LOC.YEAR, Year)

    def submit_details_and_verify_message(self):
        self.helpers.click(LOC.SUBMIT)
        return self.helpers.text(LOC.CONFIRMATION_MESSAGE)