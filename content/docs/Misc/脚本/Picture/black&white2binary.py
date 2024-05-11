import binascii
from PIL import Image

#打开图片
imgpath = "C:\\CTF\\temp\\Untitled1.png"
img = Image.open(imgpath)

#获取图片的像素
pix = img.load()
width = img.size[0]
height = img.size[1]

#将图片转换为二进制
for i in range(width):
    for j in range(height):
        if pix[i,j] == 0:
            pix[i,j] = 1
        else:
            pix[i,j] = 0
            
#将二进制转换为字符串
text = ""
for i in range(width):
    for j in range(height):
        text += str(pix[i,j])
        
#将字符串转换为十六进制
hexstr = hex(int(text,2))[2:]
print(hexstr)
