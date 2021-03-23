import os
import json

import pytest
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options

CONFIG_PATH = os.path.dirname(os.path.realpath(__file__)) + '/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox', 'safari']
DEFAULT_BROWSER = 'chrome'


# define a command-line option to choose a browser configuration:
# $ pytest --wb ff
def pytest_addoption(parser):
    parser.addoption(
        '--wb',
        '--browser',
        help='chrome (ch), firefox (ff), safari (sf)'
    )
    parser.addoption("--headless", action="store_true", help="Use a headless browser")


@pytest.fixture
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)

    return data


@pytest.fixture
def config_browser(request, config):
    option = request.config.getoption('--browser')

    # Validate and return the browser choice from the given configuration
    if option is not None:
        shorthand = {'ch': 'chrome', 'ff': 'firefox', 'sf': 'safari'}
        return option if option not in shorthand else shorthand[option]
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    elif 'browser' in config:
        return config['browser']
    else:
        return DEFAULT_BROWSER


@pytest.fixture
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def file_url():
    def _file_url(path):
        return 'file://' + os.getcwd() + '/' + path

    return _file_url


@pytest.fixture
def report_path():
    path = 'tests/reports/sleep-report.html'

    yield path

    os.remove(path)


@pytest.fixture
def browser(request, config_browser, config_wait_time):
    ''' Initialize WebDriver for the chosen browser '''
    project_path = os.path.dirname(os.path.realpath(__file__)) + \
                   os.sep + '..' + os.sep

    if config_browser == 'chrome':
        # chrome driver path setup to include Windows machines
        if os.path.exists('/usr/local/bin/chromedriver'):
            driver_path = '/usr/local/bin/chromedriver'
        else:
            driver_path = '{}/webdrivers/chromedriver'.format(project_path) + \
                          ('.exe' if os.name == 'nt' else '')

        options = Options()
        options.add_argument("--no-sandbox")
        # options.add_argument("--incognito")
        # options.add_argument('--disable-web-security')
        # options.add_argument('--allow-running-insecure-content')
        # options.accept_untrusted_certs = True
        # options.assume_untrusted_cert_issuer = True
        options.headless = request.config.getoption('--headless')

        browser = webdriver.Chrome(
            executable_path=driver_path,
            options=options,
            seleniumwire_options={'verify_ssl': False}
        )
        # browser.delete_all_cookies()
        browser.maximize_window()
    elif config_browser == 'firefox':
        if os.path.exists('/usr/local/bin/geckodriver'):
            driver_path = '/usr/local/bin/geckodriver'
        else:
            driver_path = '{}/webdrivers/geckodriver'.format(project_path)

        browser = webdriver.Firefox(executable_path=driver_path)
    elif config_browser == 'safari':
        browser = webdriver.Safari(seleniumwire_options={'port': 0})
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    browser.implicitly_wait(config_wait_time)

    # Return the driver object at the end of setup
    yield browser

    # For clean-up, quit the driver
    browser.quit()
