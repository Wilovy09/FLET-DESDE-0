import flet as ft
from flet import *

background = "#fddddd"

def main(page: Page):
    #! Para poner un font
    page.fonts = {
        'Firacode': "/fonts/Fira Code Bold Nerd Font Complete Mono Windows Compatible.ttf"
        }
    page.theme = Theme(font_family="Firacode")
    
    #! Para hacer transparente una ventana (se requieren todos)
    # page.window_bgcolor = ft.colors.TRANSPARENT
    # page.bgcolor = ft.colors.TRANSPARENT
    # page.window_title_bar_hidden = True
    # page.window_frameless = True

    #! Para poner un fondo
    # page.bgcolor = ft.colors.WHITE
    page.bgcolor = background

    #! Para quitar la barra de titul o frame
    # page.window_title_bar_hidden = True
    # page.window_frameless = True

    #! Para poner un tema a la app 'dark','light' o 'system'
    # page.theme_mode="light"
    
    #! Para ponerle padding a la pagina
    page.padding = 50
    
    #! Para ponerle un tamaño a la ventana
    page.window_width = 500
    page.window_height = 500
    
    #! Para ponerle un titulo a la ventana
    page.title = 'Tests'
    
    #! Para no dejar resteablecer el tamaño de la ventana
    page.window_resizable = True
    
    #! Para ponerle un icono a la ventana (no se como se usa)
    # page.window_icon = 'https://flet.app/favicon.ico'

    #! Para no aparecer en la barra de tareas
    # page.window_skip_task_bar = True

    #! Para ponerle opacidad a la ventana
    # page.window_opacity = 0.9

    #! Para que la ventana se aparezca activa desde el inicio
    page.window_focused = True

    t = Text(
        value="FLET\n&\nPython!",
        size=30,
        color="white",
        bgcolor="pink",
        weight="bold",
        italic=True,
        text_align="center"
    )

    page.add(t)

ft.app(target=main, assets_dir="assets")
# ft.app(target=main, assets_dir="assets", port=5000, view=ft.WEB_BROWSER)