from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QLabel
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PetMatch 🦴')
        self.setGeometry(100, 100, 969, 800)
        self.setMinimumSize(969, 800)
        self.setMaximumSize(969, 800)

        # Define a cor vinho
        fundo_vinho = QColor(80, 0, 0)

        # Aplica a cor vinho como fundo usando CSS
        self.setStyleSheet(f"background-color: {fundo_vinho.name()};")

        icone = QIcon('imagens/icone.png')
        self.setWindowIcon(icone)

        self.menu()

        cadastro_button = QPushButton(self)
        cadastro_button.setStyleSheet("background-color: transparent; border: 1px solid #000000")
        cadastro_button.setGeometry(0, 35, 269, 630)
        cadastro_button.setCursor(Qt.PointingHandCursor)  # cursor vira mãozinha
        cadastro_button.setAutoFillBackground(True)  # luz botão
        cadastro_button.clicked.connect(self.buttonClicked)
        button_icon = QIcon('imagens/Cadastrar um novo pet.png')
        cadastro_button.setIcon(button_icon)
        cadastro_button.setIconSize(cadastro_button.size())  # ajustar o tamanho do ícone


        caninos_button = QPushButton(self)
        caninos_button.setStyleSheet("background-color: transparent; border: 1px solid #000000")
        caninos_button.setGeometry(269, 35, 700, 210)
        caninos_button.setCursor(Qt.PointingHandCursor)  # cursor vira mãozinha
        caninos_button.setAutoFillBackground(True)  # luz botão
        caninos_button.clicked.connect(self.buttonClicked)
        button_icon = QIcon('imagens/cachorro.png')
        caninos_button.setIcon(button_icon)
        caninos_button.setIconSize(caninos_button.size())  # ajustar o tamanho do ícone

        felinos_button = QPushButton(self)
        felinos_button.setStyleSheet("background-color: transparent")
        felinos_button.setGeometry(269, 245, 700, 210)
        felinos_button.setCursor(Qt.PointingHandCursor)  # cursor vira mãozinha
        felinos_button.setAutoFillBackground(True)   # luz botão
        felinos_button.clicked.connect(self.buttonClicked)
        button_icon2 = QIcon('imagens/Gatos.png')
        felinos_button.setIcon(button_icon2)
        felinos_button.setIconSize(felinos_button.size())  # ajustar o tamanho do ícone

        outros_button = QPushButton(self)
        outros_button.setStyleSheet("background-color: transparent")
        outros_button.setGeometry(269, 455, 700, 210)
        outros_button.setCursor(Qt.PointingHandCursor)  # cursor vira mãozinha
        outros_button.setAutoFillBackground(True)  # luz botão
        outros_button.clicked.connect(self.buttonClicked)
        button_icon3 = QIcon('imagens/Outros.png')
        outros_button.setIcon(button_icon3)
        outros_button.setIconSize(outros_button.size())  # ajustar o tamanho do ícone3

        univassouras_button = QPushButton(self)
        univassouras_button.setStyleSheet("background-color: transparent")
        univassouras_button.setGeometry(5, 670, 964, 130)
        univassouras_button.setCursor(Qt.PointingHandCursor)  # cursor vira mãozinha
        univassouras_button.setAutoFillBackground(True)  # luz botão
        univassouras_button.clicked.connect(self.buttonClicked)
        button_icon4 = QIcon('imagens/univassouras.png')
        univassouras_button.setIcon(button_icon4)
        univassouras_button.setIconSize(univassouras_button.size())  # ajustar o tamanho do ícone3

        self.show()

    def menu(self):
        barra_menu = self.menuBar()
        barra_menu.setStyleSheet("background-color: #202123;"
                                 "color: white;"
                                 "font-size: 20px")

        menu_configuracoes = barra_menu.addMenu('⚙ Configurações')

        Perfil = QAction('👥 Perfil', self)
        Perfil.triggered.connect(self.teste)
        menu_configuracoes.addAction(Perfil)

        Discord = QAction('🤖 Discord', self)
        Discord.triggered.connect(self.teste)
        menu_configuracoes.addAction(Discord)

        Arquivo  = barra_menu.addMenu('📁 Arquivo')

        meus_pets = QAction('❤ Meus pets', self)
        meus_pets.triggered.connect(self.teste)
        Arquivo.addAction(meus_pets)

        Pets = barra_menu.addMenu('🐾 Pets')

        cachorro = QAction('🐕 Sobre os cães', self)
        cachorro.triggered.connect(self.teste)
        Pets.addAction(cachorro)

        gatos = QAction('🐈 Sobre os gatos', self)
        gatos.triggered.connect(self.teste)
        Pets.addAction(gatos)


    def teste(self):
        print('Click')

    def buttonClicked(self):
        print("Botao clicado")


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    app.exec()
