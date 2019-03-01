from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
import re
import os
import time

class MyThread(QtCore.QThread):
    # python3,pyqt5与之前的版本有些不一样
    #  通过类成员对象定义信号对象
    # _signal = pyqtSignal(str)
    startBool = True
    trigger = pyqtSignal()

    def __init__(self, urlstr):
        super(MyThread, self).__init__()
        self.url = urlstr

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
        except:
                print("url错误，请重新粘贴")