import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import os
import tempfile
from tests import config


def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="https://2019.hep1undergrad.apply.ucasenvironments.com/",
                     help="base url for the application under test")
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="the name of the browser you want to test with")
    parser.addoption("--host",
                     action="store",
                     default="localhost",
                     help="local host or browserstack")
    parser.addoption("--browserversion",
                     action="store",
                     default="53.0",
                     help="the version of the browser you want to test with")
    parser.addoption("--os",
                     action="store",
                     default="Windows",
                     help="the OS you want to test with")
    parser.addoption("--osversion",
                     action="store",
                     default="10",
                     help="the OS version you want to test with")
    parser.addoption("--resolution",
                     action="store",
                     default="1600x1200",
                     help="the screen resolution you want to test with")

@pytest.fixture
def firefox_options(request, firefox_options):
    args = request.node.get_marker('firefox_arguments')
    if args is not None:
        for arg in args.args:
            firefox_options.add_argument(arg)
    #self.download_dir = tempfile.mkdtemp()
    #firefox_options.add_argument('-foreground')
    #firefox_options.add_argument("browser.download.dir", self.download_dir)
    #firefox_options.add_argument("browser.download.folderList", 2)
    #firefox_options.add_argument("browser.helperApps.neverAsk.saveToDisk",
     #       "images/jpeg, application/pdf, application/octet-stream")
    #firefox_options.add_argument("pdfjs.disabled", True)
    return firefox_options


@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption("--baseurl")
    config.browser = request.config.getoption("--browser").lower()
    config.host = request.config.getoption("--host").lower()
    config.browserversion = request.config.getoption("--browserversion").lower()
    config.os = request.config.getoption("--os").lower()
    config.osversion = request.config.getoption("--osversion")
    config.resolution = request.config.getoption("--resolution")

    try:
        if config.host == "browserstack":
            _desired_caps = {}
            _desired_caps["browser"] = config.browser
            _desired_caps["browser_version"] = config.browserversion
            _desired_caps["os"] = config.os
            _desired_caps["os_version"] = config.osversion
            _desired_caps["resolution"] = config.resolution
            _desired_caps["project"] = "Selenium Playground"
            _desired_caps["name"] = request.cls.__name__ + "." + request.function.__name__
            _url = "http://chrisharris20:wptzYxQAL2ZsLYtCuzaq@hub.browserstack.com:80/wd/hub"
            driver_ = webdriver.Remote(_url, _desired_caps)
        elif config.host == "localhost":
            if config.browser == "firefox":
                #_geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver.exe')
                driver_ = webdriver.Firefox()
            elif config.browser == "chrome":
                #_chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')
                driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return driver_
    except WebDriverException as e:
            if "executable needs to be in PATH" in str(e):
                print("I cant find your driver, do is need to be in your path or is the specified path okay?")
            elif "Expected browser binary location" in str(e):
                print("Problem with expected binary localtion")

