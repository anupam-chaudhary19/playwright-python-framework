from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.products_page import ProductsPage
from utils.config import Config
from utils.globalvariable import GlobalVar

def test_products(page):
    # Login first
    login_page = LoginPage(page)
    login_page.navigate_to(Config.BASE_URL)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    # Now on products page
    products_page = ProductsPage(page)

    assert products_page.verify_product1() == GlobalVar.product1
    assert products_page.verify_product2() == GlobalVar.product2
    assert products_page.verify_product3() == GlobalVar.product3