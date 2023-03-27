from page_objects.AdminMainPage import AdminMainPage
from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.ProductsPage import ProductsPage

PRODUCT_NAME = "Lenovo Think Pad 2.0"


def test_product_creation(browser):
    AdminLoginPage(browser).login_as_admin()
    AdminMainPage(browser).open_products_page()
    ProductsPage(browser).create_new_product(PRODUCT_NAME)


def test_product_deletion(browser):
    AdminLoginPage(browser).login_as_admin()
    AdminMainPage(browser).open_products_page()
    ProductsPage(browser).delete_product(PRODUCT_NAME)
