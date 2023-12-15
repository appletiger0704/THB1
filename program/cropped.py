# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 14:37:02 2023

@author: User
"""

from PIL import Image
from datetime import datetime
import os


now = datetime.now()
today = now.strftime("%Y%m%d")
path = rf"C:\Users\User\Desktop\North_auto\{today}"
img = ["6_06QPF.png", "6_12QPF.png", "6_18QPF.png", "6_24QPF.png"]
os.chdir(path)

# 設定要裁剪的區域 (左, 上, 右, 下)
crop_area = (650, 170, 1125, 540)

def cropped(img):
    
    image = Image.open(os.path.join(path, img))
    cropped_image = image.crop(crop_area)
    cropped_image.save("cropped_" + img)

for i in img:
    
    cropped(i)
    