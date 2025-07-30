import pytest
from selenium import webdriver

from utilities import ConfigReaderUtil


@pytest.fixture()
def setup_teardown(request):
    # driver = webdriver.Edge()
    browser = ConfigReaderUtil.readingConfiguration("basic info", "browser")
    app_url = ConfigReaderUtil.readingConfiguration("basic info", "url")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        print("The required browser is not available")
    driver.maximize_window()
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()