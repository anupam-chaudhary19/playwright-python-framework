from pages.login_page import LoginPage
from utils.config import Config
from utils.globalvariable import GlobalVar

def test_login(page):
    login_page = LoginPage(page)
    login_page.navigate_to(Config.BASE_URL)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    assert login_page.verify_login_successful() == GlobalVar.products_text