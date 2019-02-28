import os
import re

url = "curl 'https://bbin-tw.pragmaticplay.net/gs2c/v3/gameService' -H 'origin: https://bbin-tw.pragmaticplay.net' -H " \
      "'accept-encoding: gzip, deflate, br' -H 'accept-language: zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6' -H " \
      "'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) " \
      "Chrome/72.0.3626.119 Safari/537.36' -H 'content-type: application/x-www-form-urlencoded' -H 'accept: */*' -H " \
      "'referer: https://bbin-tw.pragmaticplay.net/gs2c/html5Game.do?jackpotid=0&gname=888%20Dragons&extGame=1&ext=0" \
      "&cb_target=exist_tab&symbol=vs1dragon8&jurisdictionID=99&mgckey=AUTHTOKEN" \
      "@2d49aba7f2360f63e9e9622860b72644587ff4e4dfff9ea335e4d9015ce0cfb8~stylename@bbin~SESSION@0ca09b84-eac2-484e" \
      "-ab72-ee18bb1ed189&tabName=' -H 'authority: bbin-tw.pragmaticplay.net' -H 'cookie: " \
      "_ga=GA1.3.782692004.1551164849; _gid=GA1.3.398648764.1551164849' --data " \
      "'action=doInit&symbol=vs1dragon8&cver=36308&index=1&counter=1&repeat=0&mgckey=AUTHTOKEN" \
      "@2d49aba7f2360f63e9e9622860b72644587ff4e4dfff9ea335e4d9015ce0cfb8~stylename@bbin~SESSION@0ca09b84-eac2-484e" \
      "-ab72-ee18bb1ed189' --compressed "

indexNumber = 2
counter = 3

head = "curl" + url.split("curl")[1].split("--data")[0] + "--data "

pattern = re.compile(r'\d+')

for i in range(100):
    data = '\'action=doSpin&symbol=vs1dragon8&c=1&l=1&index=' + str(indexNumber) + '&counter=' + str(
        counter) + "&repeat=0" \
           + "&mgckey" + url.split("&mgckey")[-1]
    sendUrl = head + data
    result = os.popen(sendUrl).readlines()

    if result == ['unlogged']:
        print("请输入正确的url")
        break

    print(result)
    number = pattern.findall(result[0])

    if int(number[0]) == 0:
        print("没中奖")
        indexNumber = int(result[0].split("&index=")[1].split("&balance_cash=")[0]) + 1
        counter = int(result[0].split("&counter=")[1].split("&l=")[0]) + 2
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
print('退出成功')

# result = os.popen(head + data).readlines()
# print(result)
