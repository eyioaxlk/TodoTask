#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'yexiao'

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QGridLayout, QPushButton, QMessageBox,
                             QHBoxLayout, QVBoxLayout, QLineEdit,
                             QTextEdit, QLabel)
from PyQt5.QtCore import QCoreApplication
from email.mime.text import MIMEText
from email.header import Header
import smtplib


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

        # self.title = QLabel('填写任务')

        # 邮箱行排版
        self.titleEditename = QLabel('邮箱')
        self.titleEdit = QLineEdit()
        ttbox = QHBoxLayout()
        ttbox.addWidget(self.titleEditename)
        ttbox.addWidget(self.titleEdit)

        # 主题行排版
        eebox = QHBoxLayout()
        self.egEditname = QLabel('主题')
        self.egEdit = QLineEdit()
        eebox.addWidget(self.egEditname)
        eebox.addWidget(self.egEdit)

        # 内容行排版
        cebox = QHBoxLayout()
        self.contentEditname = QLabel('内容')
        self.contentEdit = QTextEdit()
        cebox.addWidget(self.contentEditname)
        cebox.addWidget(self.contentEdit)

        # 按钮行排版
        btbox = QHBoxLayout()
        btbox.addStretch(1)
        btbox.addWidget(self.closebtn)
        btbox.addWidget(self.enterbtn)

        # 垂直排版
        vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addWidget(self.title)
        vbox.addLayout(ttbox)
        vbox.addLayout(eebox)
        vbox.addLayout(cebox)
        vbox.addLayout(btbox)

        # 设置排版
        self.setLayout(vbox)

        # 点击事件
        self.enterbtn.clicked.connect(self.sentEmail())

        # 窗口设置
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('TodoTask')
        self.show()

    """
    # 保存到本地txt文件夹
    def saveDoc(self):

        # sender = self.sender()

        with open('/Users/yexiao/Downloads/test.txt', 'w') as wdoc:
            wdoc.write(self.titleEdit.text()+'\n')
            wdoc.write(self.egEdit.text()+'\n')
            wdoc.write(self.contentEdit.toPlainText())
    """

    # 发送邮件到
    def sentEmail(self):

        from_email = 'eyioax@sina.com'
        from_ps = '**********'
        stmp_mail = 'smtp.sina.com'

        target_email = self.titleEdit.text()

        message = MIMEText(self.contentEdit.toPlainText(), 'plain', 'utf-8')
        message['From'] = Header('测试发件人', 'utf-8')
        message['To'] = Header('收件人','utf-8')
        message['Subject'] = Header('测试邮件', 'utf-8')

        server = smtplib.SMTP(stmp_mail, 25)
        # server.set_debuglevel(1)
        server.login(from_email, from_ps)
        server.sendmail(from_email, [target_email], message.as_string())
        server.quit()

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


