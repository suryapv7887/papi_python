import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import none_of
from selenium.webdriver.support.wait import WebDriverWait
from locators.contract_employee_locators import Contract_EmployeeFormLocators as LOC
from utils.helpers import Helpers


class NEW_CONTRACT_EMPLOYEE:

    def __init__(self, driver):
        self.driver = driver
        self.helpers = Helpers(driver)

    def click_add_employee(self):
        element = self.helpers.wait_for_element(LOC.ADD_CONTRACTOR_BUTTON, condition="clickable")
        ActionChains(self.driver).move_to_element(element).pause(1).click().perform()

    def is_displayed(self):
        return self.helpers.wait_for_element(LOC.ADD_CONTRACTOR_FORM, condition="visible", timeout=10)





