from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminMainPage(BasePage):
    MENU = (By.CSS_SELECTOR, "#menu")
    CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCT_MENU_ITEM = (By.XPATH, '//*[@id="collapse1"]/li[2]/a')
    CREATE_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")

    def open_products_page(self):
        catalog = self.element(self.CATALOG)
        catalog.click()
        product_item = catalog.find_element(*self.PRODUCT_MENU_ITEM)
        product_item.click()
