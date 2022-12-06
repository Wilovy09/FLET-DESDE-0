import flet as ft
from flet import *
from flet import alignment

def main(page: Page):
    page.theme_mode = 'dark'
    page.title = 'Draggable'
    
    def drag_accept(e):
        src=page.get_control(e.src_id)
        src.content.content.value = "0"
        e.control.content.content.value = "1"
        page.update()

    page.add(
        Row(
            [
                Draggable(
                    group="Number",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.CYAN_200,
                        border_radius=5,
                        content=Text("1", size=20),
                        alignment=alignment.center,
                    ),
                ),
                Container(width=100),
                DragTarget(
                    group="Number",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.PINK_200,
                        border_radius=5,
                        content=Text("0", size=20),
                        alignment=alignment.center,
                    ),
                    on_accept=drag_accept,
                ),
            ]
        )
    )
ft.app(target=main, assets_dir='assets')