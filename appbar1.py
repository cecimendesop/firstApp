import flet as ft
from flet import AppBar, ElevatedButton, Text, View
from flet.core.colors import Colors


def main(page: ft.Page):
    # configuração da página
    page.title = "Minha aplicação flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def gerencia_rota(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    ElevatedButton(text="Navegar", on_click=lambda _: page.go("/segunda"))
                ],
            )
        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda Tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text(f'Olá {input_nome.value}, seja bem-vindo!'),
                    ]

                )
            )

        page.update()
        # componente
    input_nome = ft.TextField(label="Nome", hint_text="Digite seu nome")

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rota
    page.on_view_pop = voltar


    page.go(page.route)


ft.app(main)
