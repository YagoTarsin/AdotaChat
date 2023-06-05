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

        #self.background_label = QLabel(self)
        #self.background_label.setGeometry(0, 0, 1000, 800)
        #pixmap = QPixmap('imagens/fundo.png')
        #self.background_label.setPixmap(pixmap)
        #self.background_label.setScaledContents(True)

        self.menu()


        invisible_button = QPushButton(self)
        invisible_button.setStyleSheet("background-color: transparent; border: 1px solid #000000")
        invisible_button.setGeometry(0, 35, 1000, 300)
        invisible_button.setCursor(Qt.PointingHandCursor)  # cursor vira mãozinha
        invisible_button.setAutoFillBackground(True)  # luz botão
        invisible_button.clicked.connect(self.buttonClicked)
        button_icon = QIcon('imagens/cachorro.png')
        invisible_button.setIcon(button_icon)
        invisible_button.setIconSize(invisible_button.size())  # ajustar o tamanho do ícone

        invisible_button2 = QPushButton(self)
        invisible_button2.setStyleSheet("background-color: transparent")
        invisible_button2.setGeometry(0, 336, 1000, 300)
        invisible_button2.setCursor(Qt.PointingHandCursor)  # cursor vira mãozinha
        invisible_button2.setAutoFillBackground(True)   # luz botão
        invisible_button2.clicked.connect(self.buttonClicked)
        button_icon2 = QIcon('imagens/Gatos.png')
        invisible_button2.setIcon(button_icon2)
        invisible_button2.setIconSize(invisible_button2.size())  # ajustar o tamanho do ícone

        self.show()

    def menu(self):
        barra_menu = self.menuBar()
        barra_menu.setStyleSheet("background-color: #202123;"
                                 "color: white;"
                                 "font-size: 20px")

        menu_arquivo = barra_menu.addMenu('⚙')

        Gera_Exce = QAction('Remover um pet', self)
        Gera_Exce.triggered.connect(self.teste)
        menu_arquivo.addAction(Gera_Exce)

    def teste(self):
        pass

    def buttonClicked(self):
        print("Botão invisível clicado!")

if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    app.exec()
