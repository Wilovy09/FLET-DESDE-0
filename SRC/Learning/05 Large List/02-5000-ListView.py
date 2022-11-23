import flet as ft
from flet import *
from flet import dropdown

def main(page: Page):
    page.theme_mode = 'dark'
    page.title = 'Document'
    page.window_height = 500
    page.window_width = 500

    #! Se supone que esto optimiza el rendimiento
    lv_textos = ListView(expand=True, spacing=10)

    #! Se imprime 5000 veces el texto "Line {i}"
    for i in range(5000):
        lv_textos.controls.append(Text(f'Line {i}'))
    
    page.add(lv_textos)

ft.app(target=main, assets_dir='assets')
# ft.app(target=main, assets_dir='assets', port=5000, view=ft.WEB_BROWSER)