import flet as ft
from flet import Container, icons, Page, IconButton, Row, Text, colors, alignment, Image, Stack, Column


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.title = 'X Launcher'
    page.window_width = 1000
    page.window_height = 590
    page.window_resizable = False
    page.padding = 0

    bg = Image(src=f'/images/bg1.jpg', fit=ft.ImageFit.CONTAIN)
    logo = Image(src=f'/images/logo.png', height=70)

    def column_with_horiz_alignment(align: ft.CrossAxisAlignment):
        return ft.Column(
            [
                ft.Container(
                    ft.Column([logo],
                              alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                              horizontal_alignment=align,
                              ),
                ),
            ]
        )

    page.add(Stack([
        bg,
        ft.Row(
            [
                column_with_horiz_alignment(ft.CrossAxisAlignment.CENTER)
            ],
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    ]),

    )


ft.app(target=main, assets_dir="assets")
