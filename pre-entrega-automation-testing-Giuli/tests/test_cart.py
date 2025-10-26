import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.ui
def test_add_first_product_to_cart(driver, base_url):
    """Agrega el primer producto al carrito y valida que esté presente"""
    LoginPage(driver, base_url).open_login().login("standard_user", "secret_sauce")
    inv = InventoryPage(driver, base_url)
    inv.wait_for_url_contains("/inventory.html")

    inv.add_first_product_to_cart()

    # Verifica que el contador del carrito se actualice
    badge_text = None
    for _ in range(10):
        try:
            badge_text = inv.driver.find_element(*inv.CART_BADGE).text
            if badge_text:
                break
        except Exception:
            pass

    assert badge_text == "1", f"Se esperaba badge '1' y fue {badge_text!r}"

    inv.go_to_cart()
    cart = CartPage(driver, base_url)
    cart_items = cart.listed_item_names()
    assert len(cart_items) >= 1, "Se esperaba ver al menos 1 ítem en el carrito"