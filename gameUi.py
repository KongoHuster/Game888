# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gameUi.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import re
import time
import threading
import mythread

class Ui_Dialog(object):
    indexNumber = ""
    counter = ""
    start = True

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
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
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 70, 51, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 80, 60, 16))
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
        self.textEdit_2.setHtml(_translate("Dialog",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                           "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                           "type=\"text/css\">\n "
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.SF NS Text\'; "
                                           "font-size:13pt; font-weight:400; font-style:normal;\">\n "
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                           "margin-right:0px; -qt-block-indent:0; "
                                           "text-indent:0px;\">1</p></body></html>"))
        self.label_5.setText(_translate("Dialog", "下注"))

    def startPlay(self):
        if self.start is True:
            self.pushButton.setText("关闭")
            if self.textEdit.toPlainText() is "":
                self.textBrowser.insertPlainText("第一行为空，请添加curl\n")
                cursor = self.textBrowser.textCursor()
                self.textBrowser.moveCursor(cursor.End)
                return

            if self.textEdit_2.toPlainText() is "":
                self.textBrowser.insertPlainText("下注金额为空，请输入金额")
                cursor = self.textBrowser.textCursor()
                self.textBrowser.moveCursor(cursor.End)
                return

            self.thread = mythread.MyThread()
            self.thread.start()
            # try:
            # t = threading.Thread(target=self.printHH(),  args=(20,), daemon=True)
            # t.start()
            # t.join()
        else:
            self.pushButton.setText("开始")
            self.start = False

        self.textBrowser.insertPlainText("下注金额为空，请输入金额")
        cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(cursor.End)


    def gameStart(self, url):
        indexNumber = int(url.split("&index=")[1].split("&counter=")[0]) + 1
        counter = int(url.split("&counter=")[1].split("&repeat=")[0]) + 2

        head = "curl" + url.split("curl")[1].split("--data")[0] + "--data "

        pattern = re.compile(r'\d+')

        while True:
            data = '\'action=doSpin&symbol=vs1dragon8&c=1&l=1&index=' + str(indexNumber) + '&counter=' + str(
                counter) + "&repeat=0" \
                   + "&mgckey" + url.split("&mgckey")[-1]
            sendUrl = head + data
            result = os.popen(sendUrl).readlines()

            if result[0].startwith("nomoney="):
                print("没钱了，请充值")
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
                print("没中奖")
                self.textBrowser.insertPlainText("没中奖")
                cursor = self.textBrowser.textCursor()
                self.textBrowser.moveCursor(cursor.End)
                indexNumber = int(result[0].split("&index=")[1].split("&balance_cash=")[0]) + 1
                counter = int(result[0].split("&counter=")[1].split("&l=")[0]) + 2
                time.sleep(0.005)
            else:
                print("中奖了")
                indexNumber = int(result[0].split("&index=")[1].split("&balance_cash=")[0]) + 1
                counter = int(result[0].split("&counter=")[1].split("&l=")[0]) + 2
                data = '\'symbol=vs1dragon8&action=doCollect&index=' + str(indexNumber) + '&counter=' + str(
                    counter) + "&repeat=0" \
                       + '&mgckey' + url.split("&mgckey")[-1]
                sendUrl = head + data
                result = os.popen(sendUrl).readlines()
                print(result)
                self.textBrowser.insertPlainText("中奖了")
                self.textBrowser.insertPlainText(result)
                cursor = self.textBrowser.textCursor()
                self.textBrowser.moveCursor(cursor.End)
                indexNumber = int(result[0].split("&index=")[1].split("&balance_cash=")[0]) + 1
                counter = int(result[0].split("&counter=")[1].split("&l=")[0]) + 2


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_Dialog()  # ui是你创建的ui类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
