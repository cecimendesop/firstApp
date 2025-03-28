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
                    AppBar(title=Text("Cadastro de Livros"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nomelivro,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ElevatedButton(text="Enviar", on_click=lambda _: page.go("/segunda"))
                ],
            )
        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Exibição"), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text(f'Livro: {input_nomelivro.value}'),
                        Text(f'Descrição: {input_descricao.value}'),
                        Text(f'Categoria: {input_categoria.value}'),
                        Text(f'Autor: {input_autor.value}'),
                    ]

                )
            )

        page.update()
        # componente

    input_nomelivro = ft.TextField(label="Nome", hint_text="Digite o nome do livro")
    input_descricao = ft.TextField(label="Descrição", hint_text="Digite uma breve descrição")
    input_categoria = ft.TextField(label="Categoria", hint_text="Romance, Ação, Aventura")
    input_autor = ft.TextField(label="Autor", hint_text="Digite o autor")

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rota
    page.on_view_pop = voltar

    page.go(page.route)


ft.app(main)