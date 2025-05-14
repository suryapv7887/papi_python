from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators as LOC
from utils.helpers import Helpers

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.helpers = Helpers(driver)

    def enter_username(self, username):
        self.helpers.send_keys(LOC.USERNAME,username)
    def enter_password(self, password):
        self.helpers.send_keys(LOC.PASSWORD, password)
    def click_login_button(self):
        self.helpers.click(LOC.SUBMIT_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def profile_title(self):
        return self.helpers.text(LOC.PROFILE_PAGE)

