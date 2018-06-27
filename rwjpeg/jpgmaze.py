from PIL import Image
import numpy as np

im = np.array(Image.open('D:/red.jpg').convert('L'))#Image.open("D:/red.jpg")

step=20
with open('D:/1.txt', 'w', encoding='utf-8') as f:
    for w in range(0,747,step):
        for h in range(0,747,step):
            sumbox = im[w:w+step, h:h+step].sum()
            if sumbox < 10000:
                f.write("0 ")
            else:
                f.write("1 ")
        f.write("\r\n")

print(sumbox)

#im.show()
