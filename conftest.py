import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from configurations.config import Config
from pages.login_page import LoginPage
import allure
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from datetime import datetime
from pytest_html import extras as html_extras

def pytest_addoption(parser):
    parser.addoption("--browser", default=Config.DEFAULT_BROWSER)
    parser.addoption("--env", default=Config.DEFAULT_ENV)
    parser.addoption("--headless",action="store_true",
                    default=Config.DEFAULT_HEADLESS)

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser").lower()

@pytest.fixture(scope="session")
def base_url(request):
    env = request.config.getoption("--env").lower()
    return Config.get_base_url(env)

@pytest.fixture(scope="class")
def setup(browser, base_url, request):
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version="136.0.7103.114").install()),options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
    elif browser == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def login_user(setup):
    login_page = LoginPage(setup)
    login_page.login(Config.LOGIN_USERNAME,Config.LOGIN_PASSWORD)
    return setup

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")  # Replace 'setup' if your fixture has another name
        if driver:
            try:
                xfail = hasattr(report, "wasxfail")
                if (report.skipped and xfail) or (report.failed and not xfail):
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    screenshot_name = f"{item.name}_{timestamp}.png"
                    screenshot_dir = os.path.join(os.getcwd(), "screenshots")
                    os.makedirs(screenshot_dir, exist_ok=True)

                    screenshot_path = os.path.join(screenshot_dir, screenshot_name)
                    driver.save_screenshot(screenshot_path)

                    # Allure attachment
                    with open(screenshot_path, "rb") as image_file:
                        allure.attach(
                            image_file.read(),
                            name=f"Failure_Screenshot_{item.name}_{timestamp}",
                            attachment_type=allure.attachment_type.PNG
                        )

                    # pytest-html Report
                    # extras = getattr(report, "extras", [])
                    # extras.append(html_extras.image(screenshot_path))
                    # extras.append(html_extras.html("<div style='color:red;'>Test Failed - Screenshot Attached</div>"))
                    # report.extras = extras

            except Exception as e:
                print(f"[ERROR] Screenshot capture failed: {e}")


# def pytest_html_report_title(report):
#     report.title = "PAPI - Selenium Python Test"





