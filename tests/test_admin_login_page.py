from page_objects.AdminLoginPage import AdminLoginPage


def test_admin_login_page(browser):
    AdminLoginPage(browser).check_elements_on_page()
