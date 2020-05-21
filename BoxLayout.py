#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 21:30
# @Author  : Murray
# @File    : BoxLayout.py
# @Software: win10 python3.6.3
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        okBtn = QPushButton('OK')
        cancelBtn = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okBtn)
        hbox.addWidget(cancelBtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Buttons')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
