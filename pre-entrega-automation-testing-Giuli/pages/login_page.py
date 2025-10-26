from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    """Página de login de saucedemo"""

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    LOGO = (By.CLASS_NAME, "login_logo")

    def open_login(self):
        """Abre la página principal de login"""
        return self.open("/")

    def login(self, username: str, password: str):
        """Completa los campos de usuario y contraseña y hace clic en 'Login'"""
        self.wait_for_visible(self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()