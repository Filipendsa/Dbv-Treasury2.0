import flet as ft

def main(page: ft.Page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()
    page.title = "DBV - Treasury"
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.ATTACH_MONEY_SHARP),
        leading_width=40,
        title=ft.Text("DBV - Treasury"),
        center_title=False,
        bgcolor=ft.colors.GREEN_ACCENT_700,
        actions=[
            # ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Home", icon=ft.icons.HOME),
                    ft.PopupMenuItem(),
                ]
            ),
        ],
    )
    page.navigation_bar = ft.NavigationBar(
        bgcolor=ft.colors.GREEN_ACCENT_700,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home",tooltip="Home"),
            ft.NavigationDestination(icon=ft.icons.QUERY_STATS, label="Balanço",tooltip="Balancete"),
            ft.NavigationDestination(icon=ft.icons.ADD_CARD, label="Add",tooltip="Adicionar novo saldo"),
            ft.NavigationDestination(icon=ft.icons.CREDIT_CARD_OFF, label="Send",tooltip="Adicionar despesa"),
        ]
    )

ft.app(target=main)