from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtCore import QSize

class BirthdayTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Birthday Tracker")
        self.setMinimumSize(QSize(300,200))

        display_tab = QWidget()
        insert_tab = QWidget()

        tab_control = QTabWidget()
        tad_control.addtab("Display")
        tab_control.addTab("Insert")

        self.setCentralWidget(tab_control)


app = QApplication()

win = BirthdayTracker()
win.show()

app.exec()