import sys
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QToolBar, QStatusBar, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
    
        layout = QVBoxLayout()
        widgets = [QToolBar, QTabWidget, QWebEngineView, QStatusBar]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
