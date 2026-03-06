# Playwright Python Automation Framework

This project is a UI automation framework built using **Playwright with Python**, **Pytest**, and the **Page Object Model (POM)** design pattern.

The framework is designed for scalable and maintainable test automation.

---

## Tech Stack

* Python
* Playwright
* Pytest
* Page Object Model (POM)
* Allure Reports
* Pytest HTML Reports

---

## Project Structure

```
playwright_framework
│
├── pages
│   ├── base_page.py
│   └── login_page.py
│
├── tests
│   └── test_login.py
│
├── utils
│   └── config.py
│
├── reports
├── screenshots
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone <repository-url>
```

Move into the project directory:

```
cd playwright_framework
```

Install dependencies:

```
pip install -r requirements.txt
```

Install Playwright browsers:

```
playwright install
```

---

## Running Tests

Run all tests:

```
pytest
```

Run a specific test file:

```
pytest tests/test_login.py
```

Run tests in parallel:

```
pytest -n 4
```

---

## Generate HTML Report

```
pytest --html=reports/report.html --self-contained-html
```

---

## Generate Allure Report

Run tests:

```
pytest --alluredir=allure-results
```

Generate and open report:

```
allure serve allure-results
```

---

## Features

* Page Object Model design pattern
* Parallel test execution
* HTML test reports
* Allure reporting
* Screenshot capture on failure
* Scalable project structure

---

## Author

Automation Framework developed using **Playwright + Python** for UI testing.
