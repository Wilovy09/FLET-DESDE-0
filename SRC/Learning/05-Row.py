import flet
from flet import Page, Row, Text


def main(page: Page):
    #! ##############################################
    # lenguajes = ['Python', 'Java', 'C#', 'C++', 'JavaScript', 'PHP', 'C', 'Ruby', 'Swift', 'Go']
    # etiquetas = []
    # for e in lenguajes:
    #     etiquetas.append(Text(value=e))
    # rowDatos = Row(controls=etiquetas)
    #! ##############################################

    # Declaramos el Row con controls adentro
    rowDatos = Row(controls=[
        Text("Python"), # Declaramos el control=[Text con el valor "Python"] 
        Text("Java"), # Declaramos el control=[Text con el valor "Java"] 
        Text("C#"), # Declaramos el control=[Text con el valor "C#"] 
        Text("C++"), # Declaramos el control=[Text con el valor "C++"] 
        Text("JavaScript"), # Declaramos el control=[Text con el valor "JavaScript"] 
        Text("PHP"), # Declaramos el control=[Text con el valor "PHP"] 
        Text("C"), # Declaramos el control=[Text con el valor "C"] 
        Text("Ruby"), # Declaramos el control=[Text con el valor "Ruby"] 
        Text("Swift"), # Declaramos el control=[Text con el valor "Swift"] 
        Text("Go")]) # Declaramos el control=[Text con el valor "Go"] 

    # Agregamos el Row a la página
    page.add(rowDatos)


flet.app(target=main)
# flet.app(target=main, port=5000, view=flet.WEB_BROWSER)
