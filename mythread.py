# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gameUi.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
import re
import os
import time
from queue import Queue
import threading

indexNumber = ""
counter = ""
money = ""
bet = ""


class Ui_Dialog(object):
    start = True
    gameBool = True
    indexNumber = 0
    counter = 0
    url = ""

    firstTime = True

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.textEdit = QtWidgets.QLineEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 361, 31))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 60, 261, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 110, 91, 61))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(300, 190, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(350, 190, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 220, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(350, 220, 60, 16))
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 70, 51, 25))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 75, 60, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "开始"))
        self.pushButton.clicked.connect(lambda: self.startPlay())
        self.label.setText(_translate("Dialog", "余额"))
        self.label_2.setText(_translate("Dialog", "0"))
        self.label_3.setText(_translate("Dialog", "流水"))
        self.label_4.setText(_translate("Dialog", "0"))
        self.textEdit_2.setText(_translate("Dialog", "0.2"))
        self.label_5.setText(_translate("Dialog", "下注"))

    def startPlay(self):
        if self.start is True:
            print(self.url)
            self.start = False
            self.gameBool = True
            self.pushButton.setText("关闭")
            if self.textEdit.text() is "":
                self.textBrowser.insertPlainText("第一行为空，请添加curl\n")
                cursor = self.textBrowser.textCursor()
                self.textBrowser.moveCursor(cursor.End)
                return

            if self.textEdit_2.text() is "":
                self.textBrowser.insertPlainText("下注金额为空，请输入金额\n")
                cursor = self.textBrowser.textCursor()
                self.textBrowser.moveCursor(cursor.End)
                return

            if self.firstTime:
                self.url = self.textEdit.text()

            printThread = threading.Thread(target=self.gameStart)
            printThread.start()

        else:
            self.pushButton.setText("开始")
            self.start = True
            self.gameBool = False
            self.firstTime = False


    def gameStart(self):
        try:
            print(self.url)
            self.indexNumber = int(self.url.split("&index=")[1].split("&counter=")[0]) + 1
            self.counter = int(self.url.split("&counter=")[1].split("&repeat=")[0]) + 2

            head = "curl" + self.url.split("curl")[1].split("--data")[0] + "--data "
            pattern = re.compile(r'\d+')

            while self.gameBool:
                data = '\'action=doSpin&symbol=vs1dragon8&c=0.2&l=1&index=' + str(self.indexNumber) + '&counter=' + str(
                    self.counter) + "&repeat=0" \
                       + "&mgckey" + self.url.split("&mgckey")[-1]
                sendUrl = head + data
                self.url = sendUrl
                print("发送" + sendUrl)
                result = os.popen(sendUrl).readlines()

                if result[0].startswith("undefined"):
                    pass

                if result[0].startswith("nomoney="):
                    print("没钱了，请充值\n")
                    self.textBrowser.insertPlainText("没钱了，请充值")
                    cursor = self.textBrowser.textCursor()
                    self.textBrowser.moveCursor(cursor.End)
                    break

                if result == ['unlogged']:
                    print("游戏发生错误")
                    print("请重新输入正确的url")
                    self.textBrowser.insertPlainText("游戏发生错误")
                    self.textBrowser.insertPlainText("请重新输入正确的url")
                    cursor = self.textBrowser.textCursor()
                    self.textBrowser.moveCursor(cursor.End)
                    break

                print(result)
                if result[0].endswith("SystemError"):
                    print("游戏停止，请重新复制url")
                    self.textBrowser.insertPlainText("游戏停止，请重新复制url")
                    cursor = self.textBrowser.textCursor()
                    self.textBrowser.moveCursor(cursor.End)
                    break

                number = pattern.findall(result[0])
                if int(number[0]) == 0:
                    print("没中奖\n")
                    self.textBrowser.insertPlainText("没中奖\n")
                    cursor = self.textBrowser.textCursor()
                    self.textBrowser.moveCursor(cursor.End)

                    self.label_2.setText(result[0].split("&balance=")[1].split("&index=")[0])
                    self.label_4.setText(str(self.indexNumber))

                    self.indexNumber = int(result[0].split("&index=")[1].split("&balance_cash=")[0]) + 1
                    self.counter = int(result[0].split("&counter=")[1].split("&l=")[0]) + 2
                    time.sleep(0.005)
                else:
                    print("中奖了\n")
                    self.textBrowser.insertPlainText("中奖了:" + result[0].split("tw=")[1].split("&balance=")[0] + "\n")
                    cursor = self.textBrowser.textCursor()
                    self.textBrowser.moveCursor(cursor.End)
                    self.indexNumber = int(result[0].split("&index=")[1].split("&balance_cash=")[0]) + 1
                    self.counter = int(result[0].split("&counter=")[1].split("&l=")[0]) + 2
                    data = '\'symbol=vs1dragon8&action=doCollect&index=' + str(self.indexNumber) + '&counter=' + str(
                        self.counter) + "&repeat=0" \
                           + '&mgckey' + self.url.split("&mgckey")[-1]
                    sendUrl = head + data
                    self.url = sendUrl
                    print("发送" + sendUrl)
                    result = os.popen(sendUrl).readlines()

                    self.indexNumber = int(result[0].split("&index=")[1].split("&balance_cash=")[0]) + 1
                    self.counter = int(result[0].split("&counter=")[1].split("&l=")[0]) + 2
        except:
            self.textBrowser.insertPlainText("url错误，请重新粘贴")
            cursor = self.textBrowser.textCursor()
            self.textBrowser.moveCursor(cursor.End)
            print("url错误，请重新粘贴")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_Dialog()  # ui是你创建的ui类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
