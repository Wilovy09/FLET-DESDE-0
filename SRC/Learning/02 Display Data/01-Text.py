import flet as ft
from flet import *

def main(page: Page):
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