import webbrowser
import os
import csv
from PyQt5.QtWidgets import QAction


def AbrirSiteUnivassouras():
    webbrowser.open('https://universidadedevassouras.edu.br/')


def menu(self):
    barra_menu = self.menuBar()
    barra_menu.setStyleSheet("background-color: black;"
                             "color: white;"
                             "font-size: 20px")

    menu_configuracoes = barra_menu.addMenu('⚙ Configurações')

    Perfil = QAction('👥 Perfil', self)
    Perfil.triggered.connect(self.teste)
    menu_configuracoes.addAction(Perfil)

    Discord = QAction('🤖 Discord', self)
    Discord.triggered.connect(self.teste)
    menu_configuracoes.addAction(Discord)

    Arquivo = barra_menu.addMenu('📁 Arquivo')

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


def LerBanco(tipo):
    pasta = f"Banco/{tipo}"
    coluna_alvo = "Nome"
    arquivos = os.listdir(pasta)
    pilha_valores = []

    for arquivo in arquivos:
        if arquivo.endswith(".csv"):
            with open(os.path.join(pasta, arquivo), 'r') as f:
                reader = csv.DictReader(f)

                # Obtém os valores da coluna alvo e adiciona à pilha
                for row in reader:
                    valor = row[coluna_alvo]
                    pilha_valores.append(valor)

    # Imprime os valores da coluna alvo (desempilhando)
    tipos = ['']
    while not len(pilha_valores) == 0:
        valor = pilha_valores.pop()
        for c in range(0, 21):
            tipos.append(str(valor))

