from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    """Página del inventario (catálogo de productos)"""

    TITLE = (By.CSS_SELECTOR, "span.title")
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    FIRST_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item .inventory_item_name")
    FIRST_ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item .inventory_item_price")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    FILTER_SELECT = (By.CSS_SELECTOR, "select.product_sort_container")
    CART_ICON = (By.ID, "shopping_cart_container")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    FIRST_ITEM_ADD_BTN = (By.CSS_SELECTOR, ".inventory_item button.btn")

    def title_text(self):
        """Obtiene el texto del título de la página"""
        return self.wait_for_visible(self.TITLE).text

    def products_present(self):
        """Verifica si hay al menos un producto visible"""
        items = self.wait_for_all_visible(self.INVENTORY_ITEMS)
        return len(items) > 0

    def first_product_info(self):
        """Devuelve el nombre y precio del primer producto"""
        name = self.wait_for_visible(self.FIRST_ITEM_NAME).text
        price = self.wait_for_visible(self.FIRST_ITEM_PRICE).text
        return name, price

    def add_first_product_to_cart(self):
        """Hace clic en el botón para agregar el primer producto al carrito"""
        self.wait_for_visible(self.FIRST_ITEM_ADD_BTN).click()

    def go_to_cart(self):
        """Abre la página del carrito de compras"""
        self.wait_for_visible(self.CART_ICON).click()