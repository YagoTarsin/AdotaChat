from PyQt5.QtWidgets import QPushButton, QMainWindow, QLabel, QLineEdit, QComboBox
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

        self.endereco_label = QLabel('Endereço:', self)
        self.endereco_label.move(15, 200)
        self.endereco_label.setStyleSheet('font-size: 20px')

        self.endereco_edit = QLineEdit(self)
        self.endereco_edit.move(120, 200)
        self.endereco_edit.setFixedSize(230, 30)
        self.endereco_edit.setFixedWidth(445)
        self.endereco_edit.setStyleSheet('font-size: 15px')
# ----------------------------------------------------------------------------------------------------------------------
        self.Dados_pets = QLabel('Dados do Pet', self)
        self.Dados_pets.move(175, 260)
        self.Dados_pets.setFixedSize(300, 50)
        self.Dados_pets.setStyleSheet('font-size: 40px')

        self.tipo_label = QLabel('Tipo:', self)
        self.tipo_label.move(35, 330)
        self.tipo_label.setStyleSheet('font-size: 20px')

        self.combobox_tipo = QComboBox(self)
        self.combobox_tipo.move(100, 330)
        self.combobox_tipo.setFixedWidth(175)
        self.combobox_tipo.setStyleSheet('font-size: 15px')
        self.carregar_tipo()

        self.raca_label = QLabel('Raça:', self)
        self.raca_label.move(305, 330)
        self.raca_label.setStyleSheet('font-size: 20px')

        self.raca_edit = QLineEdit(self)
        self.raca_edit.move(365, 330)
        self.raca_edit.setFixedSize(230, 30)
        self.raca_edit.setFixedWidth(200)
        self.raca_edit.setStyleSheet('font-size: 15px')

        self.idade_label = QLabel('Idade:', self)
        self.idade_label.move(35, 400)
        self.idade_label.setStyleSheet('font-size: 20px')

        self.combobox_idade = QComboBox(self)
        self.combobox_idade.move(100, 400)
        self.combobox_idade.setFixedWidth(175)
        self.combobox_idade.setStyleSheet('font-size: 15px')
        self.carregar_idade()

        self.vacina_label = QLabel('Vacina:', self)
        self.vacina_label.move(290, 400)
        self.vacina_label.setStyleSheet('font-size: 20px')

        self.combobox_vacina = QComboBox(self)
        self.combobox_vacina.move(365, 400)
        self.combobox_vacina.setFixedWidth(200)
        self.combobox_vacina.setStyleSheet('font-size: 15px')
        self.carregar_vacina()

        self.situacao_label = QLabel('Situação:', self)
        self.situacao_label.move(7, 470)
        self.situacao_label.setStyleSheet('font-size: 20px')

        self.combobox_situacao = QComboBox(self)
        self.combobox_situacao.move(100, 470)
        self.combobox_situacao.setFixedWidth(175)
        self.combobox_situacao.setStyleSheet('font-size: 15px')
        self.carregar_situacao()

        self.porte_label = QLabel('Porte:', self)
        self.porte_label.move(300, 470)
        self.porte_label.setStyleSheet('font-size: 20px')

        self.combobox_porte = QComboBox(self)
        self.combobox_porte.move(365, 470)
        self.combobox_porte.setFixedWidth(200)
        self.combobox_porte.setStyleSheet('font-size: 15px')
        self.carregar_porte()

        self.salvar_button = QPushButton('Salvar', self)
        self.salvar_button.setGeometry(200, 550, 200, 50)
        self.salvar_button.setStyleSheet('font-size: 15px')
        self.salvar_button.clicked.connect(self.salvar)

    def salvar(self):
        print('botão clicado')

    def carregar_tipo(self):
        tipos = ['', 'Caninos', 'Felinos', 'Outros']
        for tipo in range(len(tipos)):
            self.combobox_tipo.addItem(tipos[tipo])

    def carregar_idade(self):
        tipos = ['', 'Não informado']
        for c in range(0, 21):
            tipos.append(str(c))
        for tipo in range(len(tipos)):
            self.combobox_idade.addItem(tipos[tipo])

    def carregar_vacina(self):
        tipos = ['', 'Não informado', 'Em dia', 'Ausente']
        for tipo in range(len(tipos)):
            self.combobox_vacina.addItem(tipos[tipo])

    def carregar_situacao(self):
        tipos = ['', 'Adoção', 'Doação']
        for tipo in range(len(tipos)):
            self.combobox_situacao.addItem(tipos[tipo])

    def carregar_porte(self):
        tipos = ['', 'Pequeno', 'Médio', 'Grande']
        for tipo in range(len(tipos)):
            self.combobox_porte.addItem(tipos[tipo])