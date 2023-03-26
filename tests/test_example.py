from page_objects.MainPage import MainPage

def test_add_to_wish_list(browser):
    product_name = MainPage(browser).click_featured_product(0)