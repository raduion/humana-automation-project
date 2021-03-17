# Humana Automation

## Setup (with Homebrew)

On a MacBook, with [Homebrew](https://brew.sh) installed,
perform these steps:

```sh
# 1. clone project repository with GitHub CLI [cli.github.com]
$ gh repo clone https://github.com/raduion/humana-automation-project.git
# 2. change to project root
$ cd automation-template
# 3. create a virtual environment for the project [docs.python.org/3/library/venv.html]
$ python3 -m venv venv
# 4. activate virtual environment
$ source venv/bin/activate
# 5. install project requirements with Pip [pip.pypa.io/en/stable/user_guide/#requirements-files]
(venv) $ pip install -r requirements.txt
# 6. install Google ChromeDriver with Homebrew [formulae.brew.sh/cask/chromedriver]
(venv) $ brew install --cask chromedriver
# 7. allow ChromeDriver out of the Mac OS untrusted quarantine [stackoverflow.com/questions/60362018/]
(venv) $ xattr -d com.apple.quarantine /usr/local/bin/chromedriver
# 8. check ChromeDriver version, confirm it is installed (current version: 86.0.4240.22)
(venv) $ chromedriver -v
# 9. install Mozilla GeckoDriver with Homebrew [formulae.brew.sh/formula/geckodriver]
(venv) $ brew install geckodriver
# 10. check GeckoDriver version, confirm it is installed (current version: 0.27.0)
(venv) $ geckodriver -V
# 11. allow local SafariDriver connections on your machine [developer.apple.com/documentation/webkit/]
(venv) $ sudo safaridriver --enable
# 12. check SafariDriver version, confirm it is installed (current version: 15610.1.28.1.9)
(venv) $ safaridriver --version
```

## Running Tests

Use the [pytest](https://docs.pytest.org) test runner, within an active virtual environment, to run tests. 

Stop test runs by pressing: **Control-C**

### All Tests in the Project

```sh
# from project root directory
(venv) $ pytest 
```

### Multiple Tests in a Module

```sh
# give a relative file path to the Python module containing the tests
(venv) $ pytest tests/database_tests/test_template_automation.py
```

### Multiple Tests with a Keyword

```sh
# give a unique keyword contained in the file name or test name
(venv) $ pytest -k template
```

### Single Test 

```sh
# use :: to separate the file path from the test name
(venv) $ tests/database_tests/test_template_automation.py::test_example
```

## Choosing A Browser

The browser used for running the tests can be specified on the command line
with the `--browser` or `--wb` (web browser) option. Browser names can also be
shortened to two letters:

```sh
$ pytest --browser chrome   # run tests using Google Chrome
$ pytest --browser firefox  # run tests using Mozilla Firefox
$ pytest --browser safari   # run tests using Apple Safari

# shorthand names: ch, ff, sf
$ pytest --wb ch tests/reports/test_sleep_score_and_rating.py
$ pytest --wb ff tests/facebook_auth/
$ pytest --wb sf -k default_qs
```

The browser can be configured in `tests/config.json` too:

```sh
{
  "browser": "chrome",  # change this value to: chrome, firefox, safari
  "wait_time": 30
}
```
# humana-automation-project
