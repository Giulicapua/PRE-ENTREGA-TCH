from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10

class BasePage:
    """Clase base que contiene métodos comunes para todas las páginas"""

    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open(self, path: str = "/"):
        """Abre una URL completa combinando base_url y el path recibido"""
        url = self.base_url.rstrip("/") + path
        self.driver.get(url)
        return self

    def wait_for_url_contains(self, fragment: str):
        """Espera explícita hasta que la URL contenga el texto indicado"""
        self.wait.until(EC.url_contains(fragment))

    def wait_for_visible(self, locator):
        """Devuelve el elemento cuando es visible"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_all_visible(self, locator):
        """Devuelve una lista de elementos visibles"""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))