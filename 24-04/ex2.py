import flet as ft
from flet import AppBar, Text, View, ElevatedButton
from flet.core.colors import Colors

class Livro():
    def __init__(self, nome, descricao, categoria, autor):
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.autor = autor

def main(page: ft.Page):
    page.title = "Cadastro de Livros"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 375
    page.window_height = 667

    livros = []

    def salvar_livro(e):
        if input_nome.value.strip() == "":
            snackbar_error.open = True
        else:
            livro = Livro(
                input_nome.value,
                input_descricao.value,
                input_categoria.value,
                input_autor.value
            )
            livros.append(livro)

            input_nome.value = ""
            input_descricao.value = ""
            input_categoria.value = ""
            input_autor.value = ""
            snackbar_sucesso.open = True
        page.update()

    def exibir_lista(e):
        lista_livros.controls.clear()
        for i, livro in enumerate(livros):
            lista_livros.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            Text(f"📘 Nome: {livro.nome}", size=16),
                            Text(f"✍️ Autor: {livro.autor}"),
                            ft.Row([
                                ElevatedButton("Visualizar Detalhes", on_click=lambda e, idx=i: ver_detalhes(idx))
                            ])
                        ]),
                        padding=10
                    )
                )
            )
        page.update()

    def ver_detalhes(index):
        livro = livros[index]
        page.views.append(
            View(
                "/detalhes",
                [
                    AppBar(title=Text("Detalhes do Livro"), bgcolor=Colors.TERTIARY_CONTAINER),
                    Text(f"📝 Descrição: {livro.descricao}", size=18),
                    Text(f"📚 Categoria: {livro.categoria}", size=18),
                    ElevatedButton(text="Voltar", on_click=voltar)
                ]
            )
        )
        page.update()

    def gerencia_rota(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Cadastro de Livros"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ElevatedButton(text="Salvar Livro", on_click=salvar_livro),
                    ElevatedButton(text="Exibir Lista", on_click=lambda _: page.go("/lista")),
                ]
            )
        )
        if page.route == "/lista":
            exibir_lista(e)
            page.views.append(
                View(
                    "/lista",
                    [
                        AppBar(title=Text("Lista de Livros"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lista_livros
                    ]
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Campos
    input_nome = ft.TextField(label="Nome do Livro")
    input_descricao = ft.TextField(label="Descrição")
    input_categoria = ft.TextField(label="Categoria")
    input_autor = ft.TextField(label="Autor")

    lista_livros = ft.Column()

    snackbar_sucesso = ft.SnackBar(content=Text("Livro cadastrado com sucesso!"), bgcolor=Colors.GREEN)
    snackbar_error = ft.SnackBar(content=Text("Nome do livro não pode estar vazio!"), bgcolor=Colors.RED)

    page.overlay.append(snackbar_sucesso)
    page.overlay.append(snackbar_error)
    page.on_route_change = gerencia_rota
    page.on_view_pop = voltar

    page.go(page.route)

ft.app(main)