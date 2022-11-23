import flet as ft
from flet import *
from flet import dropdown

def main(page: Page):
    page.theme_mode = 'dark'
    page.title = 'Document'
    page.window_height = 720
    page.window_width = 500

    #! Shortcuts
    def on_keyboard(e: KeyboardEvent):
        page.add(
            Text(f'| Key: {e.key} | Shift: {e.shift} | Ctrl: {e.ctrl} | Alt: {e.alt} | Meta: {e.meta}'),
        )
    
    page.on_keyboard_event = on_keyboard
    
    
    page.add(
        Text('Press any key con una combinacion (Shift, Ctrl, Alt, Meta)'),
    )

ft.app(target=main, assets_dir='assets')
# ft.app(target=main, assets_dir='assets', port=5000, view=ft.WEB_BROWSER)