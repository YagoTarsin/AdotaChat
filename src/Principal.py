from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QLabel, QComboBox
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt
import FuncoesButtons
import CadastroDePets


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PetMatch 🦴')
        self.setGeometry(100, 100, 969, 760)
        self.setMinimumSize(969, 760)
        self.setMaximumSize(969, 760)

        icone = QIcon('imagens/icone.png')
        self.setWindowIcon(icone)

        fundo_vinho = QColor(80, 0, 0)
        self.setStyleSheet(f"background-color: {fundo_vinho.name()};")

        self.menu()

        cadastro_button = QPushButton(self)
        cadastro_button.setStyleSheet("background-color: transparent")
        cadastro_button.setGeometry(0, 35, 269, 630)
        cadastro_button.clicked.connect(self.ButtonCadastro)
        button_icon = QIcon('imagens/Cadastrar um novo pet.png')
        cadastro_button.setIcon(button_icon)
        cadastro_button.setIconSize(cadastro_button.size())

        caninos_button = QPushButton(self)
        caninos_button.setStyleSheet("background-color: transparent")
        caninos_button.setGeometry(269, 35, 700, 210)
        caninos_button.clicked.connect(self.buttonClicked)
        button_icon = QIcon('imagens/cachorros.png')
        caninos_button.setIcon(button_icon)
        caninos_button.setIconSize(caninos_button.size())

        felinos_button = QPushButton(self)
        felinos_button.setStyleSheet("background-color: transparent")
        felinos_button.setGeometry(269, 245, 700, 210)
        felinos_button.clicked.connect(self.buttonClicked)
        button_icon2 = QIcon('imagens/Gatos.png')
        felinos_button.setIcon(button_icon2)
        felinos_button.setIconSize(felinos_button.size())

        outros_button = QPushButton(self)
        outros_button.setStyleSheet("background-color: transparent")
        outros_button.setGeometry(269, 455, 700, 210)
        outros_button.clicked.connect(self.buttonClicked)
        button_icon3 = QIcon('imagens/Outros.png')
        outros_button.setIcon(button_icon3)
        outros_button.setIconSize(outros_button.size())

        univassouras_button = QPushButton(self)
        univassouras_button.setStyleSheet("background-color: transparent")
        univassouras_button.setGeometry(165, 680, 630, 70)
        univassouras_button.setCursor(Qt.PointingHandCursor)
        univassouras_button.clicked.connect(self.ButtonVassouras)
        button_icon4 = QIcon('imagens/univassouras.png')
        univassouras_button.setIcon(button_icon4)
        univassouras_button.setIconSize(univassouras_button.size())

        self.show()

    def menu(self):
        FuncoesButtons.menu(self)

    def teste(self):
        print('Click')

    def buttonClicked(self):
        self.escolha = QDialog()
        self.escolha.setWindowTitle('Abrir banco')
        self.escolha.setFixedSize(320, 200)

        self.Usuario = QLabel('Escolha o usuario', self.escolha)
        self.Usuario.move(80, 5)
        self.Usuario.setFixedSize(300, 50)
        self.Usuario.setStyleSheet('font-size: 20px')

        self.combobox_usuarios = QComboBox(self.escolha)
        self.combobox_usuarios.move(70, 60)
        self.combobox_usuarios.setFixedWidth(175)
        self.combobox_usuarios.setStyleSheet('font-size: 15px')

        def salvar():
            pass

        self.salvar_button = QPushButton('Salvar', self.escolha)
        self.salvar_button.setGeometry(60, 130, 200, 40)
        self.salvar_button.setStyleSheet('font-size: 15px')
        self.salvar_button.clicked.connect(salvar)


        self.escolha.show()

    def ButtonCadastro(self):
        self.Cadastro = CadastroDePets.TelaCadastro()
        self.Cadastro.show()

    def ButtonVassouras(self):
        FuncoesButtons.AbrirSiteUnivassouras()


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    app.exec()
