import locale
import sys
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar, QTabWidget, QWidget
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize

locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("ADSB Logger")
        self.setMinimumSize(1024,768)

        toolbar = QToolBar("main")
        self.addToolBar(toolbar)

        actConnect = QAction(QIcon("icons_toolbar\Connect.png"), "Start", self)
        actPause = QAction(QIcon("icons_toolbar\Pause.png"), "Pause", self)
        actSettings = QAction(QIcon("icons_toolbar\Settings.png"), "Settings", self)
        actExit = QAction(QIcon("icons_toolbar\Exit.png"), "Exit", self)
        toolbar.addAction(actConnect)
        toolbar.addAction(actPause)
        toolbar.addAction(actSettings)
        toolbar.addAction(actExit)

        #browser = QWebEngineView(tabs)
        #browser.setHtml(open("Output.html").read())
        # self.setCentralWidget(browser)

        tabs = QTabWidget()
        tabs.setMovable(False)
        # self.tabs.addTab()
        # tabs.addTab("History", "История")
        self.setCentralWidget(tabs)
     

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()