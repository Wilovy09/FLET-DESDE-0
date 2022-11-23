import os
import flet as ft
from flet import *
from flet import dropdown, alignment, border, border_radius

os.environ['FLET_WS_MAX_MASSAGE_SIZE'] = '8000000'

def main(page: Page):
    page.theme_mode = 'dark'
    page.title = 'Document'
    page.window_height = 500
    page.window_width = 500

    gv = GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(gv)

    for i in range(5000):
        gv.controls.append(
            Container(
                Text(f'Item {i}'),
                alignment=alignment.center,
                bgcolor=colors.AMBER_100,
                border=border.all(1, colors.AMBER_400),
                border_radius=border_radius.all(5),
            )
        )
    page.update()

# ft.app(target=main, assets_dir='assets')
ft.app(target=main, assets_dir='assets', port=5000, view=ft.WEB_BROWSER)