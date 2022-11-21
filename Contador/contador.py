# Importamos FLET
import flet
# Importamos los elementos que usaremos de FLET
from flet import IconButton, Page, Row, TextField, icons

# Creamos una funcion con el parametro page, de tipo Page   main(page: Page)
def main(page: Page):

    # Titulo de la pagina
    page.title = "Contador"
    
    # La alineacion vertical de los elementos en el medio
    page.vertical_alignment = "center"

    # Creamos un objeto de tipo texto con valor 0
    txtNumber = TextField(value="0", text_align="right", width=100)

    # Definimos una funcion con el parametro EVENT para el boton de restar
    def minusClick(event):
        txtNumber.value = int(txtNumber.value) - 1
        
        # Actualizamos la pagina
        page.update()
    
    # Definimos una funcion con el parametro EVENT para el boton de sumar
    def plusClick(event):
        txtNumber.value = int(txtNumber.value) + 1
        
        # Actualizamos la pagina
        page.update()
    
    # Añadimos los elementos a la pagina
    page.add(
        # Creamos una fila
        Row(
            [
                # Creamos un boton con el icono de restar con su funcion
                IconButton(icons.REMOVE, on_click=minusClick),
                # Llamamos al objeto de texto
                txtNumber,
                # Creamos un boton con el icono de sumar con su funcion
                IconButton(icons.ADD, on_click=plusClick)
                # esto se veria asi
                # [-] [0] [+]
            ]
            # alineamos en el centro
            ,alignment="center",
        )
    )

# Ejecutamos la funcion main como app
# flet.app(target=main)

# Ejecuramos la funcion main como web
# flet.app(target=main, view=flet.WEB_BROWSER)

# Ejecuramos la funcion main como web y con puerto 5000
flet.app(target=main, port=5000, view=flet.WEB_BROWSER)