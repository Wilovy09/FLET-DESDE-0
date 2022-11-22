import flet
from flet import Page, Text
from time import sleep

def main(page: Page):
    t = Text()
    page.add(t) # shortcut for page.controls.append(t)

    for i in range(10):
        t.value = f"Step {i}"
        page.update()
        sleep(1)

flet.app(target=main, port=5000, view=flet.WEB_BROWSER)
# flet.app(target=main)