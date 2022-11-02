import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Select the language in which the website will be displayed.")
    parser.addoption('--browser', action='store', default="chrome",
                     help="Select the language in which the website will be displayed.")


@pytest.fixture(scope="session")
def browser_language(request):
    return request.config.getoption("language")


@pytest.fixture(scope="function")
def browser(request, browser_language):
    browser_name = request.config.getoption("browser")
    browser = None
    if browser_name == "chrome":
        from selenium.webdriver.chrome.options import Options
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.set_preference('intl.accept_languages', browser_language)
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
