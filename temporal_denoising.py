#coding:utf-8  
import sys,os  
from PIL import Image,ImageDraw  
  
#使用二值判断方法,如果确认是噪声,用该点的上面一个点的灰度进行替换  
def getPixel(image,x,y,G,N):  
    L = image.getpixel((x,y))  
    if L > G:  
        L = True  
    else:  
        L = False  
  
    nearDots = 0  
    if L == (image.getpixel((x - 1,y - 1)) > G):  
        nearDots += 1  
    if L == (image.getpixel((x - 1,y)) > G):  
        nearDots += 1  
    if L == (image.getpixel((x - 1,y + 1)) > G):  
        nearDots += 1  
    if L == (image.getpixel((x,y - 1)) > G):  
        nearDots += 1  
    if L == (image.getpixel((x,y + 1)) > G):  
        nearDots += 1  
    if L == (image.getpixel((x + 1,y - 1)) > G):  
        nearDots += 1  
    if L == (image.getpixel((x + 1,y)) > G):  
        nearDots += 1  
    if L == (image.getpixel((x + 1,y + 1)) > G):  
        nearDots += 1  
  
    if nearDots < N:  
        return image.getpixel((x,y-1))  
    else:  
        return None  
  
# 降噪段
# 根据一个点A的灰度值，与周围的8个点的灰度值比较，设定一个值N（0 <N <8），当A的灰度值与周围8个点的灰度相等数小于N时，此点为噪点   
# G:图像二值化阀值   
# N:降噪率 0 <N <8   
# Z:降噪次数   

def deNoise(image,G,N,Z):  
    draw = ImageDraw.Draw(image)  
  
    for i in range(0,Z):  
        for x in range(1,image.size[0] - 1):  
            for y in range(1,image.size[1] - 1):  
                color = getPixel(image,x,y,G,N)  
                if color != None:  
                    draw.point((x,y),color)  
  
#测试代码  
def main():  
    #打开图片  
    image = Image.open("./source.jpg")  

    #将图片转换成灰度图片  
    image = image.convert("L")  

    #去噪,G = 50,N = 4,Z = 4  
    deNoise(image,50,4,4)

    #保存图片  
    image.save("./result.jpg")  
    
    print("done")
    
if __name__ == '__main__':  
    main()  