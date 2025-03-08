import ttkbootstrap as ttk 
from ttkbootstrap.constants import *
from tkinter import Frame, Label
from PIL import Image, ImageTk, ImageFont
from frames.functions.assets_frame import create_text_image_PIL, prox_question
from services.select_card import filtram_perguntas
import os
import random

def create_how_frame(container, show_main_frame):
    """Cria e retorna o frame de como jogar."""
    
    regras_jogo = (
    "🎉 Como jogar 'Quem é mais provável?' 🍻\n\n"
    "Reúna pelo menos 3 amigos, seja em uma chamada de vídeo ou presencialmente.\n\n "
    "Um jogador será o responsável por ler as perguntas usando o aplicativo.\n\n\n"
    "📢 Como funciona?\n\n"
    "1. O jogador da vez lê a pergunta do aplicativo, como: 'Quem é mais provável de chegar atrasado em um encontro?'\n\n"
    "2. Todos discutem (ou só riem mesmo 😂) e apontam para quem acham que combina mais com a situação.\n\n"
    "3. O mais votado paga um desafio ou, para os maiores de idade, toma um shot! 🍹\n\n"
    "Lembre-se: beba com moderação e, acima de tudo, se divirta! 🎊"
    )


    # Configuração das cores e fonte personalizada
    bg_color = "#f5f5dc"
    header_bg = "#2e2b30"
    text_color = "#222222"
    font_path = os.path.join("assets", "LT Funk.otf")
    custom_font = ImageFont.truetype(font_path, 26)

    # Criar frame principal
    how_frame = Frame(container, bg=bg_color)

    # Cabeçalho
    header_frame = Frame(how_frame, bg=header_bg)
    header_frame.pack(pady=20)

    # Carregando a imagem do cabeçalho
    try:
        img = Image.open("assets/how.png")
        img = img.resize((200, 200), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        img_label = Label(header_frame, image=photo, bg=header_bg)
        img_label.image = photo  # Mantém referência
        img_label.grid(row=0, column=0, padx=10)
    except FileNotFoundError:
        img_label = Label(
            header_frame,
            text="Imagem não encontrada",
            bg=header_bg,
            fg="#e58e8e",
            font=("Georgia", 14),
        )
        img_label.grid(row=0, column=0, padx=10)

    # Frame para o cartão
    card_frame = Frame(
        how_frame,
        bg="#f8f9fa",
        width=600,
        height=300
    )
    card_frame.pack(pady=10)
    card_frame.pack_propagate(False)

    # Texto do cartão
    card_text = Label(
        card_frame,
        text=regras_jogo,
        font=("Georgia", 10),
        wraplength= 600
    )
    card_text.pack(expand=True)


    # Criando botão de voltar (usando ttkbootstrap)
    back_button = ttk.Button(
        how_frame,
        text="Voltar ao Menu",
        bootstyle="secondary",  # Cor do botão
        command=show_main_frame,
    )
    back_button.pack(pady=20)

    # Aplicando a fonte "Georgia" ao botão de voltar
    style = ttk.Style()
    style.configure("TButton", font=("Georgia", 12))

    return how_frame