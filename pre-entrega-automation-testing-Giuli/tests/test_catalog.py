import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.ui
def test_catalog_title_and_presence(driver, base_url):
    """Verifica título, presencia de productos y datos del primer producto"""
    LoginPage(driver, base_url).open_login().login("standard_user", "secret_sauce")
    inv = InventoryPage(driver, base_url)
    inv.wait_for_url_contains("/inventory.html")

    assert inv.title_text() == "Products"
    assert inv.products_present(), "Se esperaba al menos 1 producto visible"
    name, price = inv.first_product_info()
    assert name and price