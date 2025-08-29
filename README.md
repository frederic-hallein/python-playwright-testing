# Python Playwright Testing

## Description
Automated end-to-end testing framework for web applications using Python and Playwright. This project organizes tests with pytest, supports YAML-based configuration, provides page object models for scalable test development, and uses pylint to lint the files.

**Website under test:** [https://www.saucedemo.com/](https://www.saucedemo.com/)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/frederic-hallein/python-playwright-testing.git
   cd python-playwright-testing
   ```

2. **Create virtual environment:**
    ```sh
    python3 -m venv .venv
    ```

3. **Install Python dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Install Playwright browsers:**
    ```sh
    playwright install
    ```

## Usage
- To run all tests:
    ```sh
    pytest
    ```

- To run specific tests:
    ```sh
    pytest tests/test_<page>
    ```

- To enable output capturing, add the ```-s``` flag to previous commands


**Note:** Before running the tests, the program will randomly select a user to log in. The test website may behave differently depending on the logged-in user, which can affect the test results. The possible cases are as follows:
  - **standard_user:** the user experiences no problems or errors
  - **problem_user:** a user experiences problems
  - **performance_glitch_user:** the user experiences performance issues
  - **error_user:** a user experiences errors
  - **visual_user:** the user experiences visual bugs



## Roadmap
- Add additional page object models
- Integrate CI/CD pipelines
- Expand test coverage and scenarios
- Implement test reporting and analytics
- Support for more browsers and devices

## Project Status

**Not currently in active development.** Core functionality implemented. Additional features are planned but not actively worked on.