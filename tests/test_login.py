# tests/test_login.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.fixture(scope="module")
def driver():
    """Khởi tạo WebDriver sử dụng headless Chrome."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Chạy ở chế độ không giao diện
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    """Fixture tạo đối tượng Page Object."""
    return LoginPage(driver)

URL = "http://127.0.0.1:5500/login.html"

def test_open_login_page(driver, login_page):
    """Test mở trang đăng nhập."""
    login_page.open(URL)
    assert driver.title == "Login Page", "Test Failed: Không thể mở trang Login"
    print("Test Case 1: Mở trang đăng nhập - Passed")

def test_successful_login(login_page, driver):
    """Test đăng nhập thành công."""
    login_page.open(URL)
    login_page.set_email("test@example.com")
    login_page.set_password("password123")
    login_page.click_login()
    
    # Kiểm tra URL chuyển hướng
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard.html"))
    assert "dashboard.html" in driver.current_url, "Test Failed: Không chuyển hướng đến Dashboard"
    print("Test Case 2: Đăng nhập thành công - Passed")

def test_failed_login(login_page):
    """Test đăng nhập sai thông tin."""
    login_page.open(URL)
    login_page.set_email("wrong@example.com")
    login_page.set_password("wrongpassword")
    login_page.click_login()
    
    # Kiểm tra thông báo lỗi
    assert login_page.is_error_displayed(), "Test Failed: Thông báo lỗi không hiển thị"
    assert login_page.get_error_message() == "Nhập email và mật khẩu sai.", "Test Failed: Thông báo lỗi sai"
    print("Test Case 3: Đăng nhập thất bại - Passed")

def test_empty_fields(login_page):
    """Test để trống trường Email và Password."""
    login_page.open(URL)
    # Không nhập gì
    login_page.click_login()
    
    # Kiểm tra thông báo lỗi
    assert login_page.is_error_displayed(), "Test Failed: Thông báo lỗi không hiển thị khi để trống"
    assert login_page.get_error_message() == "Vui lòng nhập email và mật khẩu.", "Test Failed: Thông báo lỗi sai khi để trống"
    print("Test Case 4: Để trống các trường - Passed")

# Hook để chụp screenshot khi test thất bại
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook để chụp screenshot khi test thất bại."""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            # Đảm bảo thư mục screenshots tồn tại
            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')
            # Chụp screenshot
            driver.save_screenshot(f"screenshots/{item.name}.png")
