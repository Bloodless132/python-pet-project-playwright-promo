# My pet project to practice UI and API testing
My personal pet project to practice different skills for Strong Middle AQA engineer.

## About the project

This is a Python test automation pet project built to practice a scalable automation framework approach for both UI and API testing.

The project includes:

- Playwright UI tests with Page Object Model
- API tests implemented in two ways: Playwright API and Python `requests`
- reusable API clients, helpers, fixtures and test data
- Allure reporting
- Playwright traces and screenshots for failed UI tests
- Docker support for local isolated test execution
- GitHub Actions CI for automated API and UI test runs


## Pytest tests execution
- Run ALL UI + API tests: `pytest tests`
- Run only UI tests: `pytest tests/ui`
- Run all API tests: `pytest tests/api`
- Run only Playwright API tests: `pytest tests/api/playwright`
- Run only Python requests API tests: `pytest tests/api/requests`

Test result files generation command line parameters:
- Allure results: `--alluredir=allure-results`
- Playwright traces for failed tests (applicable ONLY for UI tests): `--tracing=retain-on-failure --output=test-results`

Example to run ALL tests with Allure-results and PlayWright traces: `pytest tests
--alluredir=allure-results 
--tracing=retain-on-failure 
--output=test-results`

Test result files preview/execution:
- View Allure results: `allure serve <path to allure-results folder>`
- View PlayWright traces: `playwright show-trace <path to trace .zip file>`

## Docker tests execution
- Run all tests: `docker run --rm
  -v "$PWD:/app"
  playwright-tests`
- Run API tests with Allure-results: `docker run --rm
  -v "$PWD:/app"
  playwright-tests
  pytest tests/api
  --alluredir=allure-results`
- Run UI tests with Allure-results and Playwright traces: `docker run --rm
  -v "$PWD:/app"
  playwright-tests
  pytest tests/ui
  --alluredir=allure-results
  --tracing=retain-on-failure
  --output=test-results`
## GitHub tests execution
The project has separate GitHub Actions workflows for API and UI tests.

The workflows are triggered:
- manually through workflow_dispatch
- when a Pull Request targeting main is created or updated
- after changes are merged/pushed to main
