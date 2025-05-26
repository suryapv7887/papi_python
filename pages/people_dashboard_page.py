from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.dashboard_locators import DashboardLocators as LOC
from utils.helpers import Helpers

class DashboardPage:
    def __init__(self, driver,logger):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.helpers = Helpers(driver)
        self.logger=logger
    def click_regular_employees(self):
        #self.helpers.click(LOC.PEOPLE_ICON)
        self.logger.info("Clicking on Regular Employees from dropdown")
        return self.helpers.wait_and_click_dropdown_option(
            dropdown_locator=LOC.PEOPLE_ICON,
            option_locator=LOC.PEOPLE_MENU_OPTIONS,
            option_text="Regular Employees" )

    def click_contract_employees(self):
        #self.helpers.click(LOC.PEOPLE_ICON)
        self.logger.info("Clicking on Contract Employees from dropdown")
        return self.helpers.wait_and_click_dropdown_option(
            dropdown_locator=LOC.PEOPLE_ICON,
            option_locator=LOC.PEOPLE_MENU_OPTIONS,
            option_text="Contract Employees")

    def get_header_text(self):
        self.logger.info("Getting header text")
        header = self.helpers.wait_for_element(LOC.SELECTED_PEOPLE_HEADER, condition="present")
        return header.text
