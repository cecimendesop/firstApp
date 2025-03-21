import flet as ft


def main(page: ft.Page):
    # configuração da página
    page.title = "Minha aplicação flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # funções
    def verifica_numero(e):
        try:
            num1 = int(input_numero.value)
            par_impar = num1 % 2
            if par_impar == 0:
                txt_resultado.value = "par"
            else:
                txt_resultado.value = "ímpar"
        except ValueError:
            print("Insira um número")

        page.update()

    # criação componentes
    input_numero = ft.TextField(label='Número', hint_text='Digite um numero')
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=verifica_numero
    )
    txt_resultado = ft.Text(value="")


    #layout
    page.add(
        ft.Column(
            [
                input_numero,
                btn_enviar,
                txt_resultado,
            ]
        )
    )

ft.app(main)