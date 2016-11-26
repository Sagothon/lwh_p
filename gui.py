from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QVBoxLayout, QApplication, QGroupBox, QPushButton, QHBoxLayout, QWidget, QLineEdit)
import graph
import networkx as nx


class Window(QWidget):

    def dodaj(self):
        widget = Group()
        self.layout.addWidget(widget)
        self.tab.append(widget)

    def licz(self):
        print(len(self.tab))
        for i in self.tab:
            print(i.ed1.displayText())
            

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.Graph = nx.DiGraph()
        #createGraph(Graph)

        self.tab = []
        self.layout = QVBoxLayout()
        btn_dodaj = QPushButton("Dodaj zdarzenie", self)
        btn_dodaj.clicked.connect(self.dodaj)

        btn_licz = QPushButton("Licz", self)
        btn_licz.clicked.connect(self.licz)

        self.layout.addWidget(btn_dodaj)
        self.layout.addWidget(btn_licz)
        self.setLayout(self.layout)
        self.setWindowTitle("Group Box")
        self.resize(480, 320)

class Group(QGroupBox):

    def __init__(self, parent=None):

        super(Group, self).__init__(parent)
        
        self.initGroup()
        
    def initGroup(self):
        hbox = QHBoxLayout()
        self.ed1 = QLineEdit("dsfdsfd")
        self.ed2 = QLineEdit("fdf")
        self.ed3 = QLineEdit("ddddd")
        hbox.addWidget(self.ed1)
        hbox.addWidget(self.ed2)
        hbox.addWidget(self.ed3)
        self.setLayout(hbox)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())

