from playwright.sync_api import Page


class Courses:

    _COURSES_PAGE = "//a[@href='/student/courses']"

    def click_on_courses_page(self, page: Page):
        page.locator(self._COURSES_PAGE).click()

    def get_list_courses(self, page: Page):
        return page.locator(self._COURSES_PAGE).text_content()
