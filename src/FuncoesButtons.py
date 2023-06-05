import webbrowser
from PyQt5.QtWidgets import QAction

def AbrirSiteUnivassouras():
    webbrowser.open('https://universidadedevassouras.edu.br/')


def menu(self):
    barra_menu = self.menuBar()
    barra_menu.setStyleSheet("background-color: #202123;"
                             "color: white;"
                             "font-size: 20px")

    menu_configuracoes = barra_menu.addMenu('⚙ Configurações')

    Perfil = QAction('👥 Perfil', self)
    Perfil.triggered.connect(self.teste)
    menu_configuracoes.addAction(Perfil)

    Discord = QAction('🤖 Discord', self)
    Discord.triggered.connect(self.teste)
    menu_configuracoes.addAction(Discord)

    Arquivo  = barra_menu.addMenu('📁 Arquivo')

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