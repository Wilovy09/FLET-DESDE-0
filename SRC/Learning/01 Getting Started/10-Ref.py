import flet
from flet import *
from flet.ref import Ref

def main(page: Page):
    
    # Declaramos variables
    #? autofocus=True significa que al iniciar la app el cursor se pondrá en este campo
    firsName = Ref[TextField]()
    lastsName = Ref[TextField]()
    colControles = Ref[Column]()
    
    # Definimos funcion de saludar
    def saludar_clicked(event):
        # Mostramos el valor de las variables
        colControles.current.controls.append(Text(f'¡Hola {firsName.current.value} {lastsName.current.value}!'))

        # Limpiamos los campos
        firsName.current.value = ""
        lastsName.current.value = ""

        # Actualizamos la página
        page.update()
        # Ponemos el foco en el primer campo
        firsName.current.focus()

    # Creamos un botón con el evento on_click=saludar_clicked     para llamar a la función saludar_clicked
    btnHello = ElevatedButton("Saludar", on_click=saludar_clicked)

    # Añadimos los controles a la pagina
    page.add(
        TextField(ref=firsName, label="Nombre", autofocus=True),
        TextField(ref=lastsName, label="Apellido"),
        btnHello,
        Column(ref=colControles)
    )

flet.app(target=main)
# flet.app(target=main, port=5000, view=flet.WEB_BROWSER)