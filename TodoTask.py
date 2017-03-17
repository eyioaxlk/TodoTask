#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'yexiao'

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QGridLayout, QPushButton, QMessageBox)
from PyQt5.QtCore import QCoreApplication

class TodoTask(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # 创建关闭按钮
        closebtn = QPushButton('关闭', self)
        closebtn.clicked.connect(QCoreApplication.instance().quit)
        closebtn.move(50, 250)

        # 创建确认按钮
        enterbtn = QPushButton('确定', self)
        enterbtn.move(200, 250)


        # 主窗口状态
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('TodoTask')
        self.show()

    # 关闭窗口事件
    def closeEvent(self, e):

        replay = QMessageBox.question(self, '提示', '确认关闭窗口？',
                                      QMessageBox.Yes|QMessageBox.No,
                                                                   QMessageBox.No)

        if replay == QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = TodoTask()
    sys.exit(app.exec_())


