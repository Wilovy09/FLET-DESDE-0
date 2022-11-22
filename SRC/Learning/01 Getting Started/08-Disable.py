import flet
from flet import *

def main(page: Page):
    firstName = TextField(label="First Name")
    lastName = TextField(label="Last Name")

    #? Disable de forma individual
    # firstName.disabled = True
    # lastName.disabled = True


    ColumnControles = Column(controls=[firstName, lastName])

    #? Disable de forma global
    # ColumnControles.disabled = True

    page.add(ColumnControles)

flet.app(target=main)
# flet.app(target=main, port=5000, view=flet.WEB_BROWSER)