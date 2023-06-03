from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction
from PyQt5.QtGui import QPixmap


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


if __name__ == '__main__':
    app = QApplication([])
    Tela = App()
    app.exec_()