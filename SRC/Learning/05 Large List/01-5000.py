import flet as ft
from flet import *
from flet import dropdown

def main(page: Page):
    page.theme_mode = 'dark'
    page.title = 'Document'
    page.window_height = 500
    page.window_width = 500    

    for i in range(5000):
        page.controls.append(Text(f'Line {i}'))
    
    page.scroll = "always"
    page.update()

ft.app(target=main, assets_dir='assets')
# ft.app(target=main, assets_dir='assets', port=5000, view=ft.WEB_BROWSER)