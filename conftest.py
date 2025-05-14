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

def pytest_addoption(parser):
    parser.addoption("--browser", default=Config.DEFAULT_BROWSER)
    parser.addoption("--env", default=Config.DEFAULT_ENV)

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser").lower()

@pytest.fixture(scope="session")
def base_url(request):
    env = request.config.getoption("--env").lower()
    return Config.get_base_url(env)

@pytest.fixture
def setup(browser, base_url):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()

@pytest.fixture
def login_user(setup):
    login_page = LoginPage(setup)
    login_page.login("dev@simelabs.in", "1~5An)4VlQrl")
    assert "Employee Profile" in login_page.profile_title()
    return setup
