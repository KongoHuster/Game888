import os

indexNumber = 3
counter = 5

url = "curl 'https://bbin-tw.pragmaticplay.net/gs2c/v3/gameService' -H 'origin: https://bbin-tw.pragmaticplay.net' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36' -H 'content-type: application/x-www-form-urlencoded' -H 'accept: */*' -H 'referer: https://bbin-tw.pragmaticplay.net/gs2c/html5Game.do?jackpotid=0&gname=888%20Dragons&extGame=1&ext=0&cb_target=exist_tab&symbol=vs1dragon8&jurisdictionID=99&mgckey=AUTHTOKEN@94c3dec25c49286eacade486a29247d173c2b9c245a128c1e54ccf63e8a26e85~stylename@bbin~SESSION@010c91a8-b689-46c0-a26d-443722ceaa41&tabName=' -H 'authority: bbin-tw.pragmaticplay.net' -H 'cookie: _ga=GA1.3.782692004.1551164849; _gid=GA1.3.398648764.1551164849' --data 'action=doSpin&symbol=vs1dragon8&c=1&l=1&index=2&counter=3&repeat=0&mgckey=AUTHTOKEN@94c3dec25c49286eacade486a29247d173c2b9c245a128c1e54ccf63e8a26e85~stylename@bbin~SESSION@010c91a8-b689-46c0-a26d-443722ceaa41' --compressed"

head = "curl" + url.split("curl")[1].split("--data")[0] + "--data "

data = '\'action=doSpin&symbol=vs1dragon8&c=1&l=1&index=' + str(indexNumber) + '&counter=' + str(counter) + "&repeat=0" \
      +  "&mgckey" + url.split("&mgckey")[-1]

print(head + data)
print("\n\n")
print(url)
print('\n')

if url == head + data :
      print("hhh")

result = os.popen(head + data).readlines()
print(result)