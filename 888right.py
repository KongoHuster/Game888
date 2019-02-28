import os
import re
import time


def gameStart(url):
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
            break

        if result == ['unlogged']:
            print("游戏发生错误")
            print("请输入正确的url")
            break

        print(result)
        if result[0].endswith("SystemError"):
            print("游戏停止，请重新复制url")
            break

        number = pattern.findall(result[0])
        if int(number[0]) == 0:
            print("没中奖")
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
            indexNumber = int(result[0].split("&index=")[1].split("&balance_cash=")[0]) + 1
            counter = int(result[0].split("&counter=")[1].split("&l=")[0]) + 2

# print(head + data)
# print("\n\n")
# print(url)

# result = os.popen(head + data).readlines()
# print(result)
