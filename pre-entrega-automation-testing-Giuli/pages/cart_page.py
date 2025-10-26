from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    """Página del carrito de compras"""

    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")

    def listed_item_names(self):
        """Devuelve una lista con los nombres de los productos en el carrito"""
        items = self.wait_for_all_visible(self.CART_ITEMS)
        names = [i.find_element(*self.ITEM_NAME).text for i in items]
        return names