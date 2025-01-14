# Selenium Login Automation Project

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project demonstrates automated testing of a simple login page using Selenium with Python. The tests cover the following scenarios:

1. **Open Login Page:** Verify that the login page loads correctly.
2. **Successful Login:** Test logging in with valid credentials.
3. **Failed Login:** Test logging in with invalid credentials.
4. **Empty Fields:** Test submitting the form with empty email and password fields.

The project is structured using the **Page Object Model (POM)** for better maintainability and scalability. It leverages **Pytest** for organizing and running tests, **WebDriverWait** for handling dynamic content, and **webdriver-manager** for managing browser drivers.

## Project Structure

```
project/
│
├── pages/
│   ├── __init__.py
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
├── screenshots/           # (Optional) Stores screenshots of failed tests
│
├── requirements.txt
│
└── login.html
```

### Descriptions:

- **`pages/`**: Contains Page Object Models.
  - **`__init__.py`**: Makes the directory a Python package.
  - **`login_page.py`**: Defines the `LoginPage` class with locators and methods to interact with the login page.

- **`tests/`**: Contains test cases using Pytest.
  - **`test_login.py`**: Defines test functions for different login scenarios.

- **`screenshots/`**: (Optional) Stores screenshots when tests fail for debugging purposes.

- **`requirements.txt`**: Lists all Python dependencies required for the project.

- **`login.html`**: The HTML file representing the login page to be tested.

## Prerequisites

- **Python 3.7+** installed on your machine. You can download it from [here](https://www.python.org/downloads/).
- **pip** (Python package installer) is available.
- **A web server** to serve `login.html`. This can be done using Python's built-in HTTP server or an editor extension like Live Server in VSCode.
- **Google Chrome** browser installed.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/selenium-login-automation.git
   cd selenium-login-automation
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**

   - **Windows:**

     ```bash
     .venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Tests

1. **Start a Local Web Server**

   Ensure that `login.html` is being served locally. You can use Python's built-in HTTP server:

   ```bash
   python -m http.server 5500
   ```

   This will serve the files at `http://127.0.0.1:5500/`.

2. **Run Pytest**

   Open a new terminal window/tab, activate your virtual environment if not already active, navigate to the project directory, and run:

   ```bash
   python -m pytest tests/test_login.py -v
   ```

   **Expected Output:**

   ```plaintext
   ============================= test session starts =============================
   platform win32 -- Python 3.12.0, pytest-8.3.4, pluggy-1.5.0 -- C:\Path\To\Your\Python.exe
   collected 4 items

   tests\test_login.py::test_open_login_page PASSED                        [ 25%]
   tests\test_login.py::test_successful_login PASSED                       [ 50%]
   tests\test_login.py::test_failed_login PASSED                           [ 75%]
   tests\test_login.py::test_empty_fields PASSED                           [100%]

   ============================== 4 passed in X.XXs ==============================
   ```

3. **Running Tests in Non-Headless Mode (Optional)**

   If you want to see the browser actions during testing, you can disable headless mode:

   - Open `tests/test_login.py`.
   - Modify the `driver` fixture by commenting out or removing the headless option:

     ```python
     chrome_options = Options()
     # chrome_options.add_argument("--headless")  # Comment out this line
     chrome_options.add_argument("--disable-gpu")
     chrome_options.add_argument("--window-size=1920,1080")
     ```

   - Save the file and rerun Pytest.

## Troubleshooting

### 1. `ModuleNotFoundError: No module named 'pages'`

**Cause:** Python cannot locate the `pages` package.

**Solution:**

- Ensure that the `pages` directory contains an `__init__.py` file.
- Make sure you're running Pytest from the project's root directory, not from within the `tests/` folder.

### 2. `pytest` Command Not Found

**Cause:** Pytest is not recognized as a command, possibly because the virtual environment is not activated or it's not installed correctly.

**Solution:**

- Ensure the virtual environment is activated.
- Install Pytest if not already installed.

### 3. Web Server Not Running or Incorrect URL

**Cause:** Selenium cannot connect to the specified URL because the web server is not running or the URL is incorrect.

**Solution:**

- Ensure that a local web server is running and serving `login.html`.
- Verify the URL in `test_login.py` matches the server's address and port.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

2. **Create a New Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**

4. **Commit Your Changes**

   ```bash
   git commit -m "Add feature XYZ"
   ```

5. **Push to Your Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

---

**Note:** Replace `https://github.com/yourusername/selenium-login-automation.git` with the actual repository URL if you are hosting the project on GitHub or another platform.

