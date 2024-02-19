from config.expectations import Expectations
from config.url import Url
from config.playwright import Playwright
from config.base_authorization import BaseAuthorization
from config.read_credentials import Credentials

url = Url()
expectations = Expectations()
playwright = Playwright()
read_credentials = Credentials()
authorization = BaseAuthorization(read_credentials)