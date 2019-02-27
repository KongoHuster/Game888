import os

url = "curl 'https://bbin-tw.pragmaticplay.net/gs2c/v3/gameService' \
      -H 'origin: https://bbin-tw.pragmaticplay.net' \
      -H 'accept-encoding: gzip, deflate, br' \
      -H 'accept-language: zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6' \
      -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'  \
      -H 'content-type: application/x-www-form-urlencoded' \
      -H 'accept: */*' \
      -H 'referer: https://bbin-tw.pragmaticplay.net/gs2c/html5Game.do?jackpotid=0&gname=888%20Dragons&extGame=1&ext=0&cb_target=exist_tab&symbol=vs1dragon8&jurisdictionID=99&mgckey=AUTHTOKEN@48cd12fd362d43f10658aa1e4749aed38f9e21193a790f560505bef6a48f131b~stylename@bbin~SESSION@93dc3b35-2ff3-4434-a9bd-fde8966e70f0&tabName=' \
      -H 'authority: bbin-tw.pragmaticplay.net' \
      -H 'cookie: _ga=GA1.3.782692004.1551164849; _gid=GA1.3.398648764.1551164849' \
      --data 'action=doSpin&symbol=vs1dragon8&c=1&l=1&index=4&counter=7&repeat=0&mgckey=AUTHTOKEN@48cd12fd362d43f10658aa1e4749aed38f9e21193a790f560505bef6a48f131b~stylename@bbin~SESSION@93dc3b35-2ff3-4434-a9bd-fde8966e70f0' \
      --compressed"

result = os.popen(url).readlines()
print(result)