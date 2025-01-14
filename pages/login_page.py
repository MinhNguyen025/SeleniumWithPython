# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Page Object cho trang Login."""

    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.ID, "error-message")

    def open(self, url):
        """Mở trang đăng nhập."""
        self.driver.get(url)

    def set_email(self, email):
        """Nhập email."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_input)
        ).send_keys(email)

    def set_password(self, password):
        """Nhập mật khẩu."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(password)

    def click_login(self):
        """Nhấn nút đăng nhập."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def get_error_message(self):
        """Lấy thông báo lỗi."""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
        ).text

    def is_error_displayed(self):
        """Kiểm tra xem thông báo lỗi có hiển thị không."""
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.error_message)
            ).is_displayed()
        except:
            return False
