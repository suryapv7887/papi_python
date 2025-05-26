import calendar
import inspect
import logging
import os
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException,
    ElementNotInteractableException, StaleElementReferenceException)

class Helpers:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, locator, condition=None,timeout=20):
        if condition == "clickable":
            return self.wait.until(EC.element_to_be_clickable(locator))
        elif condition == "visible":
            return self.wait.until(EC.visibility_of_element_located(locator))
        elif condition == "present":
            return self.wait.until(EC.presence_of_element_located(locator))
        else:
            raise ValueError(f"Unsupported wait condition: {condition}")

    def click(self, locator):
        try:
            element = self.wait_for_element(locator, condition="clickable")
            element.click()
        except Exception as e:
            print(f"[ERROR] Failed to click on: {locator} | {e}")
            raise

    def send_keys(self, locator, text):
        try:
            element = self.wait_for_element(locator, condition="present")
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"[ERROR] Failed to send keys to: {locator} | {e}")
            raise

    def text(self, locator):
        try:
            element = self.wait_for_element(locator, condition="visible")
            return element.text
        except Exception as e:
            print(f"[ERROR] Failed to get text from: {locator} | {e}")
            raise

    def upload_file(self, locator, filepath):
        try:
            element = self.wait_for_element(locator, condition="present")
            element.send_keys(filepath)
        except Exception as e:
            print(f"[ERROR] Failed to upload file using: {locator} | {e}")
            raise

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

    def click_radio_button(self, locator_list, button_text):
        elements = self.driver.find_elements(*locator_list)
        for element in elements:
            if element.text.strip() == button_text.strip():
                self.driver.execute_script("arguments[0].click();", element)
                return
        raise Exception(f"Radio button with text '{button_text}' not found.")



