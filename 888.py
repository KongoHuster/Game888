import requests
import time

date = str(int(time.time() * 1000)) 


print(date)


url = "https://bbin-tw.pragmaticplay.net/gs2c/html5Game.do?jackpotid=0&gname=888%20Dragons&extGame=1&ext=0&cb_target=exist_tab&symbol=vs1dragon8&jurisdictionID=99&mgckey=AUTHTOKEN@1743de549dec5c750b1fcca844eabdb10ec630b329b756f7e652a36c5817ebc3~stylename@bbin~SESSION@042b5b06-acdf-4ee9-90ba-0fb7ecacd137&tabName="

token  = "7ba69023cb8f0a3ab7985cf88e348f05b3d23b70b601d83d28bc298b3c87de58"

header = {
    "Authorization": token,
    "content-length": "170",
    "content-type" : "text/html",
    "content-type" : "charset=UTF-8",
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}



data = {
    "tw" : "0.00",
    "balance" :"94.00",
    "index" : "3",
    "balance_cash" : "94.00",
    "balance_bonus" : "0.00",
    "na" : "s",
    "stime" : date,
    "sa" : "6, 6, 5",
    "sb" : "6, 6, 5",
    "sh" : "3",
    "c" : "1.00",
    "sver" : "5",
    "counter" : "6",
    "l" : "1",
    "s" : "3, 3, 6, 6, 6, 5, 5, 5, 6",
    "w" : "0.00"
}

res = requests.post(url, headers=header, data=data)
# print(res.url)
print(res.headers)
print(res.status_code)
print("\n\n\n\n")
print(res.text)
# print("\n\n\n\n")
# print(res.content)
