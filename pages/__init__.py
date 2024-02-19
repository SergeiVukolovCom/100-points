from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.courses_page import Courses
from config.base_authorization import BaseAuthorization
from config.read_credentials import Credentials

read_credentials = Credentials()
main_page = MainPage()
courses_page = Courses()
base_authorization = BaseAuthorization(read_credentials)
registration_page = RegistrationPage(base_authorization)