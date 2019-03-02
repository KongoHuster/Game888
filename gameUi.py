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
            printQueue = Queue(maxsize=1000)
            self.start = False
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

            url = self.textEdit.text()
            # print(url)
            # if before = url.split("&c=")[0] is "":
            #     before = url.split("&c=")[0]
            #
            # after = url.split("&l=1")[1]
            # print(before)
            # print(after)
            # urlInput = before + "&c=" + self.textEdit_2.text() + after
            self.thread = self.MyThread(url, printQueue)
            self.thread.start()
            printThread = threading.Thread(target=self.textBrowserPrint, args=(printQueue,))
            printThread.start()
            # self.thread._signal.connect(self.callbacklog)

            # try:
            # t = threading.Thread(target=self.printHH(),  args=(20,), daemon=True)
            # t.start()
            # t.join()
        else:
            self.pushButton.setText("开始")
            self.start = True
            # self.thread.setstartBool()

        self.textBrowser.insertPlainText("下注金额为空，请输入金额\n")
        cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(cursor.End)

    def textBrowserPrint(self, queue):
        while self.start:
            print(queue.get())

    class MyThread(QtCore.QThread):
        # python3,pyqt5与之前的版本有些不一样
        #  通过类成员对象定义信号对象
        # _signal = pyqtSignal(str)
        startBool = True
        trigger = pyqtSignal()

        def __init__(self, urlstr, queue):
            super(self.MyThread, self).__init__()
            self.url = urlstr
            self.queue = queue

        def __del__(self):
            self.wait()

        def setstartBool(self):
            self.startBool = False

        def run(self):
            # 处理你要做的业务逻辑，这里是通过一个回调来处理数据，这里的逻辑处理写自己的方法
            # wechat.start_auto(self.callback)
            # self._signal.emit(msg);  可以在这里写信号焕发
            while self.startBool:
                self.gameStart(self.url)
                pass
            self.trigger.emit()
            # self._signal.emit(msg)

        def callback(self, msg):
            # 信号焕发，我是通过我封装类的回调来发起的
            # self._signal.emit(msg)
            pass

        def gameStart(self, url):
            try:
                print(url)
                indexNumber = int(url.split("&index=")[1].split("&counter=")[0]) + 1
                counter = int(url.split("&counter=")[1].split("&repeat=")[0]) + 2

                head = "curl" + url.split("curl")[1].split("--data")[0] + "--data "

                pattern = re.compile(r'\d+')
                while 1:
                    self.queue.put(indexNumber)
                    print(indexNumber + 4)
                    indexNumber += 1

                # while True:
                #     data = '\'action=doSpin&symbol=vs1dragon8&c=1&l=1&index=' + str(indexNumber) + '&counter=' + str(
                #         counter) + "&repeat=0" \
                #            + "&mgckey" + url.split("&mgckey")[-1]
                #     sendUrl = head + data
                #     result = os.popen(sendUrl).readlines()
                #
                #     if result[0].startswith("nomoney="):
                #         print("没钱了，请充值")
                #         # self.textBrowser.insertPlainText("没钱了，请充值")
                #         # cursor = self.textBrowser.textCursor()
                #         # self.textBrowser.moveCursor(cursor.End)
                #         break
                #
                #     if result == ['unlogged']:
                #         print("游戏发生错误")
                #         print("请重新输入正确的url")
                #         self.textBrowser.insertPlainText("游戏发生错误")
                #         self.textBrowser.insertPlainText("请重新输入正确的url")
                #         cursor = self.textBrowser.textCursor()
                #         self.textBrowser.moveCursor(cursor.End)
                #         break
                #
                #     print(result)
                #     if result[0].endswith("SystemError"):
                #         print("游戏停止，请重新复制url")
                #         self.textBrowser.insertPlainText("游戏停止，请重新复制url")
                #         cursor = self.textBrowser.textCursor()
                #         self.textBrowser.moveCursor(cursor.End)
                #         break
                #
                #     number = pattern.findall(result[0])
                #     if int(number[0]) == 0:
                #         print("没中奖")
                #         # self.textBrowser.insertPlainText("没中奖")
                #         # cursor = self.textBrowser.textCursor()
                #         # self.textBrowser.moveCursor(cursor.End)
                #         indexNumber = int(result[0].split("&index=")[1].split("&balance_cash=")[0]) + 1
                #         counter = int(result[0].split("&counter=")[1].split("&l=")[0]) + 2
                #         # self._signal.emit(indexNumber, counter)
                #         self.queue.put(indexNumber)
                #         time.sleep(0.005)
                #     else:
                #         print("中奖了")
                #         indexNumber = int(result[0].split("&index=")[1].split("&balance_cash=")[0]) + 1
                #         counter = int(result[0].split("&counter=")[1].split("&l=")[0]) + 2
                #         data = '\'symbol=vs1dragon8&action=doCollect&index=' + str(indexNumber) + '&counter=' + str(
                #             counter) + "&repeat=0" \
                #                + '&mgckey' + url.split("&mgckey")[-1]
                #         sendUrl = head + data
                #         result = os.popen(sendUrl).readlines()
                #         print(result)
                #         # self.textBrowser.insertPlainText("中奖了")
                #         # self.textBrowser.insertPlainText(result)
                #         # cursor = self.textBrowser.textCursor()
                #         # self.textBrowser.moveCursor(cursor.End)
                #         indexNumber = int(result[0].split("&index=")[1].split("&balance_cash=")[0]) + 1
                #         counter = int(result[0].split("&counter=")[1].split("&l=")[0]) + 2
            except:
                print("url错误，请重新粘贴")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_Dialog()  # ui是你创建的ui类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
