from PyQt5.QtWidgets import QPushButton, QMainWindow, QLabel, QLineEdit, QComboBox
from PyQt5.QtGui import QPixmap, QIcon
import csv
import os
import pandas as pd


class TelaAdcInteressados(QMainWindow):
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

        self.tel_label = QLabel('Tel:', self)
        self.tel_label.move(320, 80)
        self.tel_label.setStyleSheet('font-size: 20px')

        self.tel_edit = QLineEdit(self)
        self.tel_edit.move(365, 80)
        self.tel_edit.setFixedSize(230, 30)
        self.tel_edit.setFixedWidth(200)
        self.tel_edit.setStyleSheet('font-size: 15px')

        self.nome_label = QLabel('Nome:', self)
        self.nome_label.move(15, 140)
        self.nome_label.setStyleSheet('font-size: 20px')

        self.nome_edit = QLineEdit(self)
        self.nome_edit.move(85, 140)
        self.nome_edit.setFixedSize(230, 30)
        self.nome_edit.setFixedWidth(200)
        self.nome_edit.setStyleSheet('font-size: 15px')

        self.tipo_label = QLabel('Tipo:', self)
        self.tipo_label.move(310, 140)
        self.tipo_label.setStyleSheet('font-size: 20px')

        self.combobox_tipo = QComboBox(self)
        self.combobox_tipo.move(365, 140)
        self.combobox_tipo.setFixedWidth(200)
        self.combobox_tipo.setStyleSheet('font-size: 15px')
        self.carregar_tipo()

        self.salvar_button = QPushButton('Salvar', self)
        self.salvar_button.setGeometry(200, 200, 200, 50)
        self.salvar_button.setStyleSheet('font-size: 15px')
        self.salvar_button.clicked.connect(self.salvar)

    def salvar(self):
        email = self.email_edit.text()
        tel = self.tel_edit.text()
        nome = self.nome_edit.text()
        Tipo = self.combobox_tipo.currentText()
        if email == '' or tel == '' or Tipo == '' or nome == '':
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

        self.email_edit.clear(), self.tel_edit.clear(), self.nome_edit.clear(), self.combobox_tipo.setCurrentIndex(0)

        caminho_arquivo = f'Banco/Interessados/Interessados.csv'
        dados = {
            'Nome': nome, 'Telefone': tel, 'Email': email, 'Tipo': Tipo
        }
        with open(f'{caminho_arquivo}', 'a', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.DictWriter(arquivo_csv, fieldnames=dados.keys())
            if arquivo_csv.tell() == 0:
                writer.writeheader()
            writer.writerow(dados)

    def carregar_tipo(self):
        tipos = ['', 'Caninos', 'Felinos', 'Outros']
        for tipo in range(len(tipos)):
            self.combobox_tipo.addItem(tipos[tipo])


