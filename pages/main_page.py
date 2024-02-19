from playwright.sync_api import Page
import config


class MainPage:
    _ENTER_BUTTON = "//button[@class='Sx2WI']//span[text()='войти']"

    def open_main_page(self, page: Page):
        page.goto(config.url.DOMAIN)

    def click_on_enter_button(self, page: Page):
        page.locator(self._ENTER_BUTTON).click()

