from PIL import Image, ImageTk, ImageDraw

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

