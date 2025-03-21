import flet as ft


def main(page: ft.Page):
    # configuração da página
    page.title = "Minha aplicação flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # funções
    def soma(e):
        try:
            numero1 = int(input_numero1.value)
            numero2 = int(input_numero2.value)
            txt_resultado.value = f"Resultado: {numero1 + numero2}"
            page.update()
        except ValueError:
            txt_resultado.value = "Erro: Parâmetros inválidos"

    def subtracao(e):
        try:
            numero1 = int(input_numero1.value)
            numero2 = int(input_numero2.value)
            txt_resultado.value = f"Resultado: {numero1 - numero2}"
            page.update()
        except ValueError:
            txt_resultado.value = "Erro: Parâmetros inválidos"

    def multiplicacao(e):
        try:
            numero1 = int(input_numero1.value)
            numero2 = int(input_numero2.value)
            txt_resultado.value = f"Resultado: {numero1 * numero2}"
            page.update()
        except ValueError:
            txt_resultado.value = "Erro: Parâmetros inválidos"

    def divisao(e):
        try:
            numero1 = int(input_numero1.value)
            numero2 = int(input_numero2.value)
            txt_resultado.value = f"Resultado: {numero1 / numero2}"
            page.update()
        except ValueError:
            txt_resultado.value = "Erro: Parâmetros inválidos"


    # criação componentes
    input_numero1 = ft.TextField(label='Número', hint_text='Digite um numero')
    input_numero2 = ft.TextField(label='Número', hint_text='Digite um numero')
    btn_adicao = ft.FilledButton(
        text="Adição",
        width=page.window.width,
        on_click=soma,
    )
    btn_subtracao = ft.FilledButton(
        text="Subtração",
        width=page.window.width,
        on_click=subtracao,
    )
    btn_multiplicacao = ft.FilledButton(
        text="Multiplicação",
        width=page.window.width,
        on_click=multiplicacao,
    )
    btn_divisao = ft.FilledButton(
        text="Divisão",
        width=page.window.width,
        on_click=divisao,
    )
    txt_resultado = ft.Text(value="")


    #layout
    page.add(
        ft.Column(
            [
                input_numero1,
                input_numero2,
                btn_adicao,
                btn_subtracao,
                btn_multiplicacao,
                btn_divisao,
                txt_resultado,
            ]
        )
    )


ft.app(main)