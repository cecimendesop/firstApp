import flet as ft
from datetime import datetime


def main(page: ft.Page):
    # configuração da página
    page.title = "Minha aplicação flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # funções
    def verifica_idade(e):
        try:
            txt_resultado.value = input_nascimento.value
            data_nascimento = datetime.strptime(input_nascimento.value, "%d/%m/%Y")
            data_atual = datetime.now()
            idade = data_atual.year - data_nascimento.year
            if datetime.today().month < data_nascimento.month:
                idade = idade - 1
            if int(idade) >= 18:
                txt_resultado.value = f'Maior de idade, você tem {idade} anos'
            else:
                txt_resultado.value = f'Menor de idade, você tem {idade} anos'
            page.update()
        except ValueError:
            return 'Insira atributos válidos'

    # criação componentes
    input_nascimento = ft.TextField(label='Nascimento', hint_text='Digite seu ano de nascimento')
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=verifica_idade
    )
    txt_resultado = ft.Text(value="")
    # layout
    page.add(
        ft.Column(
            [
                input_nascimento,
                btn_enviar,
                txt_resultado,
            ]
        )
    )

ft.app(main)
