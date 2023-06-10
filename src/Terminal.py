from PyQt5.QtWidgets import QApplication, QDialog, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt


class TerminalDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Terminal')
        self.setGeometry(100, 100, 800, 600)

        # Definir fonte
        font = QFont("Consolas", 12)
        self.setFont(font)

        # Definir layout
        layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        self.text_edit.setStyleSheet("QTextEdit { background-color: #1E1E1E; color: #EDEDED; border: none; font-size: 20px}")
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

    def write_to_terminal(self, text):
        self.text_edit.append(text)

