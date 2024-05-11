import sys
from PIL import Image

# 导入图片

imgpath = "C:\\CTF\\temp\\398cf145c92f920e637680e93707ee62cc6312f0.png"
img = Image.open(imgpath)

# 获取图片的宽和高
width = img.size[0]
height = img.size[1]

data = []
            
# 按行读取图片
for i in range(height):
    for j in range(width):
        pixel = img.getpixel((j, i))
        # print(pixel)
        if(not pixel[0] & 128 == 128):
            if(pixel[0] & 4 == 4):
                data.append(1)
            else:
                data.append(0)

# 将0和1形式的二进制数组data转换为bytes并写入文件
# 定义一个空的bytes
bytes = b''
for i in range(len(data)):
    # 每8位转换为一个字符
    if(i % 8 == 0):
        # 将8位二进制转换为一个字符
        bytes += int(''.join(str(x) for x in data[i:i+8]), 2).to_bytes(1, byteorder='big')

# 将bytes写入文件
with open('C:\\CTF\\temp\\data', 'wb') as f:
    f.write(bytes)