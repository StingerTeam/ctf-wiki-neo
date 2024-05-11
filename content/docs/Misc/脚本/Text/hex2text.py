import zlib
import binascii
import base64
id='a77e60356191c'
result =binascii.unhexlify(id)
print (result)
result = zlib.decompress(result)
print (result)