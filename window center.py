#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 17:25
# @Author  : Murray
# @File    : window center.py
# @Software: win10 python3.6.3
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget

class WindowCenter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.resize(300,300)
        self.Center()
        self.setWindowTitle('Window Center')

    def Center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = WindowCenter()
    sys.exit(app.exec_())
