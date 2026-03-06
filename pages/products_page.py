from pages.base_page import BasePage
from utils.globalvariable import GlobalVar


class ProductsPage(BasePage):

    products_title = GlobalVar.products_xpath
    product1 = GlobalVar.product1_xpath
    product2 = GlobalVar.product2_xpath
    product3 = GlobalVar.product3_xpath

    def verify_product1(self):
        return self.get_text(self.product1)

    def verify_product2(self):
        return self.get_text(self.product2)

    def verify_product3(self):
        return self.get_text(self.product3)