from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap, QIcon


class TelaCadastro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cadastro 📋')
        self.setGeometry(1100, 100, 600, 800)
        self.setMinimumSize(600, 800)
        self.setMaximumSize(600, 800)

        icone = QIcon('imagens/icone.png')
        self.setWindowIcon(icone)

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 600, 800)
        pixmap = QPixmap('imagens/fundo_cadastro.png')
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)
        self.resize(pixmap.width(), pixmap.height())
        self.setStyleSheet("QMainWindow {background: transparent;}")

        self.Dados_Pessoais = QLabel('Dados Pessoais', self)
        self.Dados_Pessoais.move(175, 10)
        self.Dados_Pessoais.setFixedSize(300, 50)
        self.Dados_Pessoais.setStyleSheet('font-size: 40px')

        self.nome_label = QLabel('Nome:', self)
        self.nome_label.move(15, 80)
        self.nome_label.setStyleSheet('font-size: 20px')

        self.nome_edit = QLineEdit(self)
        self.nome_edit.move(85, 80)
        self.nome_edit.setFixedSize(230, 30)
        self.nome_edit.setFixedWidth(200)
        self.nome_edit.setStyleSheet('font-size: 15px')

        self.cpf_label = QLabel('CPF:', self)
        self.cpf_label.move(315, 80)
        self.cpf_label.setStyleSheet('font-size: 20px')

        self.cpf_edit = QLineEdit(self)
        self.cpf_edit.move(365, 80)
        self.cpf_edit.setFixedSize(230, 30)
        self.cpf_edit.setFixedWidth(200)
        self.cpf_edit.setStyleSheet('font-size: 15px')

        self.tel_label = QLabel('Tel:', self)
        self.tel_label.move(40, 140)
        self.tel_label.setStyleSheet('font-size: 20px')

        self.tel_edit = QLineEdit(self)
        self.tel_edit.move(85, 140)
        self.tel_edit.setFixedSize(230, 30)
        self.tel_edit.setFixedWidth(200)
        self.tel_edit.setStyleSheet('font-size: 15px')

        self.email_label = QLabel('Email:', self)
        self.email_label.move(305, 140)
        self.email_label.setStyleSheet('font-size: 20px')

        self.email_edit = QLineEdit(self)
        self.email_edit.move(365, 140)
        self.email_edit.setFixedSize(230, 30)
        self.email_edit.setFixedWidth(200)
        self.email_edit.setStyleSheet('font-size: 15px')

        self.email_label = QLabel('Endereço:', self)
        self.email_label.move(15, 200)
        self.email_label.setStyleSheet('font-size: 15px')

        self.email_edit = QLineEdit(self)
        self.email_edit.move(120, 200)
        self.email_edit.setFixedSize(230, 30)
        self.email_edit.setFixedWidth(445)
        self.email_edit.setStyleSheet('font-size: 15px')