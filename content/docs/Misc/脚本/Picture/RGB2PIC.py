# 读取文本，转换为图片，每行的格式为(255,255,255)，即RGB值，要求将这些RGB值转换为图片，图片长宽由文件中的行数决定

import os
import sys
from PIL import Image

def main():
    text = r"C:\\CTF\\temp\\6.27\\杂项\\basic.txt"
    with open(text, 'r') as f:
        lines = f.readlines()
    R = []
    G = []
    B = []
    for line in lines:
        R.append(int(line.split('(')[1].split(',')[0]))
        G.append(int(line.split(',')[1]))
        B.append(int(line.split(',')[2].split(')')[0]))
    lines = len(lines)
    # 长宽为lines开方
    # 将lines分解为两个整因数，找到最接近的两个整因数
    import math
    x_max = 0
    y_max = 0
    for i in range(1, int(math.sqrt(lines))+1):
        if lines % i == 0:
            x_max = i
            y_max = lines // i
            img = Image.new('RGB', (x_max, y_max))
            for i in range(lines):
                img.putpixel((i//y_max, i%y_max), (R[i], G[i], B[i]))
            img.save(r"C:\\CTF\\temp\\6.27\\杂项\\basic"+str(y_max)+".png")



if __name__ == "__main__":
    main()