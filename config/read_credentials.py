import json


class Credentials:

    def __init__(self, filename='credentials.json'):
        self.filename = filename
        self.credentials = []
        self.load_credentials()

    def load_credentials(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.credentials = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

    def get_credentials(self):
        return self.credentials
