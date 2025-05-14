import calendar
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Helpers:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, locator, condition=None,timeout=10):
        if condition == "clickable":
            return self.wait.until(EC.element_to_be_clickable(locator))
        elif condition == "visible":
            return self.wait.until(EC.visibility_of_element_located(locator))
        elif condition == "present":
            return self.wait.until(EC.presence_of_element_located(locator))
        else:
            raise ValueError(f"Unsupported wait condition: {condition}")

    def send_keys(self, locator, text):
        element = self.wait_for_element(locator, condition="visible")
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        element = self.wait_for_element(locator, condition="clickable")
        element.click()

    def text(self, locator):
        element = self.wait_for_element(locator, condition="visible")
        return element.text

    def upload_file(self,locator,filepath):
        element=self.wait_for_element(locator,condition="present")
        element.send_keys(filepath)

    def wait_and_click_dropdown_option(self, dropdown_locator, option_locator, option_text):
        try:

            dropdown = self.wait_for_element(dropdown_locator, "clickable")
            dropdown.click()
            time.sleep(1)

            options = self.wait.until(EC.presence_of_all_elements_located(option_locator))

            for option in options:
                if option.text.strip().lower() == option_text.strip().lower():
                    option.click()
                    print(f"Clicked option: {option_text}")
                    return True

            print(f" Option not found: {option_text}")
            return False

        except Exception as e:
            print(f" Exception while selecting dropdown option '{option_text}': {e}")
            return False





