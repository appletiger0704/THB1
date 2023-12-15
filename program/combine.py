# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:17:18 2023

@author: User
"""

from PIL import Image
import os
from datetime import datetime

now = datetime.now()
today = now.strftime("%Y%m%d")

path = rf"C:\Users\User\Desktop\North_auto\{today}"

os.chdir(path)

img = ["cropped_6_06QPF.png", "cropped_6_12QPF.png", "cropped_6_18QPF.png", "cropped_6_24QPF.png"]

road_path = r"C:\Users\User\Desktop\North_auto\road.png"

image2 = Image.open(road_path)

for i in img:
    
    image1 = Image.open(os.path.join(path, i))
    image1.alpha_composite(image2, (21, 0))
    image1.save(i)