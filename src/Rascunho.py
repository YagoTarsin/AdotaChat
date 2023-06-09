import csv
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt5.QtGui import QIcon


# ----------------------------------------------------------------------------------------------------------------------


class MostrarCaninos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Estoque')
        self.setGeometry(1200, 100, 500, 750)
        self.setMinimumSize(440, 750)

        icone = QIcon('Imagens/icone.png')
        self.setWindowIcon(icone)

        self.table = QTableWidget()  # cria tabela
        self.table.setColumnCount(11)  # tabela com 3 colunas

        Conteudo = [
                'Nome',
                'CPF',
                'Telefone',
                'Email',
                'Endereço',
                'Raça',
                'Tipo',
                'Idade',
                'Vacina',
                'Situação',
                'Porte'
            ]

        self.table.setHorizontalHeaderLabels(Conteudo)

        with open('Banco/Caninos/', newline='', encoding='UTF-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for linha in reader:
                self.table.insertRow(self.table.rowCount())
                for i, field in enumerate(linha):
                    if linha == [Conteudo]:
                        pass
                    else:
                        item = QTableWidgetItem(field)
                        self.table.setItem(self.table.rowCount() - 1, i, item)
        self.setCentralWidget(self.table)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
