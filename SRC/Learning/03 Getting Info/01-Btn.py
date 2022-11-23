import flet as ft
from flet import *

def main(page: Page):
    page.theme_mode = 'dark'
    page.title = 'Document'
    page.window_height = 500
    page.window_width = 500

    btn_accion = ElevatedButton('Click me')
    
    page.add(btn_accion)

ft.app(target=main, assets_dir='assets')
# ft.app(target=main, assets_dir='assets', port=5000, view=ft.WEB_BROWSER)