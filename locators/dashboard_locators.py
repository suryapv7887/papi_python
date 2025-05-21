from selenium.webdriver.common.by import By

class DashboardLocators:
    PEOPLE_ICON = (By.XPATH, "//a[@href='/peoples']/..")
    PEOPLE_MENU_OPTIONS=(By.XPATH,"//div[@class='dropdown-menu'][1]//a")
    REGULAR_EMPLOYEES_OPTION = (By.XPATH, "//a[@href='/peoples']/../following::a[1]")
    CONTRACT_EMPLOYEES_OPTION = (By.XPATH, "//a[@href='/peoples']/../following::a[2]")
    SELECTED_PEOPLE_HEADER = (By.XPATH, "//div[@id='app-header']")

