import re

def findFirstNumber(str):
    match = re.search(r'\d+', str)
    if match:
        number = match.group()
        return number

f=open('ctf-new/Web/PortScan/terminal.txt')
lines=f.readlines()
text=""

for line in lines:
    text=text+findFirstNumber(line)+","
print(text)
