from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal


class MyThread(QtCore.QThread):
    # python3,pyqt5与之前的版本有些不一样
    #  通过类成员对象定义信号对象
    # _signal = pyqtSignal(str)
    startBool = True
    trigger = pyqtSignal()

    def __init__(self, parent=None):
        super(MyThread, self).__init__()

    def __del__(self):
        self.wait()

    def setstartBool(self):
        self.startBool = False

    def run(self):
        # 处理你要做的业务逻辑，这里是通过一个回调来处理数据，这里的逻辑处理写自己的方法
        # wechat.start_auto(self.callback)
        # self._signal.emit(msg);  可以在这里写信号焕发
        while self.startBool:
            print("12")
            pass
        self.trigger.emit()
        # self._signal.emit(msg)

    def callback(self, msg):
        # 信号焕发，我是通过我封装类的回调来发起的
        # self._signal.emit(msg)
        pass