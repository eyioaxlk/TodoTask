#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'yexiao'

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QGridLayout, QPushButton, QMessageBox,
                             QHBoxLayout, QVBoxLayout, QLineEdit,
                             QTextEdit, QLabel)
from PyQt5.QtCore import QCoreApplication


class TodoTask(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 增加一个状态栏
        # self.statusBar()

        """
        # 创建关闭按钮
        closebtn = QPushButton('关闭', self)
        closebtn.clicked.connect(QCoreApplication.instance().quit)
        closebtn.move(50, 250)

        # 创建确认按钮
        enterbtn = QPushButton('确定', self)
        enterbtn.move(200, 250)
        """

        self.closebtn = QPushButton('Close', self)
        self.enterbtn = QPushButton('Enter', self)

        self.title = QLabel('填写任务')

        self.titleEditename = QLabel('主题')
        self.titleEdit = QLineEdit()
        ttbox = QHBoxLayout()
        ttbox.addWidget(self.titleEditename)
        ttbox.addWidget(self.titleEdit)

        eebox = QHBoxLayout()
        self.egEditname = QLabel('简介')
        self.egEdit = QLineEdit()
        eebox.addWidget(self.egEditname)
        eebox.addWidget(self.egEdit)

        cebox = QHBoxLayout()
        self.contentEditname = QLabel('内容')
        self.contentEdit = QTextEdit()
        cebox.addWidget(self.contentEditname)
        cebox.addWidget(self.contentEdit)

        btbox = QHBoxLayout()
        btbox.addStretch(1)
        btbox.addWidget(self.closebtn)
        btbox.addWidget(self.enterbtn)

        vbox = QVBoxLayout()
        # vbox.addStretch(1)
        vbox.addWidget(self.title)
        vbox.addLayout(ttbox)
        vbox.addLayout(eebox)
        vbox.addLayout(cebox)
        vbox.addLayout(btbox)

        self.setLayout(vbox)

        self.enterbtn.clicked.connect(self.saveDoc)

        # 主窗口状态
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('TodoTask')
        self.show()

    # 点击保存时间（未完成）
    def saveDoc(self):

        # sender = self.sender()

        with open('/Users/yexiao/Downloads/test.txt', 'w') as wdoc:
            wdoc.write(self.titleEdit.text())


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


