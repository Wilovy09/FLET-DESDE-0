import flet as ft
from flet import *

def main(page: Page):
    page.title = 'Contador'
    page.vertical_alignment = 'center'
    page.window_width = 300
    page.window_height = 300
    
    txt_Number = TextField(value='0', text_align='right', width=100)

    def reducir_clicked(e):
        txt_Number.value = int(txt_Number.value) - 1
        page.update()

    def aumentar_clicked(e):
        txt_Number.value = int(txt_Number.value) + 1
        page.update()

    page.add(
        Row([
                IconButton(icons.REMOVE, on_click=reducir_clicked),
                txt_Number,
                IconButton(icons.ADD, on_click=aumentar_clicked)],alignment='center')
    )

# ft.app(target=main, assets_dir='assets')
ft.app(target=main, assets_dir='assets', port=5000, view=ft.WEB_BROWSER)