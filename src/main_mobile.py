from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
from kivy.core.audio import SoundLoader
from kivy.config import Config
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import NoTransition


# Configuração para tela cheia
Config.set('graphics', 'window', 'auto')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '660')

# Gerenciador de telas

class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = NoTransition()  # Remove a transição

# Tela principal (Menu)
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Define a cor de fundo da tela
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # Cor de fundo (cinza escuro)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Atualiza o retângulo quando o tamanho da tela mudar
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Layout principal (AnchorLayout para centralizar)
        root = AnchorLayout(anchor_x='center', anchor_y='center')

        # BoxLayout com widgets
        layout = BoxLayout(orientation='vertical', padding=25, spacing=10, size_hint=(0.8, 0.8))

        # Logo
        logo = Image(source='assets/logoSombra.png', size_hint=(1, 0.5))
        layout.add_widget(logo)

        # Botão "Cartas para a Família"
        family_button = Button(
            text="Cartas para a Família",
            size_hint=(1, 0.1),
            background_color=(0.866, 0.866, 0.866, 1), 
            font_name='assets/LT Funk.otf',  # Caminho da fonte
            font_size=21  
        )
        family_button.bind(on_press=self.go_to_family)
        layout.add_widget(family_button)

        # Botão "Cartas para os Amigos"
        friends_button = Button(
            text="Cartas para os Amigos",
            size_hint=(1, 0.1),
            background_color=(0.866, 0.866, 0.866, 1),
            font_name='assets/LT Funk.otf',  # Caminho da fonte
            font_size=21   
        )
        friends_button.bind(on_press=self.go_to_friends)
        layout.add_widget(friends_button)
        
        # Texto no final 
        footer_label = Label(
            text="© Produzido por Ray Del Negro",  # Substitua pelo seu nome
            size_hint=(1, 0.1),
            color=(1, 1, 1, 1),  # Cor do texto (branco)
            font_name='assets/LT Funk.otf',  # Usando a mesma fonte
            font_size=12  # Tamanho da fonte
        )
        layout.add_widget(footer_label)


        # Adiciona o BoxLayout ao AnchorLayout
        root.add_widget(layout)

        # Adiciona o AnchorLayout à tela
        self.add_widget(root)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def go_to_family(self, instance):
        self.manager.current = 'family'

    def go_to_friends(self, instance):
        self.manager.current = 'friends'


# Tela "Cartas para a Família"
class FamilyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Define a cor de fundo da tela
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # Cor de fundo (cinza escuro)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Atualiza o retângulo quando o tamanho da tela mudar
        self.bind(size=self._update_rect, pos=self._update_rect)

        # BoxLayout com widgets
        layout = BoxLayout(orientation='vertical')
        # Cabeçalho
        header_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))

        # Espaço à esquerda para centralizar os itens
        header_layout.add_widget(BoxLayout(size_hint=(0.3, 1)))  # Espaço vazio à esquerda

        # Imagem do cabeçalho
        logo = Image(source='assets/familiaSombra.png', size_hint=(0.35, 1))
        header_layout.add_widget(logo)

        # Texto do cabeçalho
        header_label = Label(
            text="Modo\nFamília",
            font_name='assets/LT Funk.otf',
            font_size=24,
            color=(1, 1, 1, 1),  # Cor do texto (branco)
            size_hint=(0.7, 1),
            halign='center',  # Centraliza o texto horizontalmente
            valign='middle'   # Centraliza o texto verticalmente
        )
        header_layout.add_widget(header_label)

        # Espaço à direita para centralizar os itens
        header_layout.add_widget(BoxLayout(size_hint=(0.1, 1)))  # Espaço vazio à direita

        layout.add_widget(header_layout)
        
    
        # Cria o card
        card = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 200), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Configuração do fundo do card
        with card.canvas.before:
            Color(0.973, 0.973, 0.973, 1)  # Cor de fundo #f8f9fa
            card.rect = Rectangle(size=card.size, pos=card.pos)

        # Atualiza o retângulo quando o tamanho ou posição muda
        def update_rect(instance, value):
            card.rect.pos = card.pos
            card.rect.size = card.size

        card.bind(pos=update_rect, size=update_rect)

        # Espaço vazio à esquerda (opcional)
        card.add_widget(BoxLayout(size_hint=(0.01, 1)))  # Espaço vazio à esquerda

        # Texto do cartão
        card_text = Label(
            text="Quem é mais provável de aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            font_size=12,
            font_name='Georgia',
            size_hint=(1, 1),  # Ocupa todo o espaço disponível no card
            halign='center',   # Centraliza o texto horizontalmente
            valign='middle',   # Centraliza o texto verticalmente
            color=(0, 0, 0, 1)  # Cor do texto: preto (RGBA)
        )
        card_text.bind(size=card_text.setter('text_size'))  # Ajusta o tamanho do texto
        card.add_widget(card_text)
        
        # Adiciona o card ao layout principal
        layout.add_widget(card)
        
        prox_card = BoxLayout(orientation='vertical', padding=20, spacing=50, size_hint=(None, None), size=(200, 200), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        # Botão "Cartas para os Amigos"
        friends_button = Button(
            text="Cartas para os Amigos",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.866, 0.866, 0.866, 1),
            font_name='assets/LT Funk.otf',  # Caminho da fonte
            font_size=21   
        )
        prox_card.add_widget(friends_button)
        
        voltar = Button(text="Voltar",  size_hint=(None, None), size=(200, 50),)
        voltar.bind(on_press=self.go_back)
        prox_card.add_widget(voltar)
        
        layout.add_widget(prox_card)
        
    
        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def go_back(self, instance):
        self.manager.current = 'main'

# Tela "Cartas para os Amigos"
class FriendsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Define a cor de fundo da tela
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # Cor de fundo (cinza escuro)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Atualiza o retângulo quando o tamanho da tela mudar
        self.bind(size=self._update_rect, pos=self._update_rect)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Cartas para os Amigos"))
        back_button = Button(text="Voltar", size_hint=(1, 0.1))
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def go_back(self, instance):
        self.manager.current = 'main'

# Aplicativo principal
class QuemEMaisProvavelApp(App):
    def build(self):
        sm = ScreenManagement()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(FamilyScreen(name='family'))
        sm.add_widget(FriendsScreen(name='friends'))
        return sm

if __name__ == '__main__':
    QuemEMaisProvavelApp().run()