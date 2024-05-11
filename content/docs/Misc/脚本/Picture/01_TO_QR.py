# 读取文本，转换为图片，格式为0110101001010101010101011010，即黑白值，要求将这些黑白值转换为图片
import os
import sys
from PIL import Image

def main():
    text = r"C:\\CTF\\temp\\6.26\\convert\\1.txt"
    pixels = []
    with open(text, 'r') as f:
        lines = f.readlines()
    for line in lines:
        for i in range(len(line)):
            if line[i] == '0':
                pixels.append(0)
            elif line[i] == '1':
                pixels.append(255)

    length = len(pixels)
    import math
    x_max = 0
    y_max = 0
    for i in range(1, int(math.sqrt(length))+1):
        if length % i == 0:
            x_max = i
            y_max = length // i

            img = Image.new('L', (x_max, y_max))
            # 从左往右，从上往下
            for y in range(y_max):
                for x in range(x_max):
                    img.putpixel((x, y), pixels[y*x_max+x])

            img.save(r"C:\\CTF\\temp\\6.26\\convert\\1\\1.png")

        


if __name__ == "__main__":
    main()