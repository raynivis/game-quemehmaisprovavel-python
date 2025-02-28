from PIL import Image, ImageTk, ImageDraw
import random
import pygame


# Função para criar texto como imagem com a fonte personalizada
def create_text_image_Tk(text, font, text_color, bg_color):
    """Cria uma imagem a partir de um texto usando a fonte personalizada."""
    text_bbox = font.getbbox(text)  # Obtém a caixa delimitadora do texto
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    image = Image.new("RGBA", (text_width + 20, text_height + 20), bg_color)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, font=font, fill=text_color)
    return ImageTk.PhotoImage(image)

def create_text_image_PIL(text, font, text_color, bg_color):
    """Cria uma imagem a partir de um texto usando a fonte personalizada."""
    text_bbox = font.getbbox(text)  # Obtém a caixa delimitadora do texto
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    image = Image.new("RGBA", (text_width + 20, text_height + 20), bg_color)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, font=font, fill=text_color)

    return image  # Retorna a imagem PIL

def animate_text(label, new_text, step=2, interval=30):
    """
    Animação de fade-out e fade-in para alterar o texto de um Label.

    label: Label do tkinter que será animado.
    new_text: Novo texto a ser exibido.
    step: Intensidade da redução/aumento do tamanho da fonte.
    interval: Intervalo de tempo entre etapas, em milissegundos.
    """
    original_font = label.cget("font")  # Obtém a fonte original
    font_name, font_size, *font_style = original_font.split()  # Divide a fonte

    font_size = 14

    def shrink_text(size):
        if size > 5:  # Tamanho mínimo antes de trocar o texto
            label.config(font=(font_name, size, *font_style))
            label.after(interval, shrink_text, size - step)
        else:
            label.config(text=new_text)
            grow_text(5)  # Começa a aumentar o texto novamente

    def grow_text(size):
        if size < font_size:
            label.config(font=(font_name, size, *font_style))
            label.after(interval, grow_text, size + step)

    shrink_text(font_size)  # Inicia o efeito de fade-out



def prox_question(perguntas, card_text):
    """Seleciona uma nova pergunta aleatória e atualiza o texto do cartão com animação."""
    # Obtém o texto atual da Label
    current_text = card_text.cget("text")  

    # Se já estiver exibindo a mensagem final, não faz nada
    if current_text == "Não há mais perguntas! \n (╥﹏╥)":
        return  

    # Se ainda houver perguntas, seleciona uma nova
    if perguntas:
        pergunta_aleatoria = random.choice(perguntas)
        new_text = "Quem é mais provável de " + pergunta_aleatoria
        perguntas.remove(pergunta_aleatoria)  # Remove a pergunta usada
    else:
        new_text = "Não há mais perguntas! \n (╥﹏╥)"

    # Chama a animação apenas se o texto for realmente mudar
    if new_text != current_text:
        animate_text(card_text, new_text)


def play_music():
    # Inicializa o mixer do pygame
    pygame.mixer.init()
    # Carrega a música
    pygame.mixer.music.load("assets/theme - quem eh mais prop.mp3")
    pygame.mixer.music.set_volume(0.2)
    # Reproduz a música
    pygame.mixer.music.play(loops=-1)
    
def pause_music(music_button):
    if pygame.mixer.music.get_busy():  # Verifica se a música está tocando
        pygame.mixer.music.pause()
        music_button.config(text="🔇")  # Altera o texto do botão
    else:
        pygame.mixer.music.unpause()
        music_button.config(text="🔊")  # Altera o texto do botão

    
    