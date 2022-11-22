import flet
from flet import Page, Row, Text, TextField, ElevatedButton

def main(page: Page):    
    # Declaramos una variable con TextField y el label "Ingrese su nombre"
    nombre = TextField(label="Ingrese su nombre")

    # lbl saluda al usuario
    lblSaludo = Text()

    # Función que se ejecuta al hacer click en el botón
    def saludar(event):
        lblSaludo.value = f"Hola {nombre.value}!"
        page.update()

    # Declaramos el Row con controls adentro
    HelloThere = Row(controls=[
        
        # Llamamos a la variable nombre
        nombre,

        # Declaramos ElevatedButton con el label "Saludar" y la función saludar
        ElevatedButton(text="Saludar", on_click=saludar),

        # Llamamos a la variable del saludo
        lblSaludo
    ])
    
    # Agregamos el HelloThere/Row a la página
    page.add(HelloThere)


flet.app(target=main)
# flet.app(target=main, port=5000, view=flet.WEB_BROWSER)