import pytest
from selenium.webdriver import ActionChains
from locators.contract_employee_locators import ContractEmployeeFormLocators as LOC
from utils.helpers import Helpers


class NewContractEmployee:

    def __init__(self, driver):
        self.driver = driver
        self.helpers = Helpers(driver)

    def click_add_employee(self):
        element = self.helpers.wait_for_element(LOC.ADD_CONTRACTOR_BUTTON, condition="clickable")
        ActionChains(self.driver).move_to_element(element).pause(1).click().perform()
    def is_displayed(self):
        return self.helpers.wait_for_element(LOC.ADD_CONTRACTOR_FORM, condition="visible", timeout=10)





