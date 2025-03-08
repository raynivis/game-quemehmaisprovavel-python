import ttkbootstrap as ttk
from tkinter import Label, Frame, messagebox
from PIL import Image, ImageTk, ImageFont
from frames.functions.assets_frame import create_text_image_Tk, play_music, pause_music
from frames.friends_frame import create_friends_frame
from frames.family_frame import create_family_frame
from frames.how_frame import create_how_frame
import os

# Função para sair do modo fullscreen ao pressionar "Esc"
def sair_fullscreen(event):
    root.attributes("-fullscreen", False)

# Função para entrar no modo fullscreen ao pressionar "F11"
def entrar_fullscreen(event):
    root.attributes("-fullscreen", True)

# Função para alternar entre frames
def show_frame(frame):
    frame.tkraise()

# Configuração principal da janela
root = ttk.Window(themename="darkly")
root.title("Quem é mais Provável?")
root.geometry("1280x720")
root.iconbitmap("assets/favicon.ico")
root.attributes("-fullscreen", True)  # Abre em fullscreen
root.bind("<Escape>", sair_fullscreen)  # Atalho para sair do fullscreen
root.bind("<F11>", entrar_fullscreen)  # Atalho para entrar no fullscreen
play_music()

# Configurações de estilos e cores
highlight_color = "#eaa1a1"
bg_color = "#DDDDDD"
text_color = "#222222"

# Caminho da fonte personalizada
font_path = os.path.join("assets", "LT Funk.otf")  # Caminho da fonte
custom_font = ImageFont.truetype(font_path, 25)  # Carrega a fonte personalizada

# Container principal para alternar frames
container = Frame(root, bg=bg_color)
container.pack(fill="both", expand=True)

# Frame principal (Menu)
main_frame = Frame(container, bg=bg_color)
main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# Frame Cartas para a Família
family_frame = create_family_frame(container, lambda: show_frame(main_frame))
family_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# Frame Cartas para os Amigos
friends_frame = create_friends_frame(container, lambda: show_frame(main_frame))
friends_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# Frame Como jogar
how_frame = create_how_frame(container, lambda: show_frame(main_frame))
how_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# Funções para os botões do menu
def cartas_familia(event=None):
    show_frame(family_frame)

def cartas_amigos(event=None):
    show_frame(friends_frame)
    
def como_jogar(event=None):
    show_frame(how_frame)
    
# Função para confirmar saída
def confirm_exit():
    resposta = messagebox.askyesno("Sair", "Tem certeza que deseja sair do jogo?")
    if resposta:  # Se clicar em "Sim", fecha o jogo
        root.quit()

# Título com imagem
try:
    img = Image.open("assets/logoSombra.png")
    logo = ImageTk.PhotoImage(img)
    logo_label = Label(main_frame, image=logo, bg=bg_color)
    logo_label.pack(pady=50)
except FileNotFoundError:
    error_image = create_text_image_Tk("Logo não encontrada", custom_font, "red", bg_color)
    logo_label = Label(main_frame, image=error_image, bg=bg_color)
    logo_label.pack(pady=50)

# Botões personalizados com eventos de clique e cursor "mão"
family_text = create_text_image_Tk("Cartas para a Família", custom_font, text_color, bg_color)
family_button = Label(main_frame, image=family_text, bg=bg_color, cursor="hand2")
family_button.pack(pady=10)
family_button.bind("<Button-1>", cartas_familia)  # Adiciona evento de clique

friends_text = create_text_image_Tk("Cartas para os Amigos", custom_font, text_color, bg_color)
friends_button = Label(main_frame, image=friends_text, bg=bg_color, cursor="hand2")
friends_button.pack(pady=10)
friends_button.bind("<Button-1>", cartas_amigos)  # Adiciona evento de clique

custom_font_how = ImageFont.truetype(font_path, 14)  # Carrega a fonte personalizada



# Adicionando os botões ao frame
how_text = create_text_image_Tk("Como jogar?", custom_font_how, text_color, bg_color)
how_button = Label(main_frame, image=how_text, bg=bg_color, cursor="hand2")
how_button.pack(pady=10)
how_button.bind("<Button-1>", como_jogar)

# Criando um frame para organizar os botões na horizontal
button_frame = Frame(main_frame, bg=bg_color)
button_frame.pack(pady=5)

music_button = ttk.Button(
    button_frame,
    text="🔊",
    command=lambda: pause_music(music_button),
    style="light.TButton",
)
music_button.pack(side="left", padx=5)

# Criando o botão de saída com modal de confirmação
exit_button = ttk.Button(
    button_frame,
    text="⏻",
    command=confirm_exit,  # Chama a função ao clicar
    style="light.TButton",
)
exit_button.pack(side="left", padx=5)


# Exibe o frame principal inicialmente
show_frame(main_frame)

# Texto do rodapé
footer_text = Label(
    root,
    text="© Produzido por Ray Del Negro",
    bg="#2e2b30",
    fg="#b8a89e",
    font=("Arial", 10),
)
footer_text.pack(side="bottom", pady=10)

# Inicia o loop principal
root.mainloop()
