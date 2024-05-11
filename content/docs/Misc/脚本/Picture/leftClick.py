import pynput
import time

# 开始后倒数三秒，之后每一秒模拟一次鼠标左键点击
def start():
    print('开始')
    time.sleep(3)
    while True:
        mouse.click(pynput.mouse.Button.left)
        time.sleep(1)

if __name__ == '__main__':
    mouse = pynput.mouse.Controller()
    start()