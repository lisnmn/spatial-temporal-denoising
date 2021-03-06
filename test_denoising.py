#测试用库
import unittest

import temporal_denoising as td
import sys,os  
from PIL import Image,ImageDraw  

#测试代码  
class Test_denoising(unittest.TestCase):
    def test_denoising(self):
        td.main()
        image_source = Image.open("./source.jpg")
        image_source = image_source.convert("L")
        image_result = Image.open("./result.jpg")
        image_result = image_result.convert("L")
        td.deNoise(image_source,50,4,4)
        image_source.save("./test.jpg")
        image_test = Image.open("./test.jpg")
        for x in range(1,image_source.size[0] - 1):  
            for y in range(1,image_source.size[1] - 1):  
                self.assertEqual(image_test.getpixel((x,y)),image_result.getpixel((x,y)))