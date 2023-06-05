from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PetMatch 🦴')
        self.setGeometry(100, 100, 1000, 800)
        self.setMinimumSize(1000, 800)
        self.setMaximumSize(1000, 800)

        icone = QIcon('imagens/icone.png')
        self.setWindowIcon(icone)

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 1000, 800)
        pixmap = QPixmap('imagens/fundo.png')
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

        self.menu()


        invisible_button = QPushButton(self)
        invisible_button.setStyleSheet("background-color: transparent; border: 1px solid #000000")
        invisible_button.setGeometry(300, 170, 700, 210)
        invisible_button.setCursor(Qt.PointingHandCursor)  # cursor vira mãozinha
        invisible_button.setAutoFillBackground(True)  # luz botão
        invisible_button.clicked.connect(self.buttonClicked)
        button_icon = QIcon('imagens/cachorro.png')
        invisible_button.setIcon(button_icon)
        invisible_button.setIconSize(invisible_button.size())  # ajustar o tamanho do ícone

        invisible_button2 = QPushButton(self)
        invisible_button2.setStyleSheet("background-color: transparent")
        invisible_button2.setGeometry(300, 380, 700, 210)
        invisible_button2.setCursor(Qt.PointingHandCursor)  # cursor vira mãozinha
        invisible_button2.setAutoFillBackground(True)   # luz botão
        invisible_button2.clicked.connect(self.buttonClicked)
        button_icon2 = QIcon('imagens/Gatos.png')
        invisible_button2.setIcon(button_icon2)
        invisible_button2.setIconSize(invisible_button2.size())  # ajustar o tamanho do ícone

        invisible_button3 = QPushButton(self)
        invisible_button3.setStyleSheet("background-color: transparent")
        invisible_button3.setGeometry(300, 590, 700, 210)
        invisible_button3.setCursor(Qt.PointingHandCursor)  # cursor vira mãozinha
        invisible_button3.setAutoFillBackground(True)  # luz botão
        invisible_button3.clicked.connect(self.buttonClicked)
        button_icon3 = QIcon('imagens/Outros.png')
        invisible_button3.setIcon(button_icon3)
        invisible_button3.setIconSize(invisible_button3.size())  # ajustar o tamanho do ícone3
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
        Perfil.triggered.connect(self.teste)
        Arquivo.addAction(meus_pets)

        Pets = barra_menu.addMenu('🐾 Pets')

        cachorro = QAction('🐕 Sobre os cães', self)
        Perfil.triggered.connect(self.teste)
        Pets.addAction(cachorro)

        gatos = QAction('🐈 Sobre os gatos', self)
        Perfil.triggered.connect(self.teste)
        Pets.addAction(gatos)


    def teste(self):
        pass

    def buttonClicked(self):
        print("Botao clicado")


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    app.exec()
