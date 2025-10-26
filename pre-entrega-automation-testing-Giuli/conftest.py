import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Carpeta donde se guardarán reportes y capturas
REPORTS_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

def _new_chrome(headless: bool = True):
    """Crea una nueva instancia de Chrome WebDriver"""
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")  # modo sin interfaz
    opts.add_argument("--window-size=1280,1000")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(0)  # usamos esperas explícitas
    return driver

def pytest_addoption(parser):
    """Agrega opciones personalizadas para pytest"""
    parser.addoption("--headed", action="store_true", help="Ejecutar con navegador visible")
    parser.addoption("--base_url", action="store", default="https://www.saucedemo.com")

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    """Devuelve la URL base del sitio bajo prueba"""
    return pytestconfig.getoption("--base_url")

@pytest.fixture
def driver(pytestconfig):
    """Inicializa y finaliza el navegador para cada test"""
    headed = pytestconfig.getoption("--headed")
    driver = _new_chrome(headless=not headed)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook que captura pantalla y HTML cuando un test falla.
    Las capturas se guardan en la carpeta 'reports'.
    """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver is not None:
            ts = time.strftime("%Y%m%d-%H%M%S")
            test_name = item.name.replace("/", "_")
            png_path = os.path.join(REPORTS_DIR, f"{test_name}_{ts}.png")
            html_path = os.path.join(REPORTS_DIR, f"{test_name}_{ts}.html")
            try:
                driver.save_screenshot(png_path)
            except Exception:
                pass
            try:
                with open(html_path, "w", encoding="utf-8") as f:
                    f.write(driver.page_source)
            except Exception:
                pass
            if hasattr(rep, "extras"):
                from pytest_html import extras
                if os.path.exists(png_path):
                    rep.extras.append(extras.image(png_path))
                if os.path.exists(html_path):
                    rep.extras.append(extras.html(f'<a href="{html_path}">{html_path}</a>'))