from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "[name='search']")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart")
    NAVIGATION_BAR = (By.CSS_SELECTOR, "ul.nav.navbar-nav")
    CONTENT_DIV = (By.CSS_SELECTOR, "#content")
    PARTNERS_CAROUSEL = (By.CSS_SELECTOR, "#carousel0")
    EMPTY_SHOPPING_CARD_LABEL = (By.CSS_SELECTOR, "p.text-center")

    FEATURED_PRODUCT = (By.CSS_SELECTOR, "#content > div.row .product-layout")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")

    def click_featured_product(self, index):
        featured_product = self.elements(self.FEATURED_PRODUCT)[index]
        product_name = featured_product.find_element(*self.PRODUCT_NAME).text
        featured_product.click()
        return product_name