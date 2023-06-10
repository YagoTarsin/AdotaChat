import webbrowser
import os
import Terminal
import pandas as pd
from PyQt5.QtWidgets import QAction, QApplication


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


def pesquisa_binaria(pilha, valor):
    esquerda = 0
    direita = len(pilha) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if pilha[meio]["Raça"] == valor:
            return meio
        elif pilha[meio]["Raça"] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1


def mostrar_racas(Pasta, raca):
    pasta = f"Banco/{Pasta}"
    arquivos = os.listdir(pasta)
    pilha = []
    for arquivo in arquivos:
        if arquivo.endswith(".csv"):
            arquivo_path = os.path.join(pasta, arquivo)
            df = pd.read_csv(arquivo_path)
            registros_filtrados = df[df["Raça"] == raca].to_dict("records")
            pilha.extend(registros_filtrados)
    # Ordena a pilha pelo nome do animal
    pilha.sort(key=lambda x: x["Nome"])

    # Realiza a pesquisa binária para encontrar a raça
    indice_raca = pesquisa_binaria(pilha, raca)

    terminal_dialog = Terminal.TerminalDialog()
    if indice_raca != -1:
        for registro in pilha:
            for coluna, valor in registro.items():
                terminal_dialog.write_to_terminal(f"{coluna}: {valor}")
            terminal_dialog.write_to_terminal("-" * 20)
    terminal_dialog.exec_()

