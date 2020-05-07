#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 22:37
# @Author  : Murray
# @File    : tooltip.py
# @Software: win10 python3.6.3
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton
from PyQt5.QtGui import QFont

class Tooltip(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))

        self.setToolTip('This is a <b>QWidget</b> widget')
        self.btn = QPushButton('Button',self)
        self.btn.setToolTip('This is a <b>QPushButton</b> widget')

        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('ToolTips')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tooltip = Tooltip()
    sys.exit(app.exec_())

