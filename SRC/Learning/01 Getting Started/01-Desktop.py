import flet
from flet import *

def main(page: Page):
#  'system', 'dark', 'light'
    page.theme_mode = 'dark'
    pass

flet.app(target=main)
# flet.app(target=main, port=5000, view=flet.WEB_BROWSER)