import flet as ft
from flet import *
from flet import dropdown, alignment, border, border_radius

def main(page: Page):
    page.theme_mode = 'dark'
    page.title = 'Document'
    page.window_height = 500
    page.window_width = 500

    lvTextos = ListView(expand=1, spacing=10, item_extent=50)
    page.add(lvTextos)

    for i in range(5101):
        lvTextos.controls.append(Text(f'Line {i}'))

        if i % 500 == 0:
            page.update()
    page.update()
    
ft.app(target=main, assets_dir='assets')
# ft.app(target=main, assets_dir='assets', port=5000, view=ft.WEB_BROWSER)