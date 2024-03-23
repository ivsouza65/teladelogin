#NOTE - tela de login do PI
#Esta linha improta a Bliblioteca de estrutura Flet.
import flet as ft
#Esta linha define a função chamada main, essa função e a entrada para aplicação flet, que e necessário um unico argumento.
def main(page: ft.Page):
# TextField
    #Esta linha define o título pagina.
    page.title = "AthenaEnem"
    #Esta linha define o alinhamento vertical da página.
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #Esta linha define o alinhamento horizontal da página.
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #Esta linha atualiza a página.
    page.update()
    #Essa caixa tem o componente de campo de texto.
    txt_usuario = ft.TextField(
        label= "Usuário",#define o texto do rótulo.
        width= 250,#define a largura do campo.
        height= 50,#define a altura di campo.
        border_width= 1.5,# define a largura do campo.
        border_color= "#000000"#define a cor da porda.
    )
    #Esta linha cria o componente de texto.
    txt_senha = ft.TextField(
        label="Senha",#define o texto do rótulo.
        width= 250,#define a largura do campo.
        height= 80,#define a altura di campo.
        border_width=1.5,#define a largura do campo.
        border_color= "#000000",#define a cor da porda.
        color="black",#define a cor do texto dentro do campo como preto.
        password=True#Ativa o modo senha, ocutando os caracteres.
    )
    #essa linha define a função btn_click.
    def btn_click(e):
        u = txt_usuario.value
        s = txt_senha.value
        print(f"o usuário: {u} tem a senha: {s}")
        page.update()
    #Esta linha cria um componente de imagem, para incluir a logo.
    img = ft.Image(
        src="logo.png",#define a origem da logo.
        width=250,#define a largura da imagem.
        height=200,#define a altura da imagem
        fit=ft.ImageFit.CONTAIN,#essa garante que a imagem fica visivel.
    )
    #Esta linha atualiza a página.
    page.update()
    #Esta linha cria o componente de botão, usando o botão flet FilledButton.
    btn = ft.FilledButton("ENTRAR", width=250,height=50,on_click=btn_click)
    #Essa linha aciona  os elementos criados.
    page.add(img,txt_usuario,txt_senha,btn)

# esta linha inicia o aplicativo Flet.
ft.app(target=main)