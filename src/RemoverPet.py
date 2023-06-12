from PyQt5.QtWidgets import QPushButton, QMainWindow, QLabel, QLineEdit, QComboBox
from PyQt5.QtGui import QPixmap, QIcon
from PetMatch.src.Scripts import FuncoesButtons


class TelaRemove(QMainWindow):
    def __init__(self):
        super().__init__()
        self.erro = None
        self.setWindowTitle('Remover Pet ❌')
        self.setGeometry(1100, 100, 600, 300)
        self.setMinimumSize(600, 300)
        self.setMaximumSize(600, 300)

        icone = QIcon('Imagens/icone.png')
        self.setWindowIcon(icone)

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 600, 750)
        pixmap = QPixmap('Imagens/fundo_cadastro.png')
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)
        self.resize(pixmap.width(), pixmap.height())
        self.setStyleSheet("QMainWindow {background: transparent;}")

        self.Dados_Pessoais = QLabel('Preencha os dados', self)
        self.Dados_Pessoais.move(130, 10)
        self.Dados_Pessoais.setFixedSize(400, 50)
        self.Dados_Pessoais.setStyleSheet('font-size: 40px')

        self.email_label = QLabel('Email:', self)
        self.email_label.move(15, 80)
        self.email_label.setStyleSheet('font-size: 20px')

        self.email_edit = QLineEdit(self)
        self.email_edit.move(85, 80)
        self.email_edit.setFixedSize(230, 30)
        self.email_edit.setFixedWidth(200)
        self.email_edit.setStyleSheet('font-size: 15px')

        self.raca_label = QLabel('Raça:', self)
        self.raca_label.move(300, 80)
        self.raca_label.setStyleSheet('font-size: 20px')

        self.raca_edit = QLineEdit(self)
        self.raca_edit.move(365, 80)
        self.raca_edit.setFixedSize(230, 30)
        self.raca_edit.setFixedWidth(200)
        self.raca_edit.setStyleSheet('font-size: 15px')

        self.tipo_label = QLabel('Tipo:', self)
        self.tipo_label.move(180, 140)
        self.tipo_label.setStyleSheet('font-size: 20px')

        self.combobox_tipo = QComboBox(self)
        self.combobox_tipo.move(230, 140)
        self.combobox_tipo.setFixedWidth(175)
        self.combobox_tipo.setStyleSheet('font-size: 15px')
        self.carregar_tipo()

        self.salvar_button = QPushButton('Salvar', self)
        self.salvar_button.setGeometry(200, 200, 200, 50)
        self.salvar_button.setStyleSheet('font-size: 15px')
        self.salvar_button.clicked.connect(self.salvar)

    def salvar(self):
        email = self.email_edit.text()
        raca = self.raca_edit.text()
        Tipo = self.combobox_tipo.currentText()
        if email == '' or raca == '' or Tipo == '':
            self.erro = QLabel('Preencha todos os campos', self)
            self.erro.move(185, 250)
            self.erro.setStyleSheet('font-size: 20px; color: red')
            self.erro.setFixedWidth(400)
            self.erro.show()
        else:
            try:
                self.erro.deleteLater()  # Tratamento
            except:
                pass

            FuncoesButtons.remover_linha_raca(Tipo, email, raca)
            self.email_edit.clear(), self.raca_edit.clear, self.combobox_tipo.setCurrentIndex(0)

    def carregar_tipo(self):
        tipos = ['', 'Caninos', 'Felinos', 'Outros']
        for tipo in range(len(tipos)):
            self.combobox_tipo.addItem(tipos[tipo])