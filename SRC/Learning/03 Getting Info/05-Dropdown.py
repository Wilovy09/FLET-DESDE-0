import flet as ft
from flet import *
from flet import dropdown

def main(page: Page):
    page.theme_mode = 'dark'
    page.title = 'Dropdown'
    page.window_height = 500
    page.window_width = 500

    def submit_clicked(e):
        lbl_resultado.value = f'El valor del dropdown es: {cbx_color.value}'
        page.update()
    
    lbl_resultado = Text("")
    btn_submit= ElevatedButton("Submit", on_click=submit_clicked)

    #! Definimos el dropdown con sus opciones
    cbx_color = Dropdown(
        width=100,
        value='Rojo', #! Valor por defecto
        options=[
            dropdown.Option('Rojo'),
            dropdown.Option('Verde'),
            dropdown.Option('Azul')
        ],
    )

    page.add(
        cbx_color,
        btn_submit,
        lbl_resultado
        )

ft.app(target=main, assets_dir='assets')
# ft.app(target=main, assets_dir='assets', port=5000, view=ft.WEB_BROWSER)