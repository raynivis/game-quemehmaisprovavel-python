import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Frame, Label
from PIL import Image, ImageTk, ImageFont
from frames.functions.assets_frame import create_text_image_PIL, prox_question
from services.select_card import filtram_perguntas
import os
import random

def create_family_frame(container, show_main_frame):
    """Cria e retorna o frame do modo Familia."""
    
     # Carrega as perguntas do modo familia
    perguntas_familia = filtram_perguntas(["Familia"])
    # Seleciona a primeira pergunta e a remove
    pergunta_aleatoria = random.choice(perguntas_familia)
    perguntas_familia.remove(pergunta_aleatoria)

    # Configuração das cores e fonte personalizada
    bg_color = "#f5f5dc"
    header_bg = "#2e2b30"
    text_color = "#222222"
    font_path = os.path.join("assets", "LT Funk.otf")
    custom_font = ImageFont.truetype(font_path, 26)

    # Criar frame principal
    friends_frame = Frame(container, bg=bg_color)

    # Cabeçalho
    header_frame = Frame(friends_frame, bg=header_bg)
    header_frame.pack(pady=20)

    # Carregando a imagem do cabeçalho
    try:
        img = Image.open("assets/familiaSombra.png")
        img = img.resize((180, 130), Image.LANCZOS)
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

    # Texto do cabeçalho
    header_text = Label(
        header_frame,
        text="Modo\nFamília",
        bg=header_bg,
        fg="#ffffff",
        font=("Georgia", 22, "bold"),
        justify="center",
    )
    header_text.grid(row=0, column=1)

    # Frame para o cartão
    card_frame = Frame(
        friends_frame,
        bg="#f8f9fa",
        width=450,
        height=250,
        highlightbackground="#DDDDDD",
        highlightthickness=1,
    )
    card_frame.pack(pady=20)
    card_frame.pack_propagate(False)

    # Texto do cartão
    card_text = Label(
        card_frame,
        text="Quem é mais provável de " + pergunta_aleatoria,
        font=("Georgia", 14),
        wraplength=400,
        justify="center",
    )
    card_text.pack(expand=True)

    # Criando imagem para o botão "Próxima Carta"
    next_button_pil = create_text_image_PIL("Próxima Carta", custom_font, text_color, bg_color)
    next_button_image = ImageTk.PhotoImage(next_button_pil)

    # Botão "Próxima Carta"
    next_button = Label(friends_frame, image=next_button_image, bg=bg_color, cursor="hand2")
    next_button.image = next_button_image  # Mantém referência
    next_button.pack(pady=20)
    next_button.bind("<Button-1>", lambda event: prox_question(perguntas_familia, card_text))

    # Criando botão de voltar (usando ttkbootstrap)
    back_button = ttk.Button(
        friends_frame,
        text="Voltar ao Menu",
        bootstyle="secondary",  # Cor do botão
        command=show_main_frame,
    )
    back_button.pack(pady=20)

    # Aplicando a fonte "Georgia" ao botão de voltar
    style = ttk.Style()
    style.configure("TButton", font=("Georgia", 12))

    return friends_frame
