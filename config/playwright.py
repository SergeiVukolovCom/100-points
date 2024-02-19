import os


class Playwright:
    PAGE_VIEWPORT_SIZE = {'width': 1920, 'height': 1080}
    BROWSER = os.getenv('BROWSER', default='chrome')
    IS_HEADLESS = os.getenv('HEADLESS', default=False)
    SLOW_MO = int(os.getenv('SLOW_MO', default=50))
    LOCALE = 'ru-RU'