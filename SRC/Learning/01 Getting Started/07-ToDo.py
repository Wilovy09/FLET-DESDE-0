import flet
from flet import *

def main(page: Page):
    
    # Crear funcion para agregar tarea
    def addTask(event):

        # Obtener el checkbox con el input
        page.add(Checkbox(label=task.value))

    # Creamos un campo de texto donde se ingresara la tarea
    task = TextField(hint_text="Ingrese la tarea", width=300)

    # Creamos un boton para agregar la tarea
    btnAddTask = ElevatedButton("Agregar tarea", on_click=addTask)

    # Creamos un contenedor para el campo de texto y el boton
    page.add(Row([task, btnAddTask]))


flet.app(target=main)
# flet.app(target=main, port=5000, view=flet.WEB_BROWSER)