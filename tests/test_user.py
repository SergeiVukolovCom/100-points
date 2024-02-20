import config.base_authorization
import pages.main_page
import pages.registration_page
import pages.courses_page


class Test:

    def test_to_make_actions(self, page):
        config.authorization.set_basic_auth_headers(page, role='admin')
        pages.main_page.open_main_page(page)
        pages.main_page.click_on_enter_button(page)
        assert pages.registration_page.find_hello_on_registration_page(
            page) == "Привет!", "You aren't on Registration page"
        pages.registration_page.enter_credentials(page)
        pages.registration_page.click_continue_button(page)
        pages.courses_page.click_on_courses_page(page)
        pages.courses_page.get_list_courses(page)



