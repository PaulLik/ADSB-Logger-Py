from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QIcon, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ADSB Logger")
        self.setGeometry(200,200, 500, 600)
        
        button = QPushButton("Start")

        exitAct = QAction(QIcon("Out180.png"),"Exit",self)
        toolbar = self.addToolBar("Exit")
        toolbar.addAction(exitAct)

app = QApplication([])

window=MainWindow()
window.show()

app.exec()
