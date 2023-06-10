import sys
import markdown2
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView


class ReadmeViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Readme Viewer')
        self.setGeometry(100, 100, 800, 600)

        self.webview = QWebEngineView()
        self.setCentralWidget(self.webview)

        self.load_readme('README.md')

    def load_readme(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
            html_content = markdown2.markdown(markdown_content)
            self.webview.setHtml(html_content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ReadmeViewer()
    viewer.show()
    sys.exit(app.exec_())
