import flet as ft
from flet import *

def main(page: Page):
    page.theme_mode = 'light'
    page.title = 'Greeter'
    page.window_width = 500
    page.window_height = 500

    def saludar_clicked(e):
        if not txt_Name.value:
            txt_Name.error.value = 'Por favor, ingrese su nombre'
            page.update()
        else:
            nombre = txt_Name.value
            
            #! Remueve todos los elementos de la página
            page.clean()
            page.add(
                Text(f'Hola {nombre}!')
                )
    
    txt_Name = TextField(label="Ingresa tu nombre", width=200)

    page.add(
        txt_Name,
        ElevatedButton("Saludar", on_click=saludar_clicked)
    )

ft.app(target=main, assets_dir='assets')
# ft.app(target=main, assets_dir='assets', port=5000, view=ft.WEB_BROWSER)