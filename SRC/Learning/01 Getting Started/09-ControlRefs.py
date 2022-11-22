import flet
from flet import *

def main(page: Page):
    
    # Declaramos variables
    #? autofocus=True significa que al iniciar la app el cursor se pondrá en este campo
    firsName = TextField(label="First Name", autofocus=True)
    lastsName = TextField(label="Lasts Name")
    colControles = Column()
    
    # Definimos funcion de saludar
    def saludar_clicked(event):
        # Mostramos el valor de las variables
        colControles.controls.append(Text(f'¡Hola {firsName.value} {lastsName.value}!'))

        # Limpiamos los campos
        firsName.value = ""
        lastsName.value = ""

        # Actualizamos la página
        page.update()
        # Ponemos el foco en el primer campo
        firsName.focus()

    # Creamos un botón con el evento on_click=saludar_clicked     para llamar a la función saludar_clicked
    btnHello = ElevatedButton("Saludar", on_click=saludar_clicked)

    # Añadimos los controles a la pagina
    page.add(
        firsName,
        lastsName,
        btnHello,
        colControles
    )

flet.app(target=main)
# flet.app(target=main, port=5000, view=flet.WEB_BROWSER)