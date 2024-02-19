from playwright.sync_api import Page

from config import playwright
from config.base_authorization import BaseAuthorization

class RegistrationPage:
    _HELLO = ".m3TEN"
    _EMAIL = "input[type='email']"
    _PASS = "input[type='password']"
    _CONTINUE_BUTTON = "//div[contains(text(),'Продолжить')]"

    def __init__(self, base_authorization: BaseAuthorization):
        self.base_authorization = base_authorization

    def find_hello_on_registration_page(self, page: Page):
        return page.locator(self._HELLO).text_content()

    def enter_credentials(self, page: Page):
        page.locator(self._EMAIL).type(self.base_authorization.role_authorization("student", "login_student"))
        page.locator(self._PASS).type(self.base_authorization.role_authorization("student", "password_student"))

    def click_continue_button(self, page: Page):
        page.wait_for_selector(self._CONTINUE_BUTTON)
        page.locator(self._CONTINUE_BUTTON).click()

