import base64

from playwright.sync_api import Page
from config.read_credentials import Credentials


class BaseAuthorization:
    def __init__(self, read_credentials: Credentials):
        self.read_credentials = read_credentials

    def set_basic_auth_headers(self, page: Page, role: str):
        credentials = self.read_credentials.get_credentials()

        if role in credentials:
            username = credentials[role]['login']
            password = credentials[role]['password']
            base64_credentials = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")
            headers = {"Authorization": f"Basic {base64_credentials}"}
            page.set_extra_http_headers(headers)

        else:
            raise ValueError(f"Роль '{role}' не найдена в файле credentials.json")

    def role_authorization(self, role: str, field: str):
        credentials = self.read_credentials.get_credentials()
        if role in credentials:
            return credentials[role][field]
