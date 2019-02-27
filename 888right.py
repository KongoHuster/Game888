import os
import sys

url = "curl 'https://bbin-tw.pragmaticplay.net/gs2c/v3/gameService' -H 'Referer: https://bbin-tw.pragmaticplay.net/gs2c/html5Game.do?jackpotid=0&gname=888%20Dragons&extGame=1&ext=0&cb_target=exist_tab&symbol=vs1dragon8&jurisdictionID=99&mgckey=AUTHTOKEN@a30f2fab201014f5d2959481897f33d448d2e3899666240e0abf6463d830e404~stylename@bbin~SESSION@8164ea73-933d-4059-892c-c20faf983ea1&tabName=' -H 'Origin: https://bbin-tw.pragmaticplay.net' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36' -H 'Content-type: application/x-www-form-urlencoded' --data 'action=doSpin&symbol=vs1dragon8&c=1&l=1&index=2&counter=3&repeat=0&mgckey=AUTHTOKEN@a30f2fab201014f5d2959481897f33d448d2e3899666240e0abf6463d830e404~stylename@bbin~SESSION@8164ea73-933d-4059-892c-c20faf983ea1' --compressed"


indexNumber = 3
counter = 5

head = "curl" + url.split("curl")[1].split("--data")[0] + "--data "

for i in range(100):
      data = '\'action=doSpin&symbol=vs1dragon8&c=1&l=1&index=' + str(indexNumber) + '&counter=' + str(counter) + "&repeat=0" \
            +  "&mgckey" + url.split("&mgckey")[-1]
      sendUrl = head + data
      result = os.popen(sendUrl).readlines()
      print(result)

      print(result[i].split("tw=")[1].split("&balance")[0])

      if(float(result[i].split("tw=")[1].split("&balance")[0]) == 0):
            print("没中奖")
            indexNumber += 1
            counter += 2
      else:
            print("中奖了")
            indexNumber += 1
            counter += 2
            data = '\'symbol=vs1dragon8&action=doCollect&index=' + str(indexNumber) + '&counter=' + str(counter) + "&repeat=0" \
            +  "&mgckey" + url.split("&mgckey")[-1]
            sendUrl = head + data
            result = os.popen(sendUrl).readlines()
            print(result)
            indexNumber += 1
            counter += 2




# print(head + data)
# print("\n\n")
# print(url)
# print('\n')

if url == head + data :
      print("hhh")

# result = os.popen(head + data).readlines()
# print(result)