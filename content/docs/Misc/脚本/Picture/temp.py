from PIL import Image
filename = r"ctf-new/Picture/depthpng.png"
im = Image.open(filename)
# 图片的宽度和高度
x, y = im.size
print("图片宽度和高度分别是{},{}".format(x, y))
img_array=im.load()
 
for i in range(x):
    for j in range(y):
        print(img_array[i,j], end=' ')