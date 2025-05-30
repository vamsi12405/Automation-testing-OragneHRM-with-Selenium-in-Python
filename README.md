# Automation-testing-OragneHRM-with-Selenium-in-Python

## Overview

This repository contains automated test scripts for the [OrangeHRM](https://opensource-demo.orangehrmlive.com/) web application using Python, Selenium WebDriver, and pytest.  
The goal is to validate core functionalities of OrangeHRM through maintainable, scalable, and readable test automation code following the Page Object Model (POM) design pattern.

- **tests/**: All test cases, organized by feature.
- **pages/**: Page Object Model classes for each OrangeHRM page.

- ## Getting Started

### Prerequisites

- Python 3.x
- Chrome browser (or modify for Firefox/Edge)
- ChromeDriver (or use webdriver-manager)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/OrangeHRM-Automation.git
   cd OrangeHRM-Automation
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

### Running Tests

To execute all tests:

```sh
pytest
```
To generate an HTML report:
```sh
pytest --html=reports/report.html
