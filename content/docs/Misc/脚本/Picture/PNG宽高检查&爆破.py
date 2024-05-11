import binascii
import struct

print("PNG宽高检查&爆破")
FileName=input("输入文件地址：")
if(FileName[0]=="\"" and FileName[len(FileName)-1]=="\""):
    FileName=FileName[1:len(FileName)-1]

crcbp = open(FileName, "rb").read()
data_f = crcbp[:12]
data_r = crcbp[29: ]
crc32frombp = int(crcbp[29:33].hex(),16)

w=int(crcbp[16:20].hex(),16)
h=int(crcbp[20:24].hex(),16)

print("宽："+str(w))
print("高："+str(h))

def check_size(data):
    crc32 = binascii.crc32(data) & 0xffffffff
    if(crc32 == crc32frombp):
        return True

data = crcbp[12:16] + \
    struct.pack('>i', w)+struct.pack('>i', h)+crcbp[24:29]

if check_size(data):
    print("校验正确，无需爆破")
    exit(0)
    
print("校验不正确，开始爆破")
OutFileName=FileName[0:len(FileName)-4]+"_fixed.png"

while True:
    minw=int(input("最小宽："))
    maxw=int(input("最大宽："))
    minh=int(input("最小高："))
    maxh=int(input("最大高："))
    print("爆破中...")
    for i in range(minw,maxw):
        for j in range(minh,maxh):
            data = crcbp[12:16] + \
                struct.pack('>i', i)+struct.pack('>i', j)+crcbp[24:29]
            if check_size(data):
                output=open(OutFileName,'wb')
                output.write(data_f + data + data_r)
                print("爆破成功！")
                print("宽：",i)
                print("高：",j)
                print("文件已输出至",OutFileName)
                exit(0)
    print("爆破失败，请重试")
    
    