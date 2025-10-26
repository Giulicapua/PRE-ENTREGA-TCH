import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.ui
@pytest.mark.smoke
def test_login_success(driver, base_url):
    """Prueba de login exitoso con usuario y contraseña válidos"""
    login = LoginPage(driver, base_url).open_login()
    login.login("standard_user", "secret_sauce")

    inv = InventoryPage(driver, base_url)
    inv.wait_for_url_contains("/inventory.html")
    assert "Swag Labs" in driver.title
    assert inv.title_text() == "Products"