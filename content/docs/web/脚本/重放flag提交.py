# POST /api/v1/challenges/attempt HTTP/1.1
# Host: 182.148.156.200:60001
# Content-Length: 65
# Accept: application/json
# CSRF-Token: 865790361e4a3f8839b791b93f7db9b4c610d2a287cac6c627ca4eef591b80e5
# DNT: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57
# Content-Type: application/json
# Origin: http://182.148.156.200:60001
# Referer: http://182.148.156.200:60001/challenges
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
# Cookie: session=a2a5cc97-0295-4c12-b741-e826f5e600d7.epSmaX0dOkqjg8gAItL81RUW_Kw
# Connection: close

# {"challenge_id":27,"submission":"flag{hap1y~You~go@ooo1t~i1iIt}"}

import threading
import requests
import json
import time

url = "http://182.148.156.200:60001/api/v1/challenges/attempt"

headers = {
    'Host': '182.148.156.200:60001',
    'Content-Length': '65',
    'Accept': 'application/json',
    'CSRF-Token': '865790361e4a3f8839b791b93f7db9b4c610d2a287cac6c627ca4eef591b80e5',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
    'Content-Type': 'application/json',
    'Origin': 'http://182.148.156.200:60001',
    'Referer': 'http://182.148.156.200:60001/challenges',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': 'session=a2a5cc97-0295-4c12-b741-e826f5e600d7.epSmaX0dOkqjg8gAItL81RUW_Kw',
    'Connection': 'close'
}

payload = [
    json.dumps({"challenge_id": 27,"submission": "flag{hap1y~You~go@ooo1t~i1iIt}"}),
    json.dumps({"challenge_id":30,"submission":"flag{1uck_g4y_n0t_n55d_x0r}"}),
    json.dumps({"challenge_id":3,"submission":"flag{xhsobqyuctnedrwivkj}"}),
    json.dumps({"challenge_id":3,"submission":"flag{xhosqbuyctnedwrivkj}"}),
    json.dumps({"challenge_id":rsa,"submission":"flag{Duom1ngsh1sanqiang}"}),
    json.dumps({"challenge_id":re4,"submission":"flag{woshiikun666}"}),
]

# 定义一个计数器（动态数组），根据len(payload)来定义
count = [0 for i in range(len(payload))]


# 定义一个线程
def thread(payload,i):
    while True:
        response = requests.request("POST", url, headers=headers, data=payload[i])
        print("time: "+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+", count: "+str(count[i]))
        count[i] += 1
        print("id: "+ payload[i].split(",")[0].split(":")[1] + " " + response.text)
        time.sleep(10)
        if "incorrect" in response.text:
            print("error")
            break
        if "paused" in response.text:
            continue
        if "correct" in response.text:
            print("success")
            break
        if "Internal Server Error" in response.text:
            time.sleep(10)
            continue
        else :
            break
        
# 启动线程
for i in range(len(payload)):
    t = threading.Thread(target=thread, args=(payload,i))
    t.start()
    time.sleep(10/len(payload))

