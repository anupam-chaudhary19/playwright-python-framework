from pages.base_page import BasePage
class LoginPage(BasePage):

    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"
    products_title = "//span[text()='Products']"

    def login(self, username, password):
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.click_element(self.login_button)

    def verify_login_successful(self):
        return self.get_text(self.products_title)
