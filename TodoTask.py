#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'yexiao'

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QGridLayout, QPushButton, QMessageBox,
                             QHBoxLayout, QVBoxLayout, QLineEdit,
                             QTextEdit, QLabel, QComboBox, QCalendarWidget)
from PyQt5.QtCore import QCoreApplication
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import sqlite3
from datetime import datetime

# Create TodoTask Database
conn = sqlite3.connect('tdk.db')
cursor = conn.cursor()

# Create Tasklist Table

cursor.execute('drop table if EXISTS task_list')
cursor.execute('create table if not exists task_list (`id` INTEGER PRIMARY KEY autoincrement,`task_type` int,'
               '`task_name` varchar(50),`task_point` decimal(10,2), `task_status` int, '
               '`create_date` date,`end_date` date)')


cursor.close()
conn.commit()
conn.close()



class TodoTask(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Choice TaskType
        line1 = QHBoxLayout()
        self.tasktype_name = QLabel('任务类型')
        self.tasktype = QComboBox()
        tasktype_list = ['Choice', 'Python', 'English', 'Support', 'Financial', 'Design', 'Read', 'Travel', 'Write']
        for eachtype in tasktype_list:
            self.tasktype.addItem(eachtype)
        line1.addWidget(self.tasktype_name)
        line1.addWidget(self.tasktype)


        # Task detail
        line2 = QHBoxLayout()
        self.taskdetail_name = QLabel('任务描述')
        self.taskdetail = QTextEdit()
        line2.addWidget(self.taskdetail_name)
        line2.addWidget(self.taskdetail)


        # Task point
        line3 = QHBoxLayout()
        self.taskpoint_name = QLabel('任务积分')
        self.taskpoint = QLineEdit()
        line3.addWidget(self.taskpoint_name)
        line3.addWidget(self.taskpoint)


        # Create date
        line4 = QHBoxLayout()
        self.createdate_name = QLabel('创建时间')
        # self.createdate = QCalendarWidget(self)
        self.createdate = QLineEdit()
        self.createdate.setPlaceholderText(str(datetime.now().date()))
        line4.addWidget(self.createdate_name)
        line4.addWidget(self.createdate)

        # Create button
        line5 = QHBoxLayout()
        self.insertbtn = QPushButton('添加任务', self)
        line5.addWidget(self.insertbtn)


        # Vertical layout
        vbox = QVBoxLayout()
        vbox.addLayout(line1)
        vbox.addLayout(line2)
        vbox.addLayout(line3)
        vbox.addLayout(line4)
        vbox.addLayout(line5)


        # Set layout
        self.setLayout(vbox)

        # 点击事件
        self.insertbtn.clicked.connect(self.insertTable)

        # 窗口设置
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('TodoTask')
        self.show()

    # Insert into task_list table
    def insertTable(self):

        data_list = [int(self.tasktype.currentIndex()), self.taskdetail.toPlainText(),
                     int(self.taskpoint.text()), 1, self.createdate.text(), '']

        print(data_list)

        conn = sqlite3.connect('tdk.db')
        cursor = conn.cursor()

        cursor.execute('insert into task_list (task_type,task_name,task_point,task_status,create_date,end_date) '
                       'values(?, ?, ?, ?, ?, ?)', tuple(data_list))
        cursor.close()
        conn.commit()
        conn.close()

        """
        print()
        """


    """
    # 保存到本地txt文件夹
    def saveDoc(self):

        # sender = self.sender()

        with open('/Users/yexiao/Downloads/test.txt', 'w') as wdoc:
            wdoc.write(self.titleEdit.text()+'\n')
            wdoc.write(self.egEdit.text()+'\n')
            wdoc.write(self.contentEdit.toPlainText())
    """

    """
    # 发送邮件到
    def sentEmail(self):

        from_email = 'eyioax@sina.com'
        from_ps = '93KZAXi37L8tjWnM'
        stmp_mail = 'smtp.sina.com'

        target_email = [self.titleEdit.text()]

        message = MIMEText(self.contentEdit.toPlainText(), 'plain', 'utf-8')
        message['From'] = Header('测试发件人', 'utf-8')
        message['To'] = Header('收件人','utf-8')
        message['Subject'] = Header('测试邮件', 'utf-8')

        server = smtplib.SMTP(stmp_mail, 25)
        # server.set_debuglevel(1)
        server.login(from_email, from_ps)
        server.sendmail(from_email, target_email, message.as_string())
        server.quit()
    """


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


