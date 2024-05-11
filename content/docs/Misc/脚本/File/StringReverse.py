print("字符串倒置")
FileName=input("输入文件名：")
if(FileName[0]=="\"" and FileName[len(FileName)-1]=="\""):
    FileName=FileName[1:len(FileName)-1]
OutFileName=input("输出文件名：")
if(OutFileName[0]=="\"" and OutFileName[len(OutFileName)-1]=="\""):
    OutFileName=OutFileName[1:len(OutFileName)-1]
input = open(FileName,'rb')
input_all=input.read()
ss=input_all[::-1]
output=open(OutFileName,'wb')
output.write(ss)
input.close
output.close
print("Successful!")
exit()