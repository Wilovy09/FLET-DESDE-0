import flet
from flet import Page, Text

def main(page: Page):
    # Generamos una variable con un control tipo Text
    lblText = Text(value="Hello World", color="#FFFFFF", size=25)
    
    # Agregamos el control a la página
    page.controls.append(lblText)

    # Actializamos la página
    page.update()

#Ejecutamos como web
flet.app(target=main, port=5000, view=flet.WEB_BROWSER)