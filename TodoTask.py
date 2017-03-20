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

        closebtn = QPushButton('Close', self)
        enterbtn = QPushButton('Enter', self)

        title = QLabel('填写任务')

        titleEditename = QLabel('主题')
        titleEdit = QLineEdit()
        ttbox = QHBoxLayout()
        ttbox.addWidget(titleEditename)
        ttbox.addWidget(titleEdit)

        eebox = QHBoxLayout()
        egEditname = QLabel('简介')
        egEdit = QLineEdit()
        eebox.addWidget(egEditname)
        eebox.addWidget(egEdit)

        cebox = QHBoxLayout()
        contentEditname = QLabel('内容')
        contentEdit = QTextEdit()
        cebox.addWidget(contentEditname)
        cebox.addWidget(contentEdit)

        btbox = QHBoxLayout()
        btbox.addStretch(1)
        btbox.addWidget(closebtn)
        btbox.addWidget(enterbtn)

        vbox = QVBoxLayout()
        # vbox.addStretch(1)
        vbox.addWidget(title)
        vbox.addLayout(ttbox)
        vbox.addLayout(eebox)
        vbox.addLayout(cebox)
        vbox.addLayout(btbox)

        self.setLayout(vbox)

        enterbtn.clicked.connect(self.saveDoc)

        # 主窗口状态
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('TodoTask')
        self.show()

    # 点击保存时间（未完成）
    def saveDoc(self):

        sender = self.sender()

        with open('test.txt', 'w') as wdoc:
            wdoc.write(sender.text())


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


