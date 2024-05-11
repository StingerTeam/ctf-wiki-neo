# 有一个文件，内含类似
# (7,7)
# (7,8)
# (7,9)
# 的坐标，要求将这些坐标转换为图片，图片长宽分别为x,y的最大值+1

import os
import sys
import numpy as np
from PIL import Image

def main():
    # 读取文件
    filename = r"C:\\CTF\\temp\\zb.txt"
    with open(filename, 'r') as f:
        lines = f.readlines()
    # 读取坐标
    x = []
    y = []
    for line in lines:
        x.append(int(line.split('(')[1].split(',')[0]))
        y.append(int(line.split(',')[1].split(')')[0]))
    # 生成图片
    x_max = max(x)
    y_max = max(y)
    img = np.zeros((x_max+1, y_max+1))
    for i in range(len(x)):
        img[x[i], y[i]] = 255
    # img = Image.fromarray(img)
    # img.save(r"C:\\CTF\\temp\\zb.png")
    # cannot write mode F as PNG
    img = Image.fromarray(img.astype('uint8'))
    img.save(r"C:\\CTF\\temp\\zb.png")
    
if __name__ == "__main__":
    main()