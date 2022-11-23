import flet as ft
from flet import *

def main(page: Page):
    page.theme_mode = 'dark'
    page.title = 'Document'
    page.window_height = 500
    page.window_width = 500

    def checkbox_cicked(e):
        lbl_resultado.value = (f'¡Has aprendido a programar en Python!')
        # lbl_resultado.value = (f'Has aprendido a programar en Python? {chk_tarea.value}')
        page.update()

    lbl_resultado = Text()

    chk_tarea = Checkbox(label="Aprender a progrmar en Python", value=False, on_change=checkbox_cicked)

    page.add(
        chk_tarea,
        lbl_resultado
        )

ft.app(target=main, assets_dir='assets')
# ft.app(target=main, assets_dir='assets', port=5000, view=ft.WEB_BROWSER)