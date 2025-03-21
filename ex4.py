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
        
        data_atual = datetime.now().date()
        txt_resultado.value = f"Data de nascimento: {data_atual} - {input_nascimento}"
        idade = {data_atual} - {input_nascimento}

        if input_nascimento >= 18:
            print("Ele tem" {idade}"anos, o que faz dele maior de idade")
        elif input_nascimento <= 18:
            print("Ele tem"{idade} "anos, o que faz dele menor de idade")

        # criação componentes
    input_nascimento = ft.TextField(label='Data',
                                hint_text='Digite sua data de nascimento')
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=verifica_idade
    )
    txt_resultado = ft.Text(value="")
    # layout


ft.app(main)
