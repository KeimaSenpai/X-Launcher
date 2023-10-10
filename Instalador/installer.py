import flet as ft


async def main(page: ft.Page):
    page.title = 'X Launcher Instaler'
    page.window_width = '582'
    page.window_height = '380'
    page.window_resizable = False
    page.padding = 0

    logo = ft.Image('../assets/image/x.png', height=30)
    imagen = ft.Image(
        '../assets/image/minecraft.png', height=25)

    contenedor = ft.Column(spacing=10, controls=[
        logo,
        imagen
    ],
    )

    await page.add_async(
        ft.Container(contenedor, width=580, height=380,
                     bgcolor='#303030')
    )


ft.app(target=main)
