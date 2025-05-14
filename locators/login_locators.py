from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    PROFILE_PAGE = (By.CSS_SELECTOR, "div[id='app-header'] span")
