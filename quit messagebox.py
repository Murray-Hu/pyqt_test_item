#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 22:24
# @Author  : Murray
# @File    : quit messagebox.py
# @Software: win10 python3.6.3
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QPushButton
from PyQt5.QtCore import QCoreApplication

class QuitMessage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        btn = QPushButton('close',self)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Quit Message')

    def closeEvent(self,event):#内置的函数，重写
        reply = QMessageBox.question(self,'Message','Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    quitmessage = QuitMessage()
    sys.exit(app.exec_())