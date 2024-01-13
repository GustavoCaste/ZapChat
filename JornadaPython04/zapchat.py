

# Titulo Zapchat
# Botão de iniciar o chat
    # Popup
        # Bem vindo ao Zapchat
        # Escreva seu nome
        # Entrar no chat
# Chat
    # Gustavo entrou no chat
    # Mensagens do usuário
# Campo para enviar mensagem
# Botão de enviar

import flet as ft  


def main(pagina):
    titulo = ft.Text("Zapchat")
    
    nome_usuario = ft.TextField(label = "Escreva seu nome")

    chat = ft.Column()
   
    def enviar_mensagem_tunel(informacoes):
       chat.controls.append(ft.Text(informacoes))
       pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)



    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        pagina.pubsub.send_all(texto_campo_mensagem)

        # Limpar o campo_mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar",on_click=enviar_mensagem)
    def entrar_chat(evento):
        # Feche o popup
        popup.open = False
        # Tire o botao iniciar chat da tela
        pagina.remove(botao_iniciar)
        # Adicionar o chat
        pagina.add(chat)
        # Cria o campo de enviar mensagem
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )
        # Botao de enviar mensagem
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.add(linha_mensagem)
        
        pagina.update


    
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Zapchat"),
        content= nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
        )

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    
ft.app(main, view=ft.WEB_BROWSER)
#ft.app(main)