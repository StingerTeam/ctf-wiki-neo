# -*- coding: utf-8 -*-

import jwt

data = {
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}

# 加密 py3加密后是字节型数据
encoded = jwt.encode(data, 'secret', algorithm='HS256')
print(encoded.decode())
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.
# eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.
# DzMJlzRbt6kdh1Kbbqv8SA8QsddwfSoM1bqw41tQY2k


print(jwt.decode(encoded, 'secret', algorithms=['HS256']))
# {'sub': '1234567890', 'name': 'John Doe', 'iat': 1516239022}

